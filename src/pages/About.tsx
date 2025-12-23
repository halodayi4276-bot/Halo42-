export default function About() {
  return (
    <div>
      <h1>About Halo42</h1>
      <p>
        This is a sample React Router application that demonstrates the integration of
        Vercel Web Analytics for tracking user interactions and page metrics.
      </p>

      <h2>Vercel Web Analytics Integration</h2>
      <p>
        The <code>Analytics</code> component from <code>@vercel/analytics/react</code> is
        integrated at the root level of the application. This provides:
      </p>

      <h3>Key Features</h3>
      <ul>
        <li>Automatic page view tracking</li>
        <li>Performance metrics collection</li>
        <li>Route support with React Router</li>
        <li>Zero-configuration setup</li>
        <li>Privacy-first analytics</li>
      </ul>

      <h3>How It Works</h3>
      <p>
        Once deployed to Vercel and Web Analytics is enabled in the Vercel dashboard:
      </p>
      <ol>
        <li>The Analytics component loads the tracking script</li>
        <li>Visitor data is collected in the background</li>
        <li>No sensitive data is stored (privacy-compliant)</li>
        <li>Real-time dashboards show traffic patterns</li>
      </ol>

      <h3>Next Steps</h3>
      <p>
        To use this application with Vercel Web Analytics:
      </p>
      <ol>
        <li>Deploy to Vercel: <code>vercel deploy</code></li>
        <li>Enable Web Analytics in the Vercel dashboard</li>
        <li>View analytics data in the Analytics tab</li>
      </ol>
    </div>
  )
}
