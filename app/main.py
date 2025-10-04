"""
CuraLoop Backend - Main Application Entry Point
Combines all routers and provides a unified FastAPI application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

# Import routers from different modules
from patient.intake import router as intake_router
from analysis.diagnosis_treatment_planning import router as analysis_router, configure_llm

# Create main FastAPI application
app = FastAPI(
    title="CuraLoop Backend API",
    description="AI-powered continuous care for Alzheimer's patients",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(intake_router)
app.include_router(analysis_router)

# Root endpoint
@app.get("/")
def root():
    return {
        "service": "CuraLoop Backend API",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "intake": "/api/patient/{patient_id}/intake/*",
            "analysis": "/api/analysis/*"
        }
    }

# Health check endpoint
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "CuraLoop Backend API"
    }

# Admin endpoint to configure LLM
@app.post("/api/admin/configure-llm")
def configure_llm_endpoint(api_key: str, provider: str = "openai"):
    configure_llm(api_key, provider)
    return {
        "status": "success",
        "message": f"LLM configured with provider: {provider}",
        "llm_available": True
    }

# Run the application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
