import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    // A variável de ambiente REACT_APP_API_URL será definida pelo pipeline de CI/CD
    const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:5000';
    axios.get(`${apiUrl}/api/flights`)
      .then(response => {
        setFlights(response.data);
      })
      .catch(error => {
        console.error('Error fetching flights:', error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Flight Status</h1>
      </header>
      <div>
        <h2>All Flights</h2>
        <ul>
          {flights.map(flight => (
            <li key={flight.id}>
              {flight.flight_number} from {flight.origin} to {flight.destination} - Status: {flight.status}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
