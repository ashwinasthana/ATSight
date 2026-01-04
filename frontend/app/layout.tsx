import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'ATSight - AI Resume Analyzer',
  description: 'Optimize your resume for ATS systems with AI-powered analysis',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  )
}
