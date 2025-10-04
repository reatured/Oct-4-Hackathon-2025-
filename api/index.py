"""
CuraLoop Backend API - Vercel Entry Point
Main FastAPI application that combines all module routers
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import only the router from analysis (not the full app)
from app.analysis.diagnosis_treatment_planning import router as analysis_router

# For intake, we need to import the router without triggering app creation
# Import the intake module's router directly
import importlib.util
spec = importlib.util.spec_from_file_location("intake", os.path.join(os.path.dirname(__file__), '..', 'app', 'patient', 'intake.py'))
intake_module = importlib.util.module_from_spec(spec)
sys.modules['intake'] = intake_module
spec.loader.exec_module(intake_module)
intake_router = intake_module.router

# Create FastAPI application
app = FastAPI(
    title="CuraLoop API",
    description="AI Companion for Alzheimer's Continuous Care",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(analysis_router)
app.include_router(intake_router)

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "CuraLoop API",
        "version": "1.0.0",
        "status": "healthy",
        "endpoints": {
            "analysis": "/api/analysis",
            "patient_intake": "/api/patient",
            "docs": "/docs",
            "openapi": "/openapi.json"
        }
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "CuraLoop Backend API"
    }

# Export the app for Vercel
# Vercel will automatically detect and use the 'app' variable
