'use client'

import { useState } from 'react'
import { AnalysisForm } from './components/AnalysisForm'
import { ResultsDashboard } from './components/ResultsDashboard'
import type { AnalysisResponse } from '@/lib/api'

export default function Home() {
  const [result, setResult] = useState<AnalysisResponse | null>(null)

  const handleReset = () => {
    setResult(null)
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100">
      <div className="max-w-4xl mx-auto px-4 py-12">
        {/* Header */}
        <div className="mb-12 text-center">
          <h1 className="text-4xl font-bold tracking-tight mb-2">ATSight</h1>
          <p className="text-lg text-muted-foreground">
            AI-powered resume analysis for ATS optimization
          </p>
        </div>

        {/* Content */}
        {result ? (
          <ResultsDashboard result={result} onReset={handleReset} />
        ) : (
          <AnalysisForm onAnalysisComplete={setResult} />
        )}
      </div>
    </main>
  )
}
