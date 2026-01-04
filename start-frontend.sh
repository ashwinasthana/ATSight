#!/bin/bash
cd /Users/ashwinasthana/Documents/GitHub/ATSight/frontend
npm install -q 2>/dev/null || true
echo "✅ Frontend dependencies installed"
echo "🚀 Starting frontend on http://localhost:3000"
npm run dev
