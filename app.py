"""
FastHTML application with Vercel Web Analytics integration.

This application demonstrates how to integrate Vercel Web Analytics into a FastHTML app.
The analytics script is injected into all HTML pages automatically.
"""

from fasthtml.common import *

# Create the FastHTML app
app, rt = fast_app()


def analytics_script():
    """
    Returns the Vercel Web Analytics script snippet.
    
    For HTML/plain implementations, Vercel provides a simple script that should be
    added to your pages. When deployed to Vercel, the `/_vercel/insights/script.js`
    endpoint becomes available.
    """
    return Script(
        """
        window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
        """,
        src="/_vercel/insights/script.js",
        defer=True
    )


@rt("/")
def index():
    """Home page with analytics integration."""
    return Html(
        Head(
            Title("Halo42 - Vercel Web Analytics Example"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Style("""
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                    max-width: 900px;
                    margin: 0 auto;
                    padding: 20px;
                    line-height: 1.6;
                    color: #333;
                }
                h1 {
                    color: #0066cc;
                    border-bottom: 3px solid #0066cc;
                    padding-bottom: 10px;
                }
                .info-box {
                    background-color: #f0f4ff;
                    border-left: 4px solid #0066cc;
                    padding: 15px;
                    margin: 20px 0;
                    border-radius: 4px;
                }
                a {
                    color: #0066cc;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                code {
                    background-color: #f5f5f5;
                    padding: 2px 6px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                }
            """)
        ),
        Body(
            H1("🚀 Halo42 with Vercel Web Analytics"),
            
            Div(
                H2("About This Project"),
                P("This is a FastHTML application integrated with ", Strong("Vercel Web Analytics"), "."),
                P("Vercel Web Analytics automatically tracks:"),
                Ul(
                    Li("Page views"),
                    Li("Web vitals (Core Web Vitals)"),
                    Li("User interactions"),
                    Li("Performance metrics"),
                ),
                cls="info-box"
            ),
            
            Div(
                H2("How It Works"),
                P(
                    "The analytics script is automatically included in all pages. ",
                    "When deployed to Vercel, it sends anonymized analytics data to the ",
                    "Vercel dashboard."
                ),
                P("Key features:"),
                Ul(
                    Li("Privacy-focused: No cookies by default"),
                    Li("GDPR/CCPA compliant"),
                    Li("Automatic Core Web Vitals tracking"),
                    Li("Custom events support (via @vercel/analytics package on other frameworks)"),
                ),
                cls="info-box"
            ),
            
            Div(
                H2("Getting Started with Analytics"),
                Ol(
                    Li("Enable Web Analytics in your Vercel project dashboard → Analytics tab"),
                    Li("Deploy your app to Vercel using ", Code("vercel deploy")),
                    Li("Visit your deployed site and interact with it"),
                    Li("View analytics data in your dashboard after a few minutes"),
                ),
            ),
            
            Div(
                H2("Deployment"),
                P("To deploy to Vercel:"),
                Ol(
                    Li("Install Vercel CLI: ", Code("pip install vercel")),
                    Li("Run ", Code("vercel deploy")),
                    Li("Follow the prompts to link your Vercel project"),
                ),
                cls="info-box"
            ),
            
            Div(
                H2("Learn More"),
                Ul(
                    Li(A("Vercel Web Analytics Docs", href="https://vercel.com/docs/analytics")),
                    Li(A("FastHTML Documentation", href="https://docs.fastht.ml/")),
                    Li(A("Vercel Analytics Privacy", href="https://vercel.com/docs/analytics/privacy-policy")),
                ),
            ),
            
            Hr(),
            P(
                "📊 Analytics tracking is active. You can verify this by checking the Network tab in your browser's developer tools for requests to ",
                Code("/_vercel/insights/view"),
                "."
            ),
            
            # Include the Vercel Web Analytics script
            analytics_script(),
        )
    )


@rt("/about")
def about():
    """About page to test multi-page analytics tracking."""
    return Html(
        Head(
            Title("About - Halo42"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Style("""
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    max-width: 900px;
                    margin: 0 auto;
                    padding: 20px;
                }
                a {
                    color: #0066cc;
                    text-decoration: none;
                }
            """)
        ),
        Body(
            H1("About Halo42"),
            P("This is the about page of the Halo42 project with Vercel Web Analytics integration."),
            P(A("← Back to Home", href="/")),
            analytics_script(),
        )
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
