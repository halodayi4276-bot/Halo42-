# Halo42 - FastHTML with Vercel Web Analytics

A modern FastHTML application integrated with Vercel Web Analytics for tracking user interactions, page views, and Core Web Vitals.

## Features

- 🚀 **FastHTML Framework**: Fast, lightweight Python web framework
- 📊 **Vercel Web Analytics**: Privacy-focused analytics integrated automatically
- 🔒 **Privacy-First**: GDPR & CCPA compliant, no cookies by default
- ⚡ **Performance Metrics**: Automatic Core Web Vitals tracking (LCP, FID, CLS)
- 🌍 **Multi-Page Support**: Analytics tracking across all pages
- 📱 **Responsive**: Mobile-friendly design

## Quick Start

### Prerequisites

- Python 3.9+
- pip or your preferred Python package manager

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run the development server
python app.py
```

The app will start at `http://localhost:8000`

## Deployment to Vercel

### 1. Enable Web Analytics

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project
3. Click **Analytics** tab
4. Click **Enable**

### 2. Deploy

```bash
# Install Vercel CLI
pip install vercel

# Deploy to production
vercel deploy --prod
```

### 3. View Your Analytics

After deployment and once you have traffic:
1. Go to your Vercel Dashboard
2. Select your project
3. Click **Analytics** tab
4. View your metrics!

## Project Structure

```
.
├── app.py                 # Main FastHTML application
├── api/
│   └── index.py          # Vercel serverless entry point
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel deployment config
├── pyproject.toml        # Project metadata
├── ANALYTICS_SETUP.md    # Detailed analytics documentation
└── README.md             # This file
```

## How Vercel Web Analytics Works

The application automatically includes the Vercel Web Analytics script in all HTML pages:

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
- Tracks page views automatically
- Monitors Core Web Vitals
- Sends anonymized data to Vercel
- Works without cookies

## What Gets Tracked

- 📄 **Page Views**: Every page visit
- ⚡ **Core Web Vitals**: LCP, FID, CLS metrics
- 🌍 **Geography**: Anonymized location data
- 📱 **Device Info**: Browser and OS details
- 🔗 **Referrers**: Where traffic comes from

## Privacy & Compliance

- ✅ **GDPR Compliant**: Privacy-focused by design
- ✅ **CCPA Compliant**: No tracking cookies
- ✅ **First-Party Analytics**: Your data stays in your Vercel account
- ✅ **Transparent**: All tracking is from your domain

## Pages

- `/` - Home page with analytics overview
- `/about` - Secondary page demonstrating multi-page tracking

## Documentation

For detailed setup and configuration, see [ANALYTICS_SETUP.md](./ANALYTICS_SETUP.md)

## References

- [Vercel Web Analytics](https://vercel.com/docs/analytics)
- [FastHTML Docs](https://docs.fastht.ml/)
- [Core Web Vitals](https://web.dev/vitals/)

## License

MIT License - See LICENSE file for details

---

**Next Steps**: Deploy to Vercel and start tracking your analytics! 🎉
