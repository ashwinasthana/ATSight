#!/usr/bin/env python3
"""
ATSight - Quick Test Demo
Tests the analysis engine without needing full server setup
"""

import json
import sys
sys.path.insert(0, '/Users/ashwinasthana/Documents/GitHub/ATSight/backend')

from app.services.llm_service import llm_service
from app.schemas.analysis import AnalysisResponse, ExperienceFeedback, FormattingIssue

print("╔════════════════════════════════════════════════════════════════╗")
print("║           🚀 ATSight - Analysis Engine Test                   ║")
print("╚════════════════════════════════════════════════════════════════╝")
print()

# Test data
resume = """
Senior Software Engineer with 6 years of experience in Python, FastAPI, and React.
Led a team of 5 engineers building microservices architecture.
Proficient in Docker, AWS, and PostgreSQL.
Experience with REST APIs, GraphQL, and real-time systems.
"""

job_description = """
We are hiring a Senior Backend Engineer with 5+ years experience.
Required: Python, FastAPI, Docker, AWS
Nice to have: Kubernetes, GraphQL
Must have strong communication skills and team leadership experience.
"""

print("📋 Test Input:")
print(f"Resume: {resume[:100]}...")
print(f"Job Description: {job_description[:100]}...")
print()

try:
    print("🔄 Analyzing...")
    result = llm_service.analyze_resume(resume, job_description)
    
    print("✅ Analysis Complete!")
    print()
    print("📊 Results:")
    print(json.dumps(result.dict(), indent=2))
    print()
    print("✨ Success! The analysis engine is working correctly.")
    
except Exception as e:
    print(f"❌ Error: {str(e)}")
    print()
    print("Note: This requires a valid OPENAI_API_KEY in .env")
    print("For demo purposes, here's what the response would look like:")
    print()
    
    demo_response = {
        "match_score": 85,
        "matched_skills": ["Python", "FastAPI", "Docker", "AWS"],
        "missing_skills": ["Kubernetes"],
        "experience_feedback": [
            {
                "title": "Years of Experience",
                "feedback": "6 years exceeds the 5+ year requirement",
                "severity": "low"
            },
            {
                "title": "Team Leadership",
                "feedback": "Led team of 5 engineers - strong leadership experience",
                "severity": "low"
            }
        ],
        "formatting_issues": [
            {
                "issue": "Could add more quantified metrics",
                "suggestion": "Include specific project outcomes and metrics"
            }
        ],
        "overall_recommendation": "Hire"
    }
    
    print("📊 Demo Response:")
    print(json.dumps(demo_response, indent=2))
