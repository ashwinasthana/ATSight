# ATSight API Documentation

## Base URL

```
http://localhost:8000  (development)
https://api.atsight.com (production)
```

## Authentication

Currently no authentication required. JWT will be added for user-specific endpoints.

## Endpoints

### POST /api/v1/analyze

Analyze a resume against a job description and return structured feedback.

#### Request

```http
POST /api/v1/analyze HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
  "resume_text": "string",
  "job_description": "string"
}
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| resume_text | string | Yes | Extracted resume text (min 50 chars) |
| job_description | string | Yes | Job description (min 50 chars) |

#### Response (200 OK)

```json
{
  "match_score": 85,
  "matched_skills": [
    "Python",
    "FastAPI",
    "React",
    "Docker"
  ],
  "missing_skills": [
    "Kubernetes",
    "AWS"
  ],
  "experience_feedback": [
    {
      "title": "Years of Experience",
      "feedback": "6 years matches job requirement of 5+ years",
      "severity": "low"
    },
    {
      "title": "Relevant Experience",
      "feedback": "Strong background in backend development",
      "severity": "low"
    }
  ],
  "formatting_issues": [
    {
      "issue": "Missing action verbs in bullet points",
      "suggestion": "Start each bullet with strong action verbs like 'Developed', 'Implemented', 'Led'"
    }
  ],
  "overall_recommendation": "Hire"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| match_score | integer (0-100) | Overall match percentage |
| matched_skills | array[string] | Skills found in resume matching job |
| missing_skills | array[string] | Important skills missing from resume |
| experience_feedback | array[object] | Detailed feedback on experience |
| formatting_issues | array[object] | Resume formatting problems |
| overall_recommendation | string | "Hire" \| "Consider" \| "Develop" |

#### Experience Feedback Object

| Field | Type | Description |
|-------|------|-------------|
| title | string | Category of feedback |
| feedback | string | Specific feedback message |
| severity | string | "low" \| "medium" \| "high" |

#### Formatting Issue Object

| Field | Type | Description |
|-------|------|-------------|
| issue | string | Description of the issue |
| suggestion | string | How to fix the issue |

#### Error Responses

**400 Bad Request**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "resume_text must be at least 50 characters",
    "details": {
      "field": "resume_text",
      "min_length": 50,
      "received": 30
    }
  },
  "request_id": "req_123abc",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

**500 Internal Server Error**
```json
{
  "error": {
    "code": "ANALYSIS_FAILED",
    "message": "Failed to analyze resume"
  },
  "request_id": "req_123abc",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### Example Requests

**cURL**
```bash
curl -X POST http://localhost:8000/api/v1/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "resume_text": "Senior Software Engineer with 6 years experience in Python, FastAPI, React, and Docker. Led team of 5 engineers. Implemented microservices architecture.",
    "job_description": "We are hiring a Senior Backend Engineer with 5+ years experience in Python and FastAPI. Must have experience with Docker and cloud deployment."
  }'
```

**Python**
```python
import requests

response = requests.post(
    'http://localhost:8000/api/v1/analyze',
    json={
        'resume_text': 'Senior Software Engineer...',
        'job_description': 'We are hiring...'
    }
)

result = response.json()
print(f"Match Score: {result['match_score']}")
print(f"Recommendation: {result['overall_recommendation']}")
```

**JavaScript/TypeScript**
```typescript
const response = await fetch('http://localhost:8000/api/v1/analyze', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    resume_text: 'Senior Software Engineer...',
    job_description: 'We are hiring...'
  })
})

const result = await response.json()
console.log(`Match Score: ${result.match_score}`)
console.log(`Recommendation: ${result.overall_recommendation}`)
```

### GET /health

Health check endpoint.

#### Response (200 OK)
```json
{
  "status": "ok"
}
```

## Rate Limiting

Currently unlimited. Will be implemented per subscription tier:

- **Free**: 1 analysis/month
- **Pro**: 100 analyses/month
- **Enterprise**: Unlimited

## Error Codes

| Code | Status | Description |
|------|--------|-------------|
| VALIDATION_ERROR | 400 | Invalid request parameters |
| INVALID_FILE_FORMAT | 400 | Unsupported file type |
| ANALYSIS_FAILED | 500 | LLM analysis failed |
| RATE_LIMIT_EXCEEDED | 429 | Too many requests |
| UNAUTHORIZED | 401 | Missing/invalid authentication |
| INTERNAL_ERROR | 500 | Server error |

## Response Headers

```
Content-Type: application/json
X-Request-ID: req_123abc
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 1705315800
```

## Versioning

API uses URL versioning: `/api/v1/`

Future versions: `/api/v2/`, `/api/v3/`, etc.

## CORS

Allowed origins (development):
- http://localhost:3000
- http://localhost:3001

Production: Configure in environment variables.

## Webhooks (Future)

```
POST /webhooks/analysis-complete
```

Notify external systems when analysis completes.

## Pagination (Future)

```
GET /api/v1/analysis/history?page=1&limit=20
```

## Filtering (Future)

```
GET /api/v1/analysis/history?score_min=80&score_max=100&recommendation=Hire
```

## Changelog

### v1.0.0 (Current)
- POST /api/v1/analyze
- GET /health

### v1.1.0 (Planned)
- User authentication
- Analysis history
- Resume upload
- Rewrite suggestions

### v2.0.0 (Planned)
- Batch analysis
- Custom scoring rules
- Webhooks
- Advanced filtering
