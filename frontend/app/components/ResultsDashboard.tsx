'use client'

import { Progress } from './ui/progress'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card'
import { Button } from './ui/button'
import type { AnalysisResponse } from '@/lib/api'

interface ResultsDashboardProps {
  result: AnalysisResponse
  onReset: () => void
}

export function ResultsDashboard({ result, onReset }: ResultsDashboardProps) {
  const getScoreColor = (score: number) => {
    if (score >= 80) return 'text-green-600'
    if (score >= 60) return 'text-yellow-600'
    return 'text-red-600'
  }

  const getRecommendationBg = (rec: string) => {
    if (rec === 'Hire') return 'bg-green-50 border-green-200'
    if (rec === 'Consider') return 'bg-yellow-50 border-yellow-200'
    return 'bg-red-50 border-red-200'
  }

  return (
    <div className="space-y-6">
      {/* Score Card */}
      <Card>
        <CardHeader>
          <CardTitle>Overall Match Score</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="flex items-end gap-4">
            <div className={`text-5xl font-bold ${getScoreColor(result.match_score)}`}>
              {result.match_score}%
            </div>
            <div className="flex-1">
              <Progress value={result.match_score} />
            </div>
          </div>
          <div className={`p-4 rounded-lg border ${getRecommendationBg(result.overall_recommendation)}`}>
            <p className="font-semibold">Recommendation: {result.overall_recommendation}</p>
          </div>
        </CardContent>
      </Card>

      {/* Skills Match */}
      <Card>
        <CardHeader>
          <CardTitle className="text-lg">Skills Match</CardTitle>
        </CardHeader>
        <CardContent className="space-y-4">
          <div>
            <h4 className="font-medium text-sm mb-2 text-green-700">Matched Skills</h4>
            <div className="flex flex-wrap gap-2">
              {result.matched_skills.length > 0 ? (
                result.matched_skills.map((skill) => (
                  <span
                    key={skill}
                    className="px-3 py-1 bg-green-100 text-green-800 rounded-full text-sm"
                  >
                    {skill}
                  </span>
                ))
              ) : (
                <p className="text-muted-foreground text-sm">No matched skills</p>
              )}
            </div>
          </div>

          <div>
            <h4 className="font-medium text-sm mb-2 text-red-700">Missing Skills</h4>
            <div className="flex flex-wrap gap-2">
              {result.missing_skills.length > 0 ? (
                result.missing_skills.map((skill) => (
                  <span
                    key={skill}
                    className="px-3 py-1 bg-red-100 text-red-800 rounded-full text-sm"
                  >
                    {skill}
                  </span>
                ))
              ) : (
                <p className="text-muted-foreground text-sm">All key skills present</p>
              )}
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Experience Feedback */}
      {result.experience_feedback.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Experience Feedback</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            {result.experience_feedback.map((item, idx) => (
              <div
                key={idx}
                className="p-3 border border-border rounded-lg bg-muted/30"
              >
                <div className="flex items-start justify-between mb-1">
                  <h5 className="font-medium text-sm">{item.title}</h5>
                  <span className={`text-xs px-2 py-1 rounded ${
                    item.severity === 'high' ? 'bg-red-100 text-red-700' :
                    item.severity === 'medium' ? 'bg-yellow-100 text-yellow-700' :
                    'bg-blue-100 text-blue-700'
                  }`}>
                    {item.severity}
                  </span>
                </div>
                <p className="text-sm text-muted-foreground">{item.feedback}</p>
              </div>
            ))}
          </CardContent>
        </Card>
      )}

      {/* Formatting Issues */}
      {result.formatting_issues.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Formatting Issues</CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            {result.formatting_issues.map((item, idx) => (
              <div key={idx} className="p-3 border border-border rounded-lg bg-muted/30">
                <p className="text-sm font-medium mb-1">{item.issue}</p>
                <p className="text-sm text-muted-foreground">💡 {item.suggestion}</p>
              </div>
            ))}
          </CardContent>
        </Card>
      )}

      <Button onClick={onReset} variant="outline" className="w-full">
        Analyze Another Resume
      </Button>
    </div>
  )
}
