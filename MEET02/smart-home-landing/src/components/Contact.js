import React, { useState } from 'react';
import './Contact.css';

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    phone: '',
    subject: '',
    message: ''
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    // Simulate form submission
    setTimeout(() => {
      setIsSubmitting(false);
      setSubmitStatus('success');
      setFormData({
        name: '',
        email: '',
        phone: '',
        subject: '',
        message: ''
      });
      
      // Reset status after 3 seconds
      setTimeout(() => {
        setSubmitStatus(null);
      }, 3000);
    }, 2000);
  };

  return (
    <div className="contact-page">
      <div className="container">
        <div className="section">
          <h1 className="section-title">Contact Us</h1>
          <p className="section-subtitle">
            Get in touch with our team for any questions or inquiries
          </p>

          <div className="contact-content">
            {/* Contact Information */}
            <div className="contact-info">
              <div className="card">
                <h2>Get In Touch</h2>
                <p>
                  Ready to transform your home with smart technology? Our team is here to help 
                  you every step of the way.
                </p>
                
                <div className="contact-details">
                  <div className="contact-item">
                    <div className="contact-icon">📍</div>
                    <div>
                      <h3>Address</h3>
                      <p>123 Smart Street<br />Tech City, TC 12345<br />United States</p>
                    </div>
                  </div>
                  
                  <div className="contact-item">
                    <div className="contact-icon">📧</div>
                    <div>
                      <h3>Email</h3>
                      <p>info@smarthome.com<br />support@smarthome.com</p>
                    </div>
                  </div>
                  
                  <div className="contact-item">
                    <div className="contact-icon">📞</div>
                    <div>
                      <h3>Phone</h3>
                      <p>+1 (555) 123-4567<br />+1 (555) 987-6543</p>
                    </div>
                  </div>
                  
                  <div className="contact-item">
                    <div className="contact-icon">🕒</div>
                    <div>
                      <h3>Business Hours</h3>
                      <p>Monday - Friday: 9:00 AM - 6:00 PM<br />Saturday: 10:00 AM - 4:00 PM<br />Sunday: Closed</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Contact Form */}
            <div className="contact-form">
              <div className="card">
                <h2>Send us a Message</h2>
                
                {submitStatus === 'success' && (
                  <div className="success">
                    Thank you for your message! We'll get back to you soon.
                  </div>
                )}
                
                <form onSubmit={handleSubmit}>
                  <div className="form-group">
                    <label htmlFor="name">Full Name *</label>
                    <input
                      type="text"
                      id="name"
                      name="name"
                      value={formData.name}
                      onChange={handleChange}
                      required
                    />
                  </div>
                  
                  <div className="form-group">
                    <label htmlFor="email">Email Address *</label>
                    <input
                      type="email"
                      id="email"
                      name="email"
                      value={formData.email}
                      onChange={handleChange}
                      required
                    />
                  </div>
                  
                  <div className="form-group">
                    <label htmlFor="phone">Phone Number</label>
                    <input
                      type="tel"
                      id="phone"
                      name="phone"
                      value={formData.phone}
                      onChange={handleChange}
                    />
                  </div>
                  
                  <div className="form-group">
                    <label htmlFor="subject">Subject *</label>
                    <select
                      id="subject"
                      name="subject"
                      value={formData.subject}
                      onChange={handleChange}
                      required
                    >
                      <option value="">Select a subject</option>
                      <option value="general">General Inquiry</option>
                      <option value="sales">Sales Question</option>
                      <option value="support">Technical Support</option>
                      <option value="partnership">Partnership</option>
                      <option value="other">Other</option>
                    </select>
                  </div>
                  
                  <div className="form-group">
                    <label htmlFor="message">Message *</label>
                    <textarea
                      id="message"
                      name="message"
                      value={formData.message}
                      onChange={handleChange}
                      rows="5"
                      required
                    ></textarea>
                  </div>
                  
                  <button 
                    type="submit" 
                    className="btn btn-secondary"
                    disabled={isSubmitting}
                  >
                    {isSubmitting ? 'Sending...' : 'Send Message'}
                  </button>
                </form>
              </div>
            </div>
          </div>

          {/* FAQ Section */}
          <div className="faq-section">
            <h2 className="section-title">Frequently Asked Questions</h2>
            <div className="faq-grid">
              <div className="faq-item">
                <h3>How does smart home automation work?</h3>
                <p>
                  Smart home automation uses IoT (Internet of Things) devices that connect to your 
                  home network and can be controlled remotely through our mobile app or voice commands.
                </p>
              </div>
              
              <div className="faq-item">
                <h3>What devices are compatible with your system?</h3>
                <p>
                  Our system is compatible with a wide range of devices including smart lights, 
                  thermostats, security cameras, door locks, and more. We support major protocols 
                  like Zigbee, Z-Wave, and Wi-Fi.
                </p>
              </div>
              
              <div className="faq-item">
                <h3>Is my data secure?</h3>
                <p>
                  Absolutely! We use enterprise-grade encryption and security protocols to protect 
                  your personal data and home network. Your privacy is our top priority.
                </p>
              </div>
              
              <div className="faq-item">
                <h3>Do you offer installation services?</h3>
                <p>
                  Yes, we offer professional installation services for all our smart home products. 
                  Our certified technicians ensure everything is set up correctly and working perfectly.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Contact; 