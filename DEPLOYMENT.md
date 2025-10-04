# CuraLoop Backend - Railway Deployment Guide

## Quick Deploy to Railway

### Prerequisites
- A [Railway](https://railway.app/) account
- GitHub repository connected to Railway (optional but recommended)

### Deployment Steps

#### Option 1: Deploy from GitHub (Recommended)

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Railway deployment"
   git push origin main
   ```

2. **Create a New Project in Railway**
   - Go to [Railway Dashboard](https://railway.app/dashboard)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Railway will automatically**
   - Detect Python project
   - Install dependencies from `requirements.txt`
   - Use the `Procfile` or `railway.toml` for startup command
   - Assign a PORT environment variable

4. **Configure Environment Variables (Optional)**
   - In Railway Dashboard, go to your project
   - Click on "Variables" tab
   - Add `OPENAI_API_KEY` if you want LLM-enhanced features
   - Add `LLM_PROVIDER=openai` (default)

5. **Deploy**
   - Railway will automatically deploy
   - You'll get a public URL like `https://your-app.up.railway.app`

#### Option 2: Deploy using Railway CLI

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**
   ```bash
   railway login
   ```

3. **Initialize Railway Project**
   ```bash
   railway init
   ```

4. **Deploy**
   ```bash
   railway up
   ```

5. **Set Environment Variables**
   ```bash
   railway variables set OPENAI_API_KEY=your_api_key_here
   ```

6. **Open your deployed app**
   ```bash
   railway open
   ```

### Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `PORT` | Auto-set | Railway automatically sets this |
| `OPENAI_API_KEY` | Optional | For LLM-enhanced diagnosis and treatment planning |
| `LLM_PROVIDER` | Optional | Default is "openai" |

### API Endpoints

Once deployed, your API will be available at:
- Health Check: `GET /health`
- Root: `GET /`
- Patient Intake Start: `POST /api/patient/{patient_id}/intake/start`
- Patient Intake Reply: `POST /api/patient/{patient_id}/intake/reply`
- Patient Intake State: `GET /api/patient/{patient_id}/intake/state`
- Analysis Health: `GET /api/analysis/health`
- Direct Analysis: `POST /api/analysis/direct`
- Configure LLM: `POST /api/admin/configure-llm`

### Testing Your Deployment

```bash
# Health check
curl https://your-app.up.railway.app/health

# Start intake
curl -X POST https://your-app.up.railway.app/api/patient/123/intake/start

# Direct analysis
curl -X POST https://your-app.up.railway.app/api/analysis/direct \
  -H "Content-Type: application/json" \
  -d '{"patient_data": {...}}'
```

### Monitoring

- Railway provides built-in monitoring and logs
- View logs: Railway Dashboard → Your Project → Deployments → View Logs
- Metrics: Railway Dashboard → Your Project → Metrics

### Custom Domain (Optional)

1. Go to Railway Dashboard → Your Project → Settings
2. Click "Add Custom Domain"
3. Enter your domain and follow DNS configuration instructions

### Troubleshooting

**Build Fails:**
- Check `requirements.txt` for correct package versions
- Ensure Python 3.9+ is specified if needed

**App Crashes:**
- Check Railway logs for error messages
- Verify ML model files are included in repository
- Ensure `app/main.py` imports are correct

**ML Model Not Loading:**
- Ensure `ml/` directory with model files is in repository:
  - `alzheimers_model.joblib`
  - `alzheimers_scaler.joblib`
  - `feature_names.joblib`

### Updating Your Deployment

Railway auto-deploys when you push to your connected GitHub branch:

```bash
git add .
git commit -m "Update backend"
git push origin main
```

Railway will automatically rebuild and redeploy.

### Costs

- Railway offers a free tier with some limitations
- For production use, consider upgrading to a paid plan
- Monitor your usage in Railway Dashboard

## Support

For Railway-specific issues:
- [Railway Documentation](https://docs.railway.app/)
- [Railway Discord](https://discord.gg/railway)

For application issues:
- Check application logs in Railway Dashboard
- Review API documentation at your deployment URL
