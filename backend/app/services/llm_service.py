import json
from openai import OpenAI
from app.config import settings
from app.schemas.analysis import AnalysisResponse, ExperienceFeedback, FormattingIssue


class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=settings.openai_api_key)
    
    def analyze_resume(self, resume_text: str, job_description: str) -> AnalysisResponse:
        prompt = f"""You are an expert ATS system and hiring manager. Analyze this resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return ONLY valid JSON (no markdown, no explanation) with this exact structure:
{{
  "match_score": <0-100 integer>,
  "matched_skills": [<list of skills found in resume that match job>],
  "missing_skills": [<list of critical skills missing from resume>],
  "experience_feedback": [
    {{"title": "<feedback category>", "feedback": "<specific feedback>", "severity": "low|medium|high"}}
  ],
  "formatting_issues": [
    {{"issue": "<formatting problem>", "suggestion": "<how to fix>"}}
  ],
  "overall_recommendation": "Hire|Consider|Develop"
}}

Be critical and realistic. A recruiter would agree with your assessment."""

        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=1500
        )
        
        result_text = response.choices[0].message.content.strip()
        
        # Remove markdown code blocks if present
        if result_text.startswith("```"):
            result_text = result_text.split("```")[1]
            if result_text.startswith("json"):
                result_text = result_text[4:]
            result_text = result_text.strip()
        
        data = json.loads(result_text)
        
        # Convert to structured response
        experience_feedback = [
            ExperienceFeedback(**item) for item in data.get("experience_feedback", [])
        ]
        formatting_issues = [
            FormattingIssue(**item) for item in data.get("formatting_issues", [])
        ]
        
        return AnalysisResponse(
            match_score=data["match_score"],
            matched_skills=data["matched_skills"],
            missing_skills=data["missing_skills"],
            experience_feedback=experience_feedback,
            formatting_issues=formatting_issues,
            overall_recommendation=data["overall_recommendation"]
        )


llm_service = LLMService()
