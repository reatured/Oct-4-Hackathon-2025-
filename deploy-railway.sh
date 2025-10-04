#!/bin/bash

# Railway Deployment Script for CuraLoop Backend

echo "🚀 CuraLoop Backend - Railway Deployment"
echo "=========================================="
echo ""

# Check if Railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "❌ Railway CLI not found. Installing..."
    npm install -g @railway/cli
else
    echo "✅ Railway CLI is installed (version: $(railway --version))"
fi

echo ""
echo "Step 1: Login to Railway"
echo "------------------------"
railway login
echo ""

echo "Step 2: Initialize Railway Project"
echo "-----------------------------------"
railway init
echo ""

echo "Step 3: Deploy to Railway"
echo "-------------------------"
railway up
echo ""

echo "Step 4: Get Deployment URL"
echo "--------------------------"
railway domain
echo ""

echo "🎉 Deployment Complete!"
echo ""
echo "To view your app:"
echo "  railway open"
echo ""
echo "To view logs:"
echo "  railway logs"
echo ""
echo "To set environment variables (optional):"
echo "  railway variables set OPENAI_API_KEY=your_key_here"
echo ""
