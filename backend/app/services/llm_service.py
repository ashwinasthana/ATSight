import json
from app.schemas.analysis import AnalysisResponse, ExperienceFeedback, FormattingIssue


class LLMService:
    def __init__(self):
        pass
    
    def analyze_resume(self, resume_text: str, job_description: str) -> AnalysisResponse:
        """Mock analysis for testing"""
        
        # Simple keyword matching for demo
        resume_lower = resume_text.lower()
        job_lower = job_description.lower()
        
        # Extract skills mentioned
        all_skills = [
            "python", "fastapi", "react", "docker", "aws", "kubernetes",
            "postgresql", "graphql", "rest", "microservices", "leadership",
            "typescript", "javascript", "nodejs", "java", "golang"
        ]
        
        matched = [s.title() for s in all_skills if s in resume_lower and s in job_lower]
        missing = [s.title() for s in all_skills if s in job_lower and s not in resume_lower]
        
        # Calculate score
        score = 70
        if len(matched) >= 3:
            score += 10
        if "leadership" in resume_lower or "led" in resume_lower:
            score += 5
        if len(missing) > 2:
            score -= 10
        
        score = min(100, max(0, score))
        
        # Create feedback
        feedback = []
        if "6 years" in resume_text or "5 years" in resume_text:
            feedback.append(ExperienceFeedback(
                "Years of Experience",
                "Experience level matches or exceeds requirement",
                "low"
            ))
        
        if "led" in resume_lower or "leadership" in resume_lower:
            feedback.append(ExperienceFeedback(
                "Leadership Experience",
                "Strong leadership background demonstrated",
                "low"
            ))
        
        # Formatting issues
        formatting = []
        if len(resume_text.split('\n')) < 5:
            formatting.append(FormattingIssue(
                "Brief resume",
                "Consider adding more details and achievements"
            ))
        
        # Recommendation
        if score >= 80:
            rec = "Hire"
        elif score >= 60:
            rec = "Consider"
        else:
            rec = "Develop"
        
        return AnalysisResponse(
            match_score=score,
            matched_skills=matched[:5],
            missing_skills=missing[:3],
            experience_feedback=feedback,
            formatting_issues=formatting,
            overall_recommendation=rec
        )


llm_service = LLMService()
