import axios from 'axios'

const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

export const api = axios.create({
  baseURL: API_BASE,
})

export interface AnalysisRequest {
  resume_text: string
  job_description: string
}

export interface ExperienceFeedback {
  title: string
  feedback: string
  severity: 'low' | 'medium' | 'high'
}

export interface FormattingIssue {
  issue: string
  suggestion: string
}

export interface AnalysisResponse {
  match_score: number
  matched_skills: string[]
  missing_skills: string[]
  experience_feedback: ExperienceFeedback[]
  formatting_issues: FormattingIssue[]
  overall_recommendation: 'Hire' | 'Consider' | 'Develop'
}

export async function analyzeResume(
  resumeText: string,
  jobDescription: string
): Promise<AnalysisResponse> {
  const response = await api.post<AnalysisResponse>('/api/v1/analyze', {
    resume_text: resumeText,
    job_description: jobDescription,
  })
  return response.data
}
