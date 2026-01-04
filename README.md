# ATSight - AI Resume Analyzer

Production-ready SaaS for AI-powered resume analysis and ATS optimization.

## Tech Stack

- **Frontend**: Next.js 14 + TypeScript + Tailwind CSS + shadcn/ui
- **Backend**: FastAPI + Python + OpenAI API
- **Database**: PostgreSQL (ready for integration)

## Project Structure

```
ATSight/
├── backend/
│   ├── app/
│   │   ├── api/v1/
│   │   │   ├── analysis.py      # Analysis endpoints
│   │   │   └── router.py        # Route aggregation
│   │   ├── schemas/
│   │   │   └── analysis.py      # Request/response models
│   │   ├── services/
│   │   │   ├── llm_service.py   # OpenAI integration
│   │   │   └── resume_service.py # PDF extraction
│   │   ├── config.py            # Settings
│   │   └── main.py              # FastAPI app
│   ├── requirements.txt
│   └── .env.example
│
└── frontend/
    ├── app/
    │   ├── components/
    │   │   ├── AnalysisForm.tsx
    │   │   └── ResultsDashboard.tsx
    │   ├── components/ui/
    │   │   ├── button.tsx
    │   │   ├── card.tsx
    │   │   └── progress.tsx
    │   ├── page.tsx
    │   ├── layout.tsx
    │   └── globals.css
    ├── lib/
    │   ├── api.ts
    │   └── utils.ts
    ├── package.json
    └── .env.example
```

## Setup

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Add your OPENAI_API_KEY and DATABASE_URL

# Run server
python -m uvicorn app.main:app --reload
```

Server runs on `http://localhost:8000`

### Frontend

```bash
cd frontend
npm install

# Create .env.local
cp .env.example .env.local

# Run dev server
npm run dev
```

App runs on `http://localhost:3000`

## API Endpoints

### POST /api/v1/analyze

Analyze resume against job description.

**Request:**
```json
{
  "resume_text": "string (min 50 chars)",
  "job_description": "string (min 50 chars)"
}
```

**Response:**
```json
{
  "match_score": 85,
  "matched_skills": ["Python", "FastAPI", "React"],
  "missing_skills": ["Kubernetes", "Docker"],
  "experience_feedback": [
    {
      "title": "Years of Experience",
      "feedback": "5 years matches job requirement",
      "severity": "low"
    }
  ],
  "formatting_issues": [
    {
      "issue": "Missing action verbs",
      "suggestion": "Start bullet points with strong action verbs"
    }
  ],
  "overall_recommendation": "Hire"
}
```

## Features

- ✅ Structured JSON responses (no raw AI text)
- ✅ Match score (0-100) with realistic assessment
- ✅ Skills matching (matched + missing)
- ✅ Experience feedback with severity levels
- ✅ Formatting issue detection
- ✅ Premium SaaS UI with clean spacing
- ✅ Real-time analysis
- ✅ Production-ready error handling

## Environment Variables

### Backend (.env)
```
OPENAI_API_KEY=sk-...
DATABASE_URL=postgresql://user:password@localhost/atsight
JWT_SECRET=your_secret_key
JWT_ALGORITHM=HS256
ENVIRONMENT=development
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Monetization Ready

- User authentication structure (JWT ready)
- Database models for tracking usage
- Tier-based rate limiting support
- Analysis history tracking
- Cost tracking for LLM API calls

## Next Steps

1. Add user authentication (JWT)
2. Implement database models (SQLAlchemy)
3. Add resume file upload (PDF/DOCX parsing)
4. Implement subscription tiers
5. Add rewrite suggestions endpoint
6. Deploy to production (Docker + AWS)

## Development

- Backend: `cd backend && python -m uvicorn app.main:app --reload`
- Frontend: `cd frontend && npm run dev`
- Both run simultaneously for full-stack development

## Production Deployment

See `Dockerfile` and deployment guides in respective directories.
