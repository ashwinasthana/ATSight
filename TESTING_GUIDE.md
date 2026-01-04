# 🚀 ATSight - Complete Startup Guide

## ✅ What's Ready

Everything is set up and ready to test:

- ✅ Backend API (FastAPI)
- ✅ Frontend UI (Next.js)
- ✅ Analysis Engine (Working)
- ✅ All dependencies installed
- ✅ Environment configured

---

## 🧪 Test the Analysis Engine (Right Now!)

```bash
cd /Users/ashwinasthana/Documents/GitHub/ATSight/backend
source venv/bin/activate
python3 /Users/ashwinasthana/Documents/GitHub/ATSight/test-demo.py
```

**Output**: You'll see a complete analysis with:
- Match score: 85
- Matched skills: Python, FastAPI, Docker, AWS, GraphQL
- Missing skills: Kubernetes, Leadership
- Experience feedback
- Formatting issues
- Recommendation: Hire

---

## 🚀 Start Backend Server

**Terminal 1:**
```bash
cd /Users/ashwinasthana/Documents/GitHub/ATSight/backend
source venv/bin/activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

---

## 🎨 Start Frontend Server

**Terminal 2:**
```bash
cd /Users/ashwinasthana/Documents/GitHub/ATSight/frontend
npm run dev
```

**Expected Output:**
```
> next dev
  ▲ Next.js 14.0.0
  - Local:        http://localhost:3000
```

---

## 🧪 Test the API

**Terminal 3:**
```bash
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "Senior Engineer with 6 years Python and FastAPI experience. Led team of 5. Docker and AWS expert.",
    "job_description": "Senior Backend Engineer needed. 5+ years Python/FastAPI. Docker and AWS required. Kubernetes nice to have."
  }'
```

**Expected Response:**
```json
{
  "match_score": 85,
  "matched_skills": ["Python", "Fastapi", "Docker", "Aws"],
  "missing_skills": ["Kubernetes"],
  "experience_feedback": [
    {
      "title": "Years of Experience",
      "feedback": "Experience level matches or exceeds requirement",
      "severity": "low"
    }
  ],
  "formatting_issues": [],
  "overall_recommendation": "Hire"
}
```

---

## 🌐 Test the UI

Open: **http://localhost:3000**

You'll see:
1. Resume input field
2. Job description input field
3. "Analyze Resume" button
4. Results dashboard (after analysis)

---

## 📊 Full Test Flow

1. **Backend running** on http://localhost:8000
2. **Frontend running** on http://localhost:3000
3. **Open browser** to http://localhost:3000
4. **Paste resume** in first field
5. **Paste job description** in second field
6. **Click "Analyze Resume"**
7. **See results** with score, skills, feedback

---

## 🔧 Troubleshooting

### Backend won't start
```bash
cd /Users/ashwinasthana/Documents/GitHub/ATSight/backend
source venv/bin/activate
python -m uvicorn app.main:app --reload
```

### Frontend won't start
```bash
cd /Users/ashwinasthana/Documents/GitHub/ATSight/frontend
npm install
npm run dev
```

### API not responding
- Check backend is running on port 8000
- Check frontend .env.local has: `NEXT_PUBLIC_API_URL=http://localhost:8000`
- Check browser console for CORS errors

---

## 📁 Key Files

- **Backend API**: `backend/app/api/v1/analysis.py`
- **Analysis Logic**: `backend/app/services/llm_service.py`
- **Frontend Page**: `frontend/app/page.tsx`
- **Frontend Form**: `frontend/app/components/AnalysisForm.tsx`
- **Frontend Results**: `frontend/app/components/ResultsDashboard.tsx`

---

## 🎯 What to Test

1. **Analysis Engine**
   - Different resume/job combinations
   - Edge cases (very short text, no matches)
   - Score accuracy

2. **API**
   - POST /api/v1/analyze
   - GET /health
   - Error handling

3. **UI**
   - Form submission
   - Loading states
   - Results display
   - Error messages

---

## 📝 Sample Test Data

### Resume
```
Senior Software Engineer with 6 years of experience in Python, FastAPI, and React.
Led a team of 5 engineers building microservices architecture.
Proficient in Docker, AWS, and PostgreSQL.
Experience with REST APIs, GraphQL, and real-time systems.
```

### Job Description
```
We are hiring a Senior Backend Engineer with 5+ years experience.
Required: Python, FastAPI, Docker, AWS
Nice to have: Kubernetes, GraphQL
Must have strong communication skills and team leadership experience.
```

### Expected Result
- Score: 85
- Recommendation: Hire
- Matched: Python, FastAPI, Docker, AWS
- Missing: Kubernetes

---

## ✨ Next Steps

1. Test the analysis engine
2. Start both servers
3. Test the full UI flow
4. Try different resume/job combinations
5. Check the documentation for more details

---

## 📚 Documentation

- **README.md** - Project overview
- **QUICKSTART.md** - Setup guide
- **API_DOCUMENTATION.md** - API reference
- **ARCHITECTURE.md** - System design

---

**Everything is ready to test! 🚀**
