import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

const Home = () => {
  return (
    <div className="home">
      {/* Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-content">
            <h1 className="hero-title">
              The Future of <span className="highlight">Home Automation</span>
            </h1>
            <p className="hero-subtitle">
              Transform your home into a smart, connected, and energy-efficient living space with our cutting-edge IoT solutions.
            </p>
            <div className="hero-buttons">
              <Link to="/temperature" className="btn">
                View Temperature
              </Link>
              <Link to="/contact" className="btn btn-secondary">
                Get Started
              </Link>
            </div>
          </div>
          <div className="hero-image">
            <div className="smart-home-mockup">
              <div className="device device-1">📱</div>
              <div className="device device-2">💡</div>
              <div className="device device-3">🌡️</div>
              <div className="device device-4">🔒</div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="section features">
        <div className="container">
          <h2 className="section-title">Why Choose SmartHome?</h2>
          <p className="section-subtitle">
            Experience the convenience and efficiency of smart home technology
          </p>
          
          <div className="features-grid">
            <div className="feature-card">
              <div className="feature-icon">🏠</div>
              <h3>Smart Home Control</h3>
              <p>Control all your devices from anywhere in the world with our intuitive mobile app.</p>
            </div>
            
            <div className="feature-card">
              <div className="feature-icon">⚡</div>
              <h3>Energy Efficiency</h3>
              <p>Save up to 30% on your energy bills with smart automation and monitoring.</p>
            </div>
            
            <div className="feature-card">
              <div className="feature-icon">🔒</div>
              <h3>Enhanced Security</h3>
              <p>Keep your home safe with smart locks, cameras, and motion sensors.</p>
            </div>
            
            <div className="feature-card">
              <div className="feature-icon">🌡️</div>
              <h3>Climate Control</h3>
              <p>Maintain perfect temperature and humidity levels automatically.</p>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="section cta">
        <div className="container">
          <div className="cta-content">
            <h2>Ready to Smartify Your Home?</h2>
            <p>Join thousands of happy customers who have transformed their homes with our smart solutions.</p>
            <Link to="/contact" className="btn btn-secondary">
              Contact Us Today
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home; 