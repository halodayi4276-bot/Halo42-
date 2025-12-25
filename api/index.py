"""
Vercel serverless function entry point for the FastHTML application.
This allows the app to run on Vercel's serverless platform.
"""

from app import app

# For Vercel serverless
handler = app
