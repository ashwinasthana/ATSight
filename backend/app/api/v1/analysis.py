from fastapi import APIRouter, HTTPException
import json
from app.schemas.analysis import AnalysisRequest, AnalysisResponse, ExperienceFeedback, FormattingIssue
from app.services.llm_service import llm_service

router = APIRouter(prefix="/api/v1", tags=["analysis"])


@router.post("/analyze")
async def analyze_resume(request: dict):
    """
    Analyze resume against job description.
    Returns structured JSON with match score, skills, and feedback.
    """
    try:
        resume_text = request.get("resume_text", "")
        job_description = request.get("job_description", "")
        
        # Validate
        if len(resume_text) < 50:
            raise ValueError("resume_text must be at least 50 characters")
        if len(job_description) < 50:
            raise ValueError("job_description must be at least 50 characters")
        
        result = llm_service.analyze_resume(resume_text, job_description)
        return result.dict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Analysis failed")
