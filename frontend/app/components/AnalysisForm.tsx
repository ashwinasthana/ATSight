'use client'

import { useState } from 'react'
import { Button } from './ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card'
import { analyzeResume, type AnalysisResponse } from '@/lib/api'

interface AnalysisFormProps {
  onAnalysisComplete: (result: AnalysisResponse) => void
}

export function AnalysisForm({ onAnalysisComplete }: AnalysisFormProps) {
  const [resumeText, setResumeText] = useState('')
  const [jobDescription, setJobDescription] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError('')
    setLoading(true)

    try {
      const result = await analyzeResume(resumeText, jobDescription)
      onAnalysisComplete(result)
    } catch (err) {
      setError('Failed to analyze resume. Please try again.')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle>Analyze Your Resume</CardTitle>
        <CardDescription>
          Paste your resume and job description to get instant feedback
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div>
            <label className="block text-sm font-medium mb-2">Resume</label>
            <textarea
              value={resumeText}
              onChange={(e) => setResumeText(e.target.value)}
              placeholder="Paste your resume text here..."
              className="w-full h-32 p-3 border border-input rounded-md bg-background text-foreground placeholder-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">Job Description</label>
            <textarea
              value={jobDescription}
              onChange={(e) => setJobDescription(e.target.value)}
              placeholder="Paste the job description here..."
              className="w-full h-32 p-3 border border-input rounded-md bg-background text-foreground placeholder-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary"
              required
            />
          </div>

          {error && (
            <div className="p-3 bg-destructive/10 text-destructive rounded-md text-sm">
              {error}
            </div>
          )}

          <Button
            type="submit"
            disabled={loading || !resumeText.trim() || !jobDescription.trim()}
            className="w-full"
          >
            {loading ? 'Analyzing...' : 'Analyze Resume'}
          </Button>
        </form>
      </CardContent>
    </Card>
  )
}
