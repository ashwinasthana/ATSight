#!/bin/bash
cd /Users/ashwinasthana/Documents/GitHub/ATSight/backend
python -m venv venv 2>/dev/null || true
source venv/bin/activate
pip install -q -r requirements.txt 2>/dev/null || true
echo "✅ Backend dependencies installed"
echo "🚀 Starting backend on http://localhost:8000"
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
