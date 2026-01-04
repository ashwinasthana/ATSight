# ATSight Scoring Methodology

## Match Score Calculation (0-100)

The match score is calculated by a hiring manager AI that evaluates:

### 1. Skills Match (40%)
- **Exact matches**: +5 points each (max 20)
- **Related skills**: +2 points each (max 10)
- **Missing critical skills**: -10 points each (max -20)
- **Bonus**: +10 for exceeding requirements

**Example**:
- Job requires: Python, FastAPI, React, Docker, AWS
- Resume has: Python, FastAPI, React, Kubernetes, GCP
- Match: 3 exact (15) + 2 related (4) - 1 missing (10) = 9/40

### 2. Experience Level (30%)
- **Years match**: ±5 points based on requirement
- **Relevant roles**: +10 points per relevant position
- **Industry experience**: +5 points if relevant
- **Leadership experience**: +5 bonus if required

**Example**:
- Job requires: 5+ years
- Resume shows: 6 years in relevant roles
- Score: 5 (years match) + 10 (relevant roles) + 5 (industry) = 20/30

### 3. Education & Certifications (15%)
- **Degree match**: +10 points if required
- **Relevant certifications**: +5 points each
- **Self-taught with portfolio**: +8 points

**Example**:
- Job requires: BS in CS
- Resume shows: BS in CS + AWS Certification
- Score: 10 + 5 = 15/15

### 4. Formatting & Presentation (15%)
- **ATS-friendly format**: +10 points
- **Clear structure**: +3 points
- **Quantified achievements**: +2 points
- **Issues**: -1 to -5 per issue

**Example**:
- Clean format: +10
- Good structure: +3
- Some quantified metrics: +1
- Minor formatting issue: -1
- Score: 13/15

## Score Interpretation

| Score | Recommendation | Meaning |
|-------|---|---|
| 90-100 | **Hire** | Exceptional match. Proceed immediately. |
| 80-89 | **Hire** | Strong match. Meets all requirements. |
| 70-79 | **Consider** | Good fit. Minor gaps acceptable. |
| 60-69 | **Consider** | Solid candidate. Needs development. |
| 50-59 | **Develop** | Potential but significant gaps. |
| 0-49 | **Develop** | Poor fit. Not recommended. |

## Realism Checks

The AI applies these filters to ensure recruiter agreement:

### 1. No Inflated Scores
- If resume is generic → max 65
- If missing 3+ critical skills → max 70
- If experience is 50% below requirement → max 60

### 2. No Deflated Scores
- If all skills match exactly → min 75
- If experience exceeds requirement → min 70
- If strong portfolio/projects → +10 bonus

### 3. Industry Context
- Tech roles: Emphasize skills, projects, GitHub
- Finance roles: Emphasize certifications, compliance
- Sales roles: Emphasize metrics, achievements
- HR roles: Emphasize soft skills, culture fit

## Feedback Quality

### Experience Feedback
- **High severity**: Blocks hiring (missing critical skill, insufficient experience)
- **Medium severity**: Concerns (nice-to-have missing, formatting issues)
- **Low severity**: Improvements (minor formatting, could be stronger)

### Formatting Issues
- **Critical**: ATS parsing problems (tables, graphics, special characters)
- **Important**: Readability issues (poor structure, no metrics)
- **Nice-to-have**: Optimization tips (action verbs, keywords)

## Examples

### Example 1: Strong Match (85%)
```
Resume: Senior Python Engineer, 6 years, FastAPI, React, Docker, AWS
Job: Senior Engineer, 5+ years, Python, FastAPI, React, Docker, AWS

Skills: 40/40 (all match)
Experience: 28/30 (exceeds requirement)
Education: 12/15 (relevant degree)
Formatting: 14/15 (clean, quantified)
Total: 94/100 → Hire
```

### Example 2: Good Fit (72%)
```
Resume: Mid-level Python Dev, 3 years, Python, Django, React
Job: Senior Engineer, 5+ years, Python, FastAPI, React, Docker, AWS

Skills: 25/40 (missing Docker, AWS, FastAPI)
Experience: 18/30 (2 years short)
Education: 12/15 (relevant degree)
Formatting: 12/15 (good structure)
Total: 67/100 → Consider
```

### Example 3: Poor Fit (45%)
```
Resume: Junior Frontend Dev, 1 year, React, JavaScript
Job: Senior Backend Engineer, 5+ years, Python, FastAPI, Docker, AWS

Skills: 10/40 (only React relevant)
Experience: 5/30 (4 years short, wrong focus)
Education: 8/15 (no relevant degree)
Formatting: 10/15 (decent but junior-level)
Total: 33/100 → Develop
```

## Recruiter Validation

This methodology is designed to align with real hiring decisions:

✅ **Recruiters agree** when:
- Score 80+ → Candidate is genuinely strong
- Score 60-79 → Candidate has potential but gaps
- Score <60 → Candidate needs significant development

❌ **Recruiters disagree** when:
- Score is inflated (90+ for mediocre resume)
- Score ignores critical skills
- Score doesn't account for industry context
- Score is too harsh on career changers

## Continuous Improvement

Monitor these metrics:
- Recruiter feedback on scores
- Hire rate for 80+ scored candidates
- Rejection rate for <60 scored candidates
- Time-to-hire correlation with score
