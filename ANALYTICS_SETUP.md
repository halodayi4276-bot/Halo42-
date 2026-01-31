# Vercel Web Analytics Integration - Halo42 FastHTML App

This document explains how Vercel Web Analytics is integrated into this FastHTML application.

## Overview

Vercel Web Analytics provides privacy-focused, first-party analytics for your applications. This FastHTML app includes automatic analytics tracking that works when deployed to Vercel.

## How It's Implemented

### HTML Script Injection

The analytics script is injected into all HTML pages through the `analytics_script()` function in `app.py`:

```python
def analytics_script():
    return Script(
        """
        window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
        """,
        src="/_vercel/insights/script.js",
        defer=True
    )
```

This script:
1. Creates a placeholder function if it doesn't exist
2. Loads the actual analytics script from Vercel (`/_vercel/insights/script.js`)
3. Defers loading to avoid blocking page rendering

### Integration Points

The `analytics_script()` is included in both route handlers:
- `/` (index page)
- `/about` (example secondary page)

This ensures analytics tracking across all pages of the application.

## Setup Instructions

### 1. Enable Analytics on Vercel Dashboard

1. Go to your [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project
3. Click the **Analytics** tab
4. Click **Enable** to activate Web Analytics
5. The `/_vercel/insights/*` routes will be added after your next deployment

### 2. Deploy to Vercel

```bash
# Install Vercel CLI (if not already installed)
pip install vercel

# Deploy your application
vercel deploy

# For production deployment
vercel deploy --prod
```

### 3. Verify Analytics Collection

After deployment:

1. Visit your deployed application
2. Open browser Developer Tools (F12)
3. Go to the Network tab
4. Look for requests to `/_vercel/insights/view` - these are analytics pings
5. Interact with your site (click links, navigate pages, etc.)

### 4. View Your Data

1. Go to your Vercel Dashboard
2. Select your project
3. Click the **Analytics** tab
4. After a few minutes of traffic, you'll see data appear

## What Gets Tracked

### Automatically Tracked
- **Page Views**: Each page visit
- **Core Web Vitals**: LCP, FID, CLS
- **Navigation Timing**: Page load performance
- **User Location**: Anonymized geographic data
- **Referrer Information**: Where users came from

### Privacy & Compliance
- No cookies used by default
- GDPR compliant
- CCPA compliant
- First-party analytics (data goes to your Vercel account)
- Fully anonymized

## Advanced Usage

### Custom Events (Framework-Dependent)

For frameworks like Next.js, Remix, etc., you can use `@vercel/analytics` package for custom event tracking:

```javascript
import { trackEvent } from '@@vercel/analytics';

trackEvent('button_click', {
  category: 'engagement',
  label: 'signup-button',
  value: 1,
});
```

FastHTML with plain HTML implementation doesn't support custom events through this package, but you can implement custom event tracking using the `window.va()` function:

```javascript
window.va('event', {
  type: 'custom_event',
  event: 'purchase',
  value: 99.99,
});
```

## Troubleshooting

### Analytics Not Appearing
1. Ensure Web Analytics is enabled in Vercel dashboard
2. Make sure you're deployed to Vercel (not local development)
3. Check Network tab for `/_vercel/insights/view` requests
4. Wait 5-15 minutes for initial data to appear in dashboard

### Script Not Loading
1. Check browser console for errors
2. Verify `/_vercel/insights/script.js` loads successfully
3. Ensure your Vercel deployment completed successfully

### No Data Showing
1. Wait 5-15 minutes after deployment
2. Make sure you're generating traffic to your site
3. Check if Web Analytics is enabled (it shows "Enabled" in dashboard)

## Architecture

```
┌─────────────┐
│  FastHTML   │
│   App       │
└──────┬──────┘
       │
       ├─ Route: / (returns HTML with analytics)
       ├─ Route: /about (returns HTML with analytics)
       │
       └─ analytics_script() function
          │
          └─ Injects <script> tags into pages
             │
             └─ Loads /_vercel/insights/script.js from Vercel
                │
                └─ Sends analytics data to Vercel
```

## Files Modified/Created

- `app.py`: Main FastHTML application with analytics integration
- `requirements.txt`: Python dependencies
- `vercel.json`: Vercel deployment configuration
- `api/index.py`: Serverless function entry point
- `ANALYTICS_SETUP.md`: This documentation

## References

- [Vercel Web Analytics Documentation](https://vercel.com/docs/analytics)
- [Vercel Web Analytics Privacy](https://vercel.com/docs/analytics/privacy-policy)
- [FastHTML Documentation](https://docs.fastht.ml/)
- [Core Web Vitals](https://web.dev/vitals/)

## Next Steps

1. Deploy to Vercel
2. Monitor analytics in your dashboard
3. Optimize based on Core Web Vitals metrics
4. Consider custom events for deeper insights (if using supported framework)
