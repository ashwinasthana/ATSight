# ATSight - Architecture & Data Flow

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                          USER BROWSER                               │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │                    Next.js Frontend                          │  │
│  │                                                              │  │
│  │  ┌─────────────────────────────────────────────────────┐   │  │
│  │  │  Page: /                                            │   │  │
│  │  │  ┌──────────────────────────────────────────────┐  │   │  │
│  │  │  │  AnalysisForm Component                      │  │   │  │
│  │  │  │  - Resume textarea                           │  │   │  │
│  │  │  │  - Job description textarea                  │  │   │  │
│  │  │  │  - Submit button                             │  │   │  │
│  │  │  └──────────────────────────────────────────────┘  │   │  │
│  │  │                                                     │   │  │
│  │  │  ┌──────────────────────────────────────────────┐  │   │  │
│  │  │  │  ResultsDashboard Component                  │  │   │  │
│  │  │  │  - Score card with progress bar             │  │   │  │
│  │  │  │  - Matched skills (green tags)              │  │   │  │
│  │  │  │  - Missing skills (red tags)                │  │   │  │
│  │  │  │  - Experience feedback cards                │  │   │  │
│  │  │  │  - Formatting issues                        │  │   │  │
│  │  │  └──────────────────────────────────────────────┘  │   │  │
│  │  └─────────────────────────────────────────────────────┘   │  │
│  │                                                              │  │
│  │  ┌─────────────────────────────────────────────────────┐   │  │
│  │  │  API Client (lib/api.ts)                           │   │  │
│  │  │  - Axios instance                                  │   │  │
│  │  │  - analyzeResume() function                        │   │  │
│  │  └─────────────────────────────────────────────────────┘   │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              ↓ HTTP POST
                    /api/v1/analyze (JSON)
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                      FastAPI Backend                                │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  API Router (app/api/v1/router.py)                          │  │
│  │  ├── POST /api/v1/analyze                                   │  │
│  │  └── GET /health                                            │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                              ↓                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  Analysis Endpoint (app/api/v1/analysis.py)                 │  │
│  │  ├── Validate input (Pydantic)                              │  │
│  │  ├── Call LLM service                                       │  │
│  │  └── Return structured response                            │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                              ↓                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  LLM Service (app/services/llm_service.py)                  │  │
│  │  ├── Create analysis prompt                                 │  │
│  │  ├── Call OpenAI GPT-4 API                                  │  │
│  │  ├── Parse JSON response                                    │  │
│  │  └── Return AnalysisResponse object                         │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                              ↓                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  Pydantic Schemas (app/schemas/analysis.py)                 │  │
│  │  ├── AnalysisRequest                                        │  │
│  │  ├── AnalysisResponse                                       │  │
│  │  ├── ExperienceFeedback                                     │  │
│  │  └── FormattingIssue                                        │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              ↓ HTTP Response
                    JSON (AnalysisResponse)
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    Frontend (Display Results)                       │
│  - Update ResultsDashboard with response data                       │
│  - Display score, skills, feedback                                  │
│  - Show recommendations                                             │
└─────────────────────────────────────────────────────────────────────┘
```

## Data Flow Diagram

```
USER INPUT
    ↓
┌─────────────────────────────────────────┐
│  Resume Text                            │
│  Job Description                        │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Frontend Validation                    │
│  - Min 50 characters                    │
│  - Not empty                            │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  API Request (Axios)                    │
│  POST /api/v1/analyze                   │
│  {                                      │
│    "resume_text": "...",                │
│    "job_description": "..."             │
│  }                                      │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Backend Validation (Pydantic)          │
│  - Validate schema                      │
│  - Check constraints                    │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  LLM Analysis                           │
│  - Create prompt                        │
│  - Call OpenAI GPT-4                    │
│  - Parse response                       │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Structured Response                    │
│  {                                      │
│    "match_score": 85,                   │
│    "matched_skills": [...],             │
│    "missing_skills": [...],             │
│    "experience_feedback": [...],        │
│    "formatting_issues": [...],          │
│    "overall_recommendation": "Hire"     │
│  }                                      │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Frontend Display                       │
│  - Score card                           │
│  - Skills tags                          │
│  - Feedback cards                       │
│  - Recommendation badge                 │
└─────────────────────────────────────────┘
    ↓
USER SEES RESULTS
```

## Component Hierarchy

```
App (page.tsx)
├── State: result (AnalysisResponse | null)
├── Handlers: handleReset()
│
├── Conditional Render:
│   ├── IF result === null:
│   │   └── AnalysisForm
│   │       ├── State: resumeText, jobDescription, loading, error
│   │       ├── Props: onAnalysisComplete
│   │       ├── Handlers: handleSubmit()
│   │       └── Components:
│   │           ├── Card
│   │           ├── CardHeader
│   │           ├── CardTitle
│   │           ├── CardDescription
│   │           ├── CardContent
│   │           ├── textarea (resume)
│   │           ├── textarea (job description)
│   │           ├── Button (submit)
│   │           └── Error display
│   │
│   └── IF result !== null:
│       └── ResultsDashboard
│           ├── Props: result, onReset
│           ├── Helpers: getScoreColor(), getRecommendationBg()
│           └── Components:
│               ├── Card (Score)
│               │   ├── CardHeader
│               │   ├── CardTitle
│               │   ├── CardContent
│               │   ├── Score display (large)
│               │   ├── Progress bar
│               │   └── Recommendation badge
│               │
│               ├── Card (Skills)
│               │   ├── CardHeader
│               │   ├── CardTitle
│               │   ├── CardContent
│               │   ├── Matched skills (green tags)
│               │   └── Missing skills (red tags)
│               │
│               ├── Card (Experience Feedback)
│               │   ├── CardHeader
│               │   ├── CardTitle
│               │   ├── CardContent
│               │   └── Feedback items (with severity)
│               │
│               ├── Card (Formatting Issues)
│               │   ├── CardHeader
│               │   ├── CardTitle
│               │   ├── CardContent
│               │   └── Issue items (with suggestions)
│               │
│               └── Button (Analyze Another)
```

## Request/Response Flow

```
FRONTEND                          BACKEND
   │                                 │
   │  POST /api/v1/analyze           │
   │  {                              │
   │    "resume_text": "...",        │
   │    "job_description": "..."     │
   │  }                              │
   ├────────────────────────────────>│
   │                                 │
   │                          Validate Input
   │                          (Pydantic)
   │                                 │
   │                          Create Prompt
   │                                 │
   │                          Call OpenAI
   │                          (GPT-4)
   │                                 │
   │                          Parse Response
   │                                 │
   │                          Build AnalysisResponse
   │                                 │
   │  200 OK                         │
   │  {                              │
   │    "match_score": 85,           │
   │    "matched_skills": [...],     │
   │    "missing_skills": [...],     │
   │    "experience_feedback": [...],│
   │    "formatting_issues": [...],  │
   │    "overall_recommendation": "Hire"
   │  }                              │
   │<────────────────────────────────┤
   │                                 │
   Display Results                   │
   │                                 │
```

## Error Handling Flow

```
USER INPUT
    ↓
┌─────────────────────────────────────────┐
│  Frontend Validation                    │
│  ├── Empty check                        │
│  ├── Min length check (50 chars)        │
│  └── Show error if invalid              │
└─────────────────────────────────────────┘
    ↓ (if valid)
┌─────────────────────────────────────────┐
│  API Request                            │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Backend Validation (Pydantic)          │
│  ├── Schema validation                  │
│  ├── Constraint checking                │
│  └── Return 400 if invalid              │
└─────────────────────────────────────────┘
    ↓ (if valid)
┌─────────────────────────────────────────┐
│  LLM Analysis                           │
│  ├── Try OpenAI API call                │
│  ├── Catch exceptions                   │
│  └── Return 500 if fails                │
└─────────────────────────────────────────┘
    ↓ (if success)
┌─────────────────────────────────────────┐
│  Return Results                         │
│  200 OK with AnalysisResponse           │
└─────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────┐
│  Frontend Error Handling                │
│  ├── Catch API errors                   │
│  ├── Display error message              │
│  └── Allow retry                        │
└─────────────────────────────────────────┘
```

## Deployment Architecture (Production)

```
┌─────────────────────────────────────────────────────────────┐
│                    CDN (CloudFront)                         │
│                  Static Assets Cache                        │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│                  Frontend (Vercel/Amplify)                  │
│              Next.js App (Serverless)                       │
│              - Auto-scaling                                 │
│              - Global distribution                          │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              Load Balancer (ALB/NLB)                        │
│              - Route traffic                                │
│              - SSL termination                              │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│         Backend (ECS Fargate / Kubernetes)                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  FastAPI Container (Multiple Instances)             │  │
│  │  - Auto-scaling based on CPU/memory                 │  │
│  │  - Health checks                                    │  │
│  │  - Logging to CloudWatch                            │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              Database (RDS PostgreSQL)                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Primary Instance                                   │  │
│  │  - Multi-AZ deployment                              │  │
│  │  - Automated backups                                │  │
│  │  - Read replicas                                    │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              External Services                              │
│  ├── OpenAI API (GPT-4)                                    │
│  ├── Sentry (Error tracking)                               │
│  ├── CloudWatch (Monitoring)                               │
│  └── Stripe (Payments - future)                            │
└─────────────────────────────────────────────────────────────┘
```

## Database Schema (Future)

```
┌─────────────────────────────────────────┐
│  users                                  │
├─────────────────────────────────────────┤
│ id (UUID, PK)                           │
│ email (VARCHAR, UNIQUE)                 │
│ password_hash (VARCHAR)                 │
│ subscription_tier (VARCHAR)             │
│ created_at (TIMESTAMP)                  │
│ updated_at (TIMESTAMP)                  │
└─────────────────────────────────────────┘
           ↓ (1:N)
┌─────────────────────────────────────────┐
│  resumes                                │
├─────────────────────────────────────────┤
│ id (UUID, PK)                           │
│ user_id (UUID, FK)                      │
│ filename (VARCHAR)                      │
│ extracted_text (TEXT)                   │
│ created_at (TIMESTAMP)                  │
└─────────────────────────────────────────┘
           ↓ (1:N)
┌─────────────────────────────────────────┐
│  analyses                               │
├─────────────────────────────────────────┤
│ id (UUID, PK)                           │
│ user_id (UUID, FK)                      │
│ resume_id (UUID, FK)                    │
│ job_description (TEXT)                  │
│ match_score (INTEGER)                   │
│ results_json (JSONB)                    │
│ created_at (TIMESTAMP)                  │
└─────────────────────────────────────────┘
```

---

This architecture is:
- ✅ Scalable (horizontal scaling)
- ✅ Reliable (multi-AZ, backups)
- ✅ Performant (CDN, caching)
- ✅ Secure (SSL, firewalls)
- ✅ Monitorable (logging, metrics)
- ✅ Cost-effective (auto-scaling)
