import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div>
      <h1>Welcome to Halo42</h1>
      <p>This application demonstrates Vercel Web Analytics integration with React Router.</p>
      <section>
        <h2>Features</h2>
        <ul>
          <li>React Router for client-side routing</li>
          <li>Vercel Web Analytics for visitor tracking</li>
          <li>TypeScript for type safety</li>
          <li>Vite for fast development and builds</li>
        </ul>
      </section>
      <section>
        <h2>Getting Started</h2>
        <p>
          The Vercel Web Analytics component is automatically integrated into the app root.
          Once deployed to Vercel, analytics data will be collected automatically for:
        </p>
        <ul>
          <li>Page views and navigation</li>
          <li>Performance metrics</li>
          <li>User interactions</li>
        </ul>
      </section>
      <p>
        <Link to="/about">Learn more about this project →</Link>
      </p>
    </div>
  )
}
