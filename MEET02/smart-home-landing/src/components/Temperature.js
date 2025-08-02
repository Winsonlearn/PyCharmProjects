import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Temperature.css';

const Temperature = () => {
  const [currentTemp, setCurrentTemp] = useState(null);
  const [tempHistory, setTempHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [newTemp, setNewTemp] = useState('');

  // Replace with your PythonAnywhere username
  const API_BASE_URL = 'https://YOUR_USERNAME.pythonanywhere.com';

  useEffect(() => {
    fetchCurrentTemperature();
    fetchTemperatureHistory();
  }, []);

  const fetchCurrentTemperature = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${API_BASE_URL}/temperature`);
      setCurrentTemp(response.data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch current temperature');
      console.error('Error fetching current temperature:', err);
    } finally {
      setLoading(false);
    }
  };

  const fetchTemperatureHistory = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/temperatures`);
      setTempHistory(response.data);
    } catch (err) {
      console.error('Error fetching temperature history:', err);
    }
  };

  const addTemperature = async (e) => {
    e.preventDefault();
    if (!newTemp) return;

    try {
      await axios.post(`${API_BASE_URL}/temperature`, {
        temperature: parseFloat(newTemp)
      });
      setNewTemp('');
      fetchTemperatureHistory();
      setError(null);
    } catch (err) {
      setError('Failed to add temperature reading');
      console.error('Error adding temperature:', err);
    }
  };

  const deleteTemperature = async (id) => {
    try {
      await axios.delete(`${API_BASE_URL}/temperature/${id}`);
      fetchTemperatureHistory();
    } catch (err) {
      setError('Failed to delete temperature reading');
      console.error('Error deleting temperature:', err);
    }
  };

  return (
    <div className="temperature-page">
      <div className="container">
        <div className="section">
          <h1 className="section-title">Smart Home Temperature Monitor</h1>
          <p className="section-subtitle">
            Real-time temperature monitoring and control for your smart home
          </p>

          {/* Current Temperature Display */}
          <div className="current-temp-section">
            <div className="card">
              <h2>Current Temperature</h2>
              {loading ? (
                <div className="loading">Loading...</div>
              ) : error ? (
                <div className="error">{error}</div>
              ) : currentTemp ? (
                <div className="temperature-display">
                  {currentTemp.temperature}°C
                </div>
              ) : (
                <div className="error">No temperature data available</div>
              )}
              <button 
                className="btn btn-secondary" 
                onClick={fetchCurrentTemperature}
                disabled={loading}
              >
                Refresh
              </button>
            </div>
          </div>

          {/* Add New Temperature */}
          <div className="add-temp-section">
            <div className="card">
              <h2>Add New Temperature Reading</h2>
              <form onSubmit={addTemperature} className="temp-form">
                <input
                  type="number"
                  step="0.1"
                  value={newTemp}
                  onChange={(e) => setNewTemp(e.target.value)}
                  placeholder="Enter temperature (e.g., 25.5)"
                  className="temp-input"
                  required
                />
                <button type="submit" className="btn">
                  Add Reading
                </button>
              </form>
            </div>
          </div>

          {/* Temperature History */}
          <div className="temp-history-section">
            <div className="card">
              <h2>Temperature History</h2>
              {tempHistory.length === 0 ? (
                <p className="no-data">No temperature history available</p>
              ) : (
                <div className="temp-table">
                  <table>
                    <thead>
                      <tr>
                        <th>ID</th>
                        <th>Temperature (°C)</th>
                        <th>Timestamp</th>
                        <th>Actions</th>
                      </tr>
                    </thead>
                    <tbody>
                      {tempHistory.map((temp) => (
                        <tr key={temp.id}>
                          <td>{temp.id}</td>
                          <td>{temp.temperature}</td>
                          <td>{new Date(temp.timestamp).toLocaleString()}</td>
                          <td>
                            <button
                              onClick={() => deleteTemperature(temp.id)}
                              className="btn-delete"
                            >
                              Delete
                            </button>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>
          </div>

          {/* API Status */}
          <div className="api-status">
            <div className="card">
              <h2>API Status</h2>
              <p>
                <strong>API URL:</strong> {API_BASE_URL}
              </p>
              <p>
                <strong>Status:</strong> 
                <span className={error ? 'status-error' : 'status-success'}>
                  {error ? 'Error' : 'Connected'}
                </span>
              </p>
              <p className="note">
                Note: Make sure to replace 'YOUR_USERNAME' in the API URL with your actual PythonAnywhere username.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Temperature; 