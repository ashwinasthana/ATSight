#!/bin/bash

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                  🚀 ATSight - Starting All                    ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Backend setup
echo "📦 Setting up backend..."
cd /Users/ashwinasthana/Documents/GitHub/ATSight/backend
python -m venv venv 2>/dev/null || true
source venv/bin/activate
pip install -q -r requirements.txt 2>/dev/null || true
echo "✅ Backend ready"
echo ""

# Frontend setup
echo "📦 Setting up frontend..."
cd /Users/ashwinasthana/Documents/GitHub/ATSight/frontend
npm install -q 2>/dev/null || true
echo "✅ Frontend ready"
echo ""

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                   🎯 Ready to Start                           ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo "Run in separate terminals:"
echo ""
echo "Terminal 1 (Backend):"
echo "  cd /Users/ashwinasthana/Documents/GitHub/ATSight/backend"
echo "  source venv/bin/activate"
echo "  python -m uvicorn app.main:app --reload"
echo ""
echo "Terminal 2 (Frontend):"
echo "  cd /Users/ashwinasthana/Documents/GitHub/ATSight/frontend"
echo "  npm run dev"
echo ""
echo "Then open: http://localhost:3000"
echo ""
