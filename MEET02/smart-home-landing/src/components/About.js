import React from 'react';
import './About.css';

const About = () => {
  return (
    <div className="about-page">
      <div className="container">
        <div className="section">
          <h1 className="section-title">About SmartHome</h1>
          <p className="section-subtitle">
            Leading the future of home automation with innovative IoT solutions
          </p>

          {/* Company Story */}
          <div className="about-section">
            <div className="card">
              <h2>Our Story</h2>
              <p>
                Founded in 2020, SmartHome has been at the forefront of the home automation revolution. 
                We started with a simple mission: to make homes smarter, safer, and more energy-efficient 
                through cutting-edge technology.
              </p>
              <p>
                Today, we serve thousands of customers worldwide, providing comprehensive smart home 
                solutions that transform the way people live. Our team of engineers, designers, and 
                IoT experts work tirelessly to create innovative products that seamlessly integrate 
                into your daily life.
              </p>
            </div>
          </div>

          {/* Mission & Vision */}
          <div className="mission-vision">
            <div className="mission-card">
              <div className="card">
                <h3>🎯 Our Mission</h3>
                <p>
                  To democratize smart home technology by making it accessible, affordable, and 
                  user-friendly for everyone. We believe that every home deserves to be smart.
                </p>
              </div>
            </div>
            
            <div className="vision-card">
              <div className="card">
                <h3>🔮 Our Vision</h3>
                <p>
                  To be the global leader in smart home automation, creating a world where 
                  technology enhances human comfort, security, and sustainability.
                </p>
              </div>
            </div>
          </div>

          {/* Values */}
          <div className="values-section">
            <h2 className="section-title">Our Values</h2>
            <div className="values-grid">
              <div className="value-card">
                <div className="value-icon">💡</div>
                <h3>Innovation</h3>
                <p>Constantly pushing boundaries to create the next generation of smart home technology.</p>
              </div>
              
              <div className="value-card">
                <div className="value-icon">🤝</div>
                <h3>Customer First</h3>
                <p>Every decision we make is centered around improving the customer experience.</p>
              </div>
              
              <div className="value-card">
                <div className="value-icon">🌱</div>
                <h3>Sustainability</h3>
                <p>Committed to creating eco-friendly solutions that help protect our planet.</p>
              </div>
              
              <div className="value-card">
                <div className="value-icon">🔒</div>
                <h3>Security</h3>
                <p>Your privacy and security are our top priorities in everything we build.</p>
              </div>
            </div>
          </div>

          {/* Team */}
          <div className="team-section">
            <h2 className="section-title">Our Team</h2>
            <div className="team-grid">
              <div className="team-member">
                <div className="member-avatar">👨‍💼</div>
                <h3>John Smith</h3>
                <p className="member-role">CEO & Founder</p>
                <p>10+ years in IoT and home automation</p>
              </div>
              
              <div className="team-member">
                <div className="member-avatar">👩‍💻</div>
                <h3>Sarah Johnson</h3>
                <p className="member-role">CTO</p>
                <p>Expert in smart home protocols and AI</p>
              </div>
              
              <div className="team-member">
                <div className="member-avatar">👨‍🎨</div>
                <h3>Mike Chen</h3>
                <p className="member-role">Head of Design</p>
                <p>Creating beautiful, intuitive user experiences</p>
              </div>
              
              <div className="team-member">
                <div className="member-avatar">👩‍🔬</div>
                <h3>Emily Davis</h3>
                <p className="member-role">Lead Engineer</p>
                <p>Specialist in embedded systems and IoT</p>
              </div>
            </div>
          </div>

          {/* Stats */}
          <div className="stats-section">
            <div className="stats-grid">
              <div className="stat-card">
                <div className="stat-number">10,000+</div>
                <div className="stat-label">Happy Customers</div>
              </div>
              
              <div className="stat-card">
                <div className="stat-number">50+</div>
                <div className="stat-label">Smart Devices</div>
              </div>
              
              <div className="stat-card">
                <div className="stat-number">30%</div>
                <div className="stat-label">Energy Savings</div>
              </div>
              
              <div className="stat-card">
                <div className="stat-number">24/7</div>
                <div className="stat-label">Support</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About; 