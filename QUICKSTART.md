# Quick Start Guide

## 1. Clone & Setup

```bash
cd ATSight
```

## 2. Backend Setup (5 minutes)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create .env
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## 3. Frontend Setup (5 minutes)

```bash
cd frontend
npm install

# Create .env.local
cp .env.example .env.local
```

## 4. Run Both Services

**Terminal 1 - Backend:**
```bash
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --reload
# Runs on http://localhost:8000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
# Runs on http://localhost:3000
```

## 5. Test the API

Open http://localhost:3000 and:
1. Paste a resume
2. Paste a job description
3. Click "Analyze Resume"

## API Testing with cURL

```bash
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "Senior Software Engineer with 5 years experience in Python, FastAPI, React...",
    "job_description": "We are looking for a Senior Engineer with Python and FastAPI experience..."
  }'
```

## Production Deployment

### Using Docker Compose

```bash
docker-compose up -d
```

### Manual Deployment

**Backend (AWS EC2/ECS):**
```bash
docker build -t atsight-backend ./backend
docker run -p 8000:8000 -e OPENAI_API_KEY=sk-... atsight-backend
```

**Frontend (Vercel/AWS Amplify):**
```bash
npm run build
npm start
```

## Troubleshooting

**Backend won't start:**
- Check OPENAI_API_KEY is set
- Verify Python 3.11+
- Run `pip install -r requirements.txt` again

**Frontend won't connect to backend:**
- Ensure backend is running on port 8000
- Check NEXT_PUBLIC_API_URL in .env.local
- Check browser console for CORS errors

**Analysis fails:**
- Verify OpenAI API key is valid
- Check resume_text and job_description are > 50 chars
- Check OpenAI API quota

## Next Features to Build

1. **User Authentication** - JWT + database
2. **Resume Upload** - PDF/DOCX parsing
3. **Analysis History** - Save past analyses
4. **Rewrite Suggestions** - AI-powered improvements
5. **Subscription Tiers** - Monetization
6. **Email Notifications** - Analysis results
