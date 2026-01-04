from fastapi import APIRouter, HTTPException
from app.schemas.analysis import AnalysisRequest, AnalysisResponse
from app.services.llm_service import llm_service

router = APIRouter(prefix="/api/v1", tags=["analysis"])


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_resume(request: AnalysisRequest) -> AnalysisResponse:
    """
    Analyze resume against job description.
    Returns structured JSON with match score, skills, and feedback.
    """
    try:
        result = llm_service.analyze_resume(
            resume_text=request.resume_text,
            job_description=request.job_description
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Analysis failed")
