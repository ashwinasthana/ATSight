from pydantic import BaseModel, Field
from typing import List


class SkillMatch(BaseModel):
    matched_skills: List[str] = Field(..., description="Skills found in resume matching job description")
    missing_skills: List[str] = Field(..., description="Important skills missing from resume")


class ExperienceFeedback(BaseModel):
    title: str
    feedback: str
    severity: str = Field(..., description="low|medium|high")


class FormattingIssue(BaseModel):
    issue: str
    suggestion: str


class AnalysisResponse(BaseModel):
    match_score: int = Field(..., ge=0, le=100, description="Overall match score 0-100")
    matched_skills: List[str]
    missing_skills: List[str]
    experience_feedback: List[ExperienceFeedback]
    formatting_issues: List[FormattingIssue]
    overall_recommendation: str = Field(..., description="Hire|Consider|Develop")


class AnalysisRequest(BaseModel):
    resume_text: str = Field(..., min_length=50, description="Extracted resume text")
    job_description: str = Field(..., min_length=50, description="Job description to match against")
