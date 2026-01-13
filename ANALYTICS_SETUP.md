# Vercel Web Analytics Setup for FastHTML

This guide explains how to use Vercel Web Analytics with your FastHTML application.

## Prerequisites

- A Vercel account. If you don't have one, you can [sign up for free](https://vercel.com/signup).
- A Vercel project. If you don't have one, you can [create a new project](https://vercel.com/new).
- Python 3.8+ installed locally
- The Vercel CLI installed:

```bash
npm i -g vercel
```

## Installation

### 1. Install FastHTML

Install FastHTML using pip:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install fasthtml
```

### 2. Enable Web Analytics in Vercel

1. Go to your [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project
3. Click the **Analytics** tab
4. Click **Enable** from the dialog

> **Note:** Enabling Web Analytics will add new routes (scoped at `/_vercel/insights/*`) after your next deployment.

## Integration with FastHTML

### Adding the Analytics Script

For FastHTML applications, you need to include the Vercel Web Analytics script in your HTML pages. This application includes a helper function `analytics_script()` that returns the required script tags:

```python
def analytics_script():
    """
    Returns the Vercel Web Analytics script.
    """
    return Script("""
    window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
    """), Script(src="/_vercel/insights/script.js", defer=True)
```

### Using in Your Pages

Include the analytics script in your page's Body element:

```python
@app.get("/")
def home():
    return Html(
        Head(...),
        Body(
            # Your content here
            *analytics_script(),
        ),
    )
```

### Tracking Custom Events

You can track custom events using the `window.va()` function:

```python
# In your HTML:
Button(
    "Click Me",
    onclick="window.va('event', { name: 'button_click', data: { action: 'clicked' } });"
)
```

## Running Locally

Start the development server:

```bash
python app.py
```

The app will be available at `http://localhost:8000`.

> **Note:** Analytics tracking only works when deployed to Vercel. The script is a no-op when running locally.

## Deployment to Vercel

### 1. Initialize Vercel (if not already done)

```bash
vercel
```

Follow the prompts to set up your project.

### 2. Deploy Your Application

```bash
vercel deploy
```

### 3. Verify Deployment

Once deployed:
- Visit your deployed URL
- Open the browser's Developer Tools → Network tab
- Look for requests to `/_vercel/insights/view`
- These requests confirm analytics tracking is active

## Viewing Your Data

After deployment and once users have visited your site:

1. Go to your [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project
3. Click the **Analytics** tab
4. Explore your data:
   - View real-time visitor metrics
   - See page view trends
   - Track custom events (for Pro/Enterprise plans)
   - Filter data by various metrics

### Timeline

- **Immediately**: Tracking starts working
- **After a few hours**: Basic analytics appear in the dashboard
- **After 24-48 hours**: Full analytics data is available with trends and comparisons

## Key Metrics Tracked

By default, Vercel Web Analytics tracks:

- **Page Views**: Every time a user visits a page
- **Unique Visitors**: Based on anonymous fingerprinting
- **Referrers**: Where your traffic is coming from
- **Top Pages**: Which pages are most popular
- **Devices**: Desktop, mobile, tablet distribution
- **Browsers**: Browser and OS information
- **Countries**: Geographic distribution of visitors

## Custom Events (Pro/Enterprise Plans)

For Pro and Enterprise plans, you can track custom events:

```python
# Track button clicks
Button(
    "Sign Up",
    onclick="window.va('event', { name: 'signup_click' });"
)

# Track form submissions
Form(
    Input(type="email", name="email"),
    Button("Subscribe"),
    onsubmit="window.va('event', { name: 'newsletter_signup' }); return true;"
)

# Track purchases
onclick="window.va('event', { name: 'purchase', data: { amount: 99.99, product: 'premium' } });"
```

## Privacy and Compliance

Vercel Web Analytics is built with privacy in mind:

- **No cookies**: Does not use cookies for tracking
- **GDPR compliant**: Complies with GDPR and privacy regulations
- **No PII collected**: Does not collect personally identifiable information
- **Visitor anonymity**: Users are anonymously fingerprinted

For more details, see the [Privacy Policy](https://vercel.com/docs/analytics/privacy-policy).

## Troubleshooting

### Analytics Not Showing Data

1. **Check deployment**: Ensure your app is deployed to Vercel
2. **Verify script**: Open DevTools → Network tab and look for `/_vercel/insights/script.js`
3. **Check console**: Look for any JavaScript errors
4. **Wait for data**: It can take 5-10 minutes for initial data to appear

### Script Not Loading

If `/_vercel/insights/script.js` is not loading:

1. Verify Web Analytics is enabled in your Vercel dashboard
2. Check that your pages include the `analytics_script()` output
3. Verify the script tags are in the `<body>` of your HTML

### No Custom Events Appearing

- Verify you're on a Pro or Enterprise plan
- Check browser console for any JavaScript errors
- Ensure the `window.va()` function is being called

## Next Steps

- Learn more about [Vercel Web Analytics](https://vercel.com/docs/analytics)
- Explore [custom events](https://vercel.com/docs/analytics/custom-events)
- Read about [data filtering](https://vercel.com/docs/analytics/filtering)
- Check [pricing and limits](https://vercel.com/docs/analytics/limits-and-pricing)
- Review the [@vercel/analytics package](https://www.npmjs.com/package/@vercel/analytics)

## Example Application

This repository includes an example FastHTML application with Vercel Web Analytics fully integrated. The `app.py` file demonstrates:

- Basic page structure
- Analytics script integration
- Custom event tracking
- Multi-page application setup

Run the example:

```bash
python app.py
# Visit http://localhost:8000
# Deploy to Vercel to see analytics
```

## Support

For additional help:

- [Vercel Documentation](https://vercel.com/docs)
- [FastHTML Documentation](https://docs.fastht.ml/)
- [Vercel Community](https://vercel.com/community)
