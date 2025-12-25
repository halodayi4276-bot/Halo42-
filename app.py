#!/usr/bin/env python
"""
FastHTML application with Vercel Web Analytics integration.

This example demonstrates how to integrate Vercel Web Analytics with a FastHTML application.
The analytics script is included in the HTML template, allowing you to track user interactions
and page views across your application.
"""

from fasthtml.common import *

# Create the FastHTML app
app = FastHTML()


# Define the analytics script that will be injected into the page
def analytics_script():
    """
    Returns the Vercel Web Analytics script.
    
    This script captures page views and custom events when deployed to Vercel.
    The script is a no-op when running locally or on non-Vercel deployments.
    """
    return Script("""
    window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
    """), Script(src="/_vercel/insights/script.js", defer=True)


@app.get("/")
def home():
    """Homepage with Vercel Web Analytics integration."""
    return Html(
        Head(
            Title("FastHTML with Vercel Web Analytics"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Style("""
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
                        'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
                    -webkit-font-smoothing: antialiased;
                    -moz-osx-font-smoothing: grayscale;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                    color: #333;
                }
                h1, h2 {
                    color: #ffffff;
                }
                .container {
                    background: white;
                    border-radius: 8px;
                    padding: 30px;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                }
                code {
                    background: #f4f4f4;
                    padding: 2px 6px;
                    border-radius: 3px;
                    font-family: 'Courier New', monospace;
                }
                .feature {
                    background: #f9f9f9;
                    border-left: 4px solid #667eea;
                    padding: 15px;
                    margin: 15px 0;
                    border-radius: 4px;
                }
                button {
                    background: #667eea;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                    margin: 10px 0;
                }
                button:hover {
                    background: #764ba2;
                }
                .info-box {
                    background: #e3f2fd;
                    border-left: 4px solid #2196f3;
                    padding: 15px;
                    margin: 15px 0;
                    border-radius: 4px;
                }
            """),
        ),
        Body(
            Div(
                Div(
                    H1("🚀 FastHTML with Vercel Web Analytics"),
                    P(
                        "This is a FastHTML application integrated with ",
                        Strong("Vercel Web Analytics"),
                        " to track user interactions and page views."
                    ),
                    Div(
                        H2("✨ Features"),
                        Div(
                            H3("Automatic Page View Tracking"),
                            P("Every page view is automatically tracked when deployed to Vercel."),
                            className="feature"
                        ),
                        Div(
                            H3("Custom Event Tracking"),
                            P(
                                "You can track custom events using the ",
                                Code("window.va()"),
                                " function. Click the button below to see it in action!"
                            ),
                            Button(
                                "Track Custom Event",
                                onclick="window.va('event', { name: 'custom_button_click', data: { timestamp: new Date().toISOString() } }); alert('Event tracked!');",
                            ),
                            className="feature"
                        ),
                        Div(
                            H3("Network Monitoring"),
                            P(
                                "Check your browser's Network tab for requests to ",
                                Code("/_vercel/insights/view"),
                                " when deployed to Vercel."
                            ),
                            className="feature"
                        ),
                    ),
                    Div(
                        H2("🔧 Setup Instructions"),
                        Ol(
                            Li("Install dependencies: ", Code("pip install -r requirements.txt")),
                            Li("Enable Web Analytics in your Vercel dashboard"),
                            Li("Deploy to Vercel: ", Code("vercel deploy")),
                            Li("View analytics in the Analytics tab of your Vercel dashboard"),
                        ),
                    ),
                    Div(
                        H2("📊 Analytics Dashboard"),
                        P(
                            "After deploying to Vercel, visit your ",
                            A(
                                "Vercel Dashboard",
                                href="https://vercel.com/dashboard",
                                target="_blank"
                            ),
                            " to:"
                        ),
                        Ul(
                            Li("View real-time visitor analytics"),
                            Li("Monitor page view trends"),
                            Li("Track custom events"),
                            Li("Filter data by various metrics"),
                        ),
                    ),
                    Div(
                        H2("📚 Documentation"),
                        P("For more information, visit:"),
                        Ul(
                            Li(
                                A(
                                    "Vercel Web Analytics",
                                    href="https://vercel.com/docs/analytics",
                                    target="_blank"
                                )
                            ),
                            Li(
                                A(
                                    "@vercel/analytics Package",
                                    href="https://www.npmjs.com/package/@vercel/analytics",
                                    target="_blank"
                                )
                            ),
                            Li(
                                A(
                                    "FastHTML Documentation",
                                    href="https://docs.fastht.ml/",
                                    target="_blank"
                                )
                            ),
                        ),
                    ),
                    Div(
                        H2("🌐 Deployment"),
                        P("To deploy this application to Vercel:"),
                        Ol(
                            Li("Install Vercel CLI: ", Code("npm i -g vercel")),
                            Li("Deploy: ", Code("vercel deploy")),
                            Li("Follow the prompts to set up your project"),
                        ),
                        className="info-box"
                    ),
                    className="container"
                ),
            ),
            # Include the Vercel Web Analytics scripts
            *analytics_script(),
        ),
    )


@app.get("/about")
def about():
    """About page to demonstrate multi-page analytics tracking."""
    return Html(
        Head(
            Title("About - FastHTML with Vercel Web Analytics"),
            Meta(charset="utf-8"),
            Meta(name="viewport", content="width=device-width, initial-scale=1"),
            Style("""
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                }
                .container {
                    background: white;
                    border-radius: 8px;
                    padding: 30px;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
                }
                h1 {
                    color: #667eea;
                }
                a {
                    color: #667eea;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
            """),
        ),
        Body(
            Div(
                H1("About FastHTML with Vercel Analytics"),
                P("This application demonstrates how to integrate Vercel Web Analytics with FastHTML."),
                P(
                    "Visit the ",
                    A("homepage", href="/"),
                    " to explore more features and learn about analytics tracking."
                ),
                P("Every page you visit is tracked and will appear in your Vercel Analytics dashboard once deployed."),
                className="container"
            ),
            *analytics_script(),
        ),
    )


if __name__ == "__main__":
    serve(port=8000)
