from typing import List


class ExperienceFeedback:
    def __init__(self, title: str, feedback: str, severity: str):
        self.title = title
        self.feedback = feedback
        self.severity = severity
    
    def dict(self):
        return {
            "title": self.title,
            "feedback": self.feedback,
            "severity": self.severity
        }


class FormattingIssue:
    def __init__(self, issue: str, suggestion: str):
        self.issue = issue
        self.suggestion = suggestion
    
    def dict(self):
        return {
            "issue": self.issue,
            "suggestion": self.suggestion
        }


class AnalysisResponse:
    def __init__(
        self,
        match_score: int,
        matched_skills: List[str],
        missing_skills: List[str],
        experience_feedback: List[ExperienceFeedback],
        formatting_issues: List[FormattingIssue],
        overall_recommendation: str
    ):
        self.match_score = match_score
        self.matched_skills = matched_skills
        self.missing_skills = missing_skills
        self.experience_feedback = experience_feedback
        self.formatting_issues = formatting_issues
        self.overall_recommendation = overall_recommendation
    
    def dict(self):
        return {
            "match_score": self.match_score,
            "matched_skills": self.matched_skills,
            "missing_skills": self.missing_skills,
            "experience_feedback": [f.dict() for f in self.experience_feedback],
            "formatting_issues": [f.dict() for f in self.formatting_issues],
            "overall_recommendation": self.overall_recommendation
        }


class AnalysisRequest:
    def __init__(self, resume_text: str, job_description: str):
        if len(resume_text) < 50:
            raise ValueError("resume_text must be at least 50 characters")
        if len(job_description) < 50:
            raise ValueError("job_description must be at least 50 characters")
        self.resume_text = resume_text
        self.job_description = job_description
