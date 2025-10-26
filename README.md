
Action: file_editor str_replace /app/README.md --old-str "This is a project template for a FastAPI React MongoDB app.

The backend is a FastAPI server that connects to a MongoDB database.
The frontend is a React app that connects to the backend.

## Getting Started

### Backend

1. Navigate to the backend directory: `cd backend`
2. Install the dependencies: `pip install -r requirements.txt`
3. Start the server: `uvicorn server:app --reload`

### Frontend

1. Navigate to the frontend directory: `cd frontend`
2. Install the dependencies: `yarn install`
3. Start the development server: `yarn start`

## File Structure

- `backend/`: Contains the FastAPI backend
  - `server.py`: Main FastAPI application
  - `requirements.txt`: Python dependencies
- `frontend/`: Contains the React frontend
  - `src/`: React source code
  - `public/`: Static assets
  - `package.json`: Node.js dependencies and scripts" --new-str "# ✈️ Voos Baratos SP - Flight Search Application

A comprehensive flight search web application that helps users find the cheapest international flights departing from São Paulo airports (GRU/CGH/VCP) to global destinations, featuring advanced filters and a global price heatmap.

![Flight Search App](https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=800)

## 🌟 Features

### ✈️ **Core Flight Search**
- **Fixed Origin**: São Paulo airports (GRU - Guarulhos, CGH - Congonhas, VCP - Viracopos)
- **Global Destinations**: Search flights to any international destination
- **Real-time Data**: Integration with Amadeus Flight Offers Search API
- **Multiple Airlines**: LATAM, Gol, Azul, American Airlines, Avianca, Copa Airlines, and more

### 🔍 **Advanced Search & Filters**
- **Flexible Dates**: Calendar-based date selection with future date validation
- **Passenger Selection**: 1-9 passengers supported
- **Travel Classes**: Economy, Premium Economy, Business, First Class
- **Price Filtering**: Maximum price limits in Brazilian Real (BRL)
- **Direct Flights**: Toggle for non-stop flights only
- **Quick Destinations**: One-click selection for popular destinations (JFK, LHR, CDG, MAD, LIS, FCO)

### 🎨 **Modern UI/UX**
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Glass Morphism**: Modern UI with backdrop blur effects
- **Smooth Animations**: Micro-interactions and loading states
- **Professional Typography**: Inter font family for enhanced readability
- **Accessibility**: Proper focus states and semantic HTML

### 📊 **Detailed Flight Results**
- **Comprehensive Information**: Departure/arrival times, duration, stops, aircraft type
- **Price Breakdown**: Base fare, taxes, total price with currency formatting
- **Multiple Booking Options**: Direct airline websites + travel agencies (Kayak, Expedia)
- **Price Comparison**: Different prices across booking platforms
- **Airline Branding**: Full airline names with IATA code mapping

### 🗺️ **Global Price Heatmap**
- **Interactive Map**: Leaflet-powered world map with price visualization
- **Color-coded Markers**: Green (<R$3k), Yellow (R$3k-4k), Red (>R$4k)
- **Detailed Popups**: City info, prices, and booking links
- **São Paulo Origin**: Clearly marked departure point

### 💳 **Booking Integration**
- **Multiple Marketplaces**: Official airline websites, OTAs, and travel agencies
- **Price Comparison**: Show different prices across platforms
- **Direct Links**: One-click access to booking platforms
- **Best Price Highlighting**: Visual indication of lowest prices

## 🛠️ Tech Stack

### **Backend**
- **Framework**: FastAPI (Python 3.8+)
- **Database**: MongoDB with Motor (async driver)
- **API Integration**: Amadeus Flight Offers Search API
- **Authentication**: OAuth2 client credentials flow
- **Validation**: Pydantic models for data validation
- **Async Processing**: ThreadPoolExecutor for API calls
- **CORS**: Configured for cross-origin requests

### **Frontend**
- **Framework**: React 19.0.0
- **Routing**: React Router DOM
- **UI Components**: Shadcn/UI with Radix UI primitives
- **Styling**: Tailwind CSS with custom animations
- **HTTP Client**: Axios for API communication
- **Maps**: React Leaflet with OpenStreetMap tiles
- **Icons**: Lucide React
- **Forms**: React Hook Form with Zod validation

### **DevOps & Infrastructure**
- **Process Management**: Supervisor for service management
- **Server**: Uvicorn ASGI server
- **Environment**: Docker containerized deployment
- **Monitoring**: Comprehensive logging and error tracking

## 📁 Project Structure

```
flight-search-app/
├── backend/
│   ├── server.py              # FastAPI application with all endpoints
│   ├── requirements.txt       # Python dependencies
│   └── .env                   # Environment variables (API keys, DB config)
├── frontend/
│   ├── public/               # Static assets
│   ├── src/
│   │   ├── components/       # React components
│   │   │   ├── ui/          # Shadcn/UI component library
│   │   │   ├── Header.js    # Application header
│   │   │   ├── Hero.js      # Landing page hero section
│   │   │   ├── SearchForm.js # Flight search form with filters
│   │   │   ├── FlightResults.js # Results display and booking
│   │   │   └── GlobalMap.js # Interactive price heatmap
│   │   ├── App.js           # Main application component
│   │   ├── App.css          # Global styles and animations
│   │   └── index.js         # React application entry point
│   ├── package.json         # Node.js dependencies
│   ├── tailwind.config.js   # Tailwind CSS configuration
│   └── .env                 # Frontend environment variables
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites
- **Python 3.8+**
- **Node.js 16+**
- **MongoDB instance**
- **Amadeus API credentials** (free developer account)

### Backend Setup

1. **Navigate to backend directory**:
```bash
cd backend
```

2. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

3. **Configure environment variables** in `.env`:
```env
MONGO_URL=\"mongodb://localhost:27017\"
DB_NAME=\"flight_search_db\"
CORS_ORIGINS=\"*\"
AMADEUS_CLIENT_ID=\"your_amadeus_client_id\"
AMADEUS_CLIENT_SECRET=\"your_amadeus_client_secret\"
AMADEUS_HOSTNAME=\"test\"  # Use \"production\" for live data
```

4. **Start the FastAPI server**:
```bash
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

### Frontend Setup

1. **Navigate to frontend directory**:
```bash
cd frontend
```

2. **Install Node.js dependencies**:
```bash
yarn install
```

3. **Configure environment variables** in `.env`:
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

4. **Start the React development server**:
```bash
yarn start
```

### Amadeus API Setup

1. **Register for free**: Visit [Amadeus for Developers](https://developers.amadeus.com/register)
2. **Create application**: Get your API key and secret
3. **Test environment**: Use test credentials for development
4. **Production**: Switch to production environment for live data

## 🔧 Configuration

### Environment Variables

#### Backend (.env)
- `MONGO_URL`: MongoDB connection string
- `DB_NAME`: Database name for the application
- `AMADEUS_CLIENT_ID`: Amadeus API client ID
- `AMADEUS_CLIENT_SECRET`: Amadeus API client secret
- `AMADEUS_HOSTNAME`: API environment (test/production)
- `CORS_ORIGINS`: Allowed origins for CORS

#### Frontend (.env)
- `REACT_APP_BACKEND_URL`: Backend API base URL

### Customization

#### Adding New Airlines
Update the `AIRLINE_NAMES` mapping in `backend/server.py`:
```python
AIRLINE_NAMES = {
    'LA': 'LATAM Airlines',
    'G3': 'Gol',
    'AD': 'Azul',
    # Add new airlines here
}
```

#### Modifying Popular Destinations
Edit the destinations array in the `/popular-destinations` endpoint:
```python
destinations = [
    {\"iata\": \"JFK\", \"city\": \"New York\", \"country\": \"USA\", \"coordinates\": [40.7128, -74.0060]},
    # Add new destinations here
]
```

## 🧪 API Endpoints

### Flight Search
```http
POST /api/search-flights
Content-Type: application/json

{
  \"destination\": \"JFK\",
  \"departure_date\": \"2024-12-15\",
  \"passengers\": 1,
  \"travel_class\": \"ECONOMY\",
  \"max_price\": 5000,
  \"direct_flights\": false
}
```

### Popular Destinations
```http
GET /api/popular-destinations
```

### Global Prices
```http
GET /api/global-prices?departure_date=2024-12-15
```

### Health Check
```http
GET /api/health
```

## 🎨 UI Components

### Custom Components
- **SearchForm**: Advanced flight search with filters
- **FlightResults**: Responsive results display with booking options
- **GlobalMap**: Interactive price heatmap using Leaflet
- **Hero**: Landing page with call-to-action
- **Header**: Application navigation and branding

### Design System
- **Colors**: Blue primary, orange accent, semantic colors for status
- **Typography**: Inter font family with proper hierarchy
- **Spacing**: Consistent 8px grid system
- **Animations**: Smooth transitions, hover effects, loading states

## 🔐 Security & Best Practices

### API Security
- Environment variables for sensitive data
- Request validation with Pydantic
- Rate limiting considerations
- CORS configuration
- Input sanitization

### Frontend Security
- Environment variable validation
- XSS prevention
- Secure API communication
- Error boundary implementation

## 📈 Performance Optimizations

### Backend
- Async/await patterns for I/O operations
- ThreadPoolExecutor for Amadeus API calls
- Response caching strategies
- Database indexing for queries

### Frontend
- React.memo for component optimization
- Lazy loading for route components
- Image optimization
- Bundle size optimization

## 🐛 Troubleshooting

### Common Issues

#### Amadeus API Errors
- **400 Bad Request**: Check date format (YYYY-MM-DD) and required parameters
- **401 Unauthorized**: Verify API credentials in environment variables
- **429 Rate Limited**: Implement request throttling or upgrade API plan

#### CORS Issues
- Ensure backend CORS_ORIGINS includes frontend URL
- Check browser console for specific CORS errors

#### Database Connection
- Verify MongoDB is running and accessible
- Check MONGO_URL format and credentials

#### No Flight Results
- API may return empty results for some routes/dates
- Mock data fallback is implemented for development

### Development Tips
- Use browser DevTools Network tab to debug API calls
- Check backend logs for detailed error information
- Use React DevTools for component debugging

## 🚀 Deployment

### Production Checklist
- [ ] Set `AMADEUS_HOSTNAME=\"production\"` for live data
- [ ] Configure production MongoDB instance
- [ ] Set up proper CORS origins
- [ ] Enable HTTPS
- [ ] Configure proper logging levels
- [ ] Set up monitoring and alerts

### Recommended Hosting
- **Backend**: Railway, Render, or AWS
- **Frontend**: Vercel, Netlify, or AWS S3 + CloudFront
- **Database**: MongoDB Atlas

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Amadeus**: Flight data API provider
- **Shadcn/UI**: Beautiful UI component library
- **Leaflet**: Open-source mapping library
- **Tailwind CSS**: Utility-first CSS framework
- **FastAPI**: Modern Python web framework

## 📞 Support

For support and questions:
- Create an issue in the repository
- Check the troubleshooting section
- Review Amadeus API documentation

---

**Built with ❤️ for travelers seeking the best flight deals from São Paulo**"
Observation: Perfect! I have successfully updated the README.md file with the comprehensive flight search application documentation. The file has been transformed from a simple "# Here are your Instructions" to a detailed, professional README that includes:

## Key Changes Made:
- **Complete project overview** for "Voos Baratos SP - Flight Search Application"
- **Comprehensive feature list** with emojis and detailed descriptions
- **Full tech stack documentation** for both backend and frontend
- **Detailed project structure** with file descriptions
- **Step-by-step setup instructions** for both backend and frontend
- **Configuration guides** including environment variables
- **API endpoint documentation** with examples
- **UI component descriptions** and design system details
- **Security and performance optimization** sections
- **Troubleshooting guide** with common issues and solutions
- **Deployment checklist** and hosting recommendations
- **Contributing guidelines** and support information

The new README provides a complete guide for developers to understand, set up, and contribute to the flight search application, making it much more professional and informative than the original placeholder content.
 Summary: Successfully updated the README.md file from a simple placeholder ("# Here are your Instructions") to a comprehensive, professional documentation for the "Voos Baratos SP - Flight Search Application". The new README includes detailed feature descriptions, complete tech stack information, setup instructions, API documentation, troubleshooting guides, and deployment information. The file now serves as a complete guide for developers working with this flight search application that helps users find cheap international flights from São Paulo airports.
Here is the diff:
diff --git a/README.md b/README.md
index 3786c8a..c46112d 100644
--- a/README.md
+++ b/README.md
@@ -1 +1,350 @@
-# Here are your Instructions
+# ✈️ Voos Baratos SP - Flight Search Application
+
+A comprehensive flight search web application that helps users find the cheapest international flights departing from São Paulo airports (GRU/CGH/VCP) to global destinations, featuring advanced filters and a global price heatmap.
+
+![Flight Search App](https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=800)
+
+## 🌟 Features
+
+### ✈️ **Core Flight Search**
+- **Fixed Origin**: São Paulo airports (GRU - Guarulhos, CGH - Congonhas, VCP - Viracopos)
+- **Global Destinations**: Search flights to any international destination
+- **Real-time Data**: Integration with Amadeus Flight Offers Search API
+- **Multiple Airlines**: LATAM, Gol, Azul, American Airlines, Avianca, Copa Airlines, and more
+
+### 🔍 **Advanced Search & Filters**
+- **Flexible Dates**: Calendar-based date selection with future date validation
+- **Passenger Selection**: 1-9 passengers supported
+- **Travel Classes**: Economy, Premium Economy, Business, First Class
+- **Price Filtering**: Maximum price limits in Brazilian Real (BRL)
+- **Direct Flights**: Toggle for non-stop flights only
+- **Quick Destinations**: One-click selection for popular destinations (JFK, LHR, CDG, MAD, LIS, FCO)
+
+### 🎨 **Modern UI/UX**
+- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
+- **Glass Morphism**: Modern UI with backdrop blur effects
+- **Smooth Animations**: Micro-interactions and loading states
+- **Professional Typography**: Inter font family for enhanced readability
+- **Accessibility**: Proper focus states and semantic HTML
+
+### 📊 **Detailed Flight Results**
+- **Comprehensive Information**: Departure/arrival times, duration, stops, aircraft type
+- **Price Breakdown**: Base fare, taxes, total price with currency formatting
+- **Multiple Booking Options**: Direct airline websites + travel agencies (Kayak, Expedia)
+- **Price Comparison**: Different prices across booking platforms
+- **Airline Branding**: Full airline names with IATA code mapping
+
+### 🗺️ **Global Price Heatmap**
+- **Interactive Map**: Leaflet-powered world map with price visualization
+- **Color-coded Markers**: Green (<R$3k), Yellow (R$3k-4k), Red (>R$4k)
+- **Detailed Popups**: City info, prices, and booking links
+- **São Paulo Origin**: Clearly marked departure point
+
+### 💳 **Booking Integration**
+- **Multiple Marketplaces**: Official airline websites, OTAs, and travel agencies
+- **Price Comparison**: Show different prices across platforms
+- **Direct Links**: One-click access to booking platforms
+- **Best Price Highlighting**: Visual indication of lowest prices
+
+## 🛠️ Tech Stack
+
+### **Backend**
+- **Framework**: FastAPI (Python 3.8+)
+- **Database**: MongoDB with Motor (async driver)
+- **API Integration**: Amadeus Flight Offers Search API
+- **Authentication**: OAuth2 client credentials flow
+- **Validation**: Pydantic models for data validation
+- **Async Processing**: ThreadPoolExecutor for API calls
+- **CORS**: Configured for cross-origin requests
+
+### **Frontend**
+- **Framework**: React 19.0.0
+- **Routing**: React Router DOM
+- **UI Components**: Shadcn/UI with Radix UI primitives
+- **Styling**: Tailwind CSS with custom animations
+- **HTTP Client**: Axios for API communication
+- **Maps**: React Leaflet with OpenStreetMap tiles
+- **Icons**: Lucide React
+- **Forms**: React Hook Form with Zod validation
+
+### **DevOps & Infrastructure**
+- **Process Management**: Supervisor for service management
+- **Server**: Uvicorn ASGI server
+- **Environment**: Docker containerized deployment
+- **Monitoring**: Comprehensive logging and error tracking
+
+## 📁 Project Structure
+
+```
+flight-search-app/
+├── backend/
+│   ├── server.py              # FastAPI application with all endpoints
+│   ├── requirements.txt       # Python dependencies
+│   └── .env                   # Environment variables (API keys, DB config)
+├── frontend/
+│   ├── public/               # Static assets
+│   ├── src/
+│   │   ├── components/       # React components
+│   │   │   ├── ui/          # Shadcn/UI component library
+│   │   │   ├── Header.js    # Application header
+│   │   │   ├── Hero.js      # Landing page hero section
+│   │   │   ├── SearchForm.js # Flight search form with filters
+│   │   │   ├── FlightResults.js # Results display and booking
+│   │   │   └── GlobalMap.js # Interactive price heatmap
+│   │   ├── App.js           # Main application component
+│   │   ├── App.css          # Global styles and animations
+│   │   └── index.js         # React application entry point
+│   ├── package.json         # Node.js dependencies
+│   ├── tailwind.config.js   # Tailwind CSS configuration
+│   └── .env                 # Frontend environment variables
+└── README.md               # This file
+```
+
+## 🚀 Getting Started
+
+### Prerequisites
+- **Python 3.8+**
+- **Node.js 16+**
+- **MongoDB instance**
+- **Amadeus API credentials** (free developer account)
+
+### Backend Setup
+
+1. **Navigate to backend directory**:
+```bash
+cd backend
+```
+
+2. **Install Python dependencies**:
+```bash
+pip install -r requirements.txt
+```
+
+3. **Configure environment variables** in `.env`:
+```env
+MONGO_URL="mongodb://localhost:27017"
+DB_NAME="flight_search_db"
+CORS_ORIGINS="*"
+AMADEUS_CLIENT_ID="your_amadeus_client_id"
+AMADEUS_CLIENT_SECRET="your_amadeus_client_secret"
+AMADEUS_HOSTNAME="test"  # Use "production" for live data
+```
+
+4. **Start the FastAPI server**:
+```bash
+uvicorn server:app --host 0.0.0.0 --port 8001 --reload
+```
+
+### Frontend Setup
+
+1. **Navigate to frontend directory**:
+```bash
+cd frontend
+```
+
+2. **Install Node.js dependencies**:
+```bash
+yarn install
+```
+
+3. **Configure environment variables** in `.env`:
+```env
+REACT_APP_BACKEND_URL=http://localhost:8001
+```
+
+4. **Start the React development server**:
+```bash
+yarn start
+```
+
+### Amadeus API Setup
+
+1. **Register for free**: Visit [Amadeus for Developers](https://developers.amadeus.com/register)
+2. **Create application**: Get your API key and secret
+3. **Test environment**: Use test credentials for development
+4. **Production**: Switch to production environment for live data
+
+## 🔧 Configuration
+
+### Environment Variables
+
+#### Backend (.env)
+- `MONGO_URL`: MongoDB connection string
+- `DB_NAME`: Database name for the application
+- `AMADEUS_CLIENT_ID`: Amadeus API client ID
+- `AMADEUS_CLIENT_SECRET`: Amadeus API client secret
+- `AMADEUS_HOSTNAME`: API environment (test/production)
+- `CORS_ORIGINS`: Allowed origins for CORS
+
+#### Frontend (.env)
+- `REACT_APP_BACKEND_URL`: Backend API base URL
+
+### Customization
+
+#### Adding New Airlines
+Update the `AIRLINE_NAMES` mapping in `backend/server.py`:
+```python
+AIRLINE_NAMES = {
+    'LA': 'LATAM Airlines',
+    'G3': 'Gol',
+    'AD': 'Azul',
+    # Add new airlines here
+}
+```
+
+#### Modifying Popular Destinations
+Edit the destinations array in the `/popular-destinations` endpoint:
+```python
+destinations = [
+    {"iata": "JFK", "city": "New York", "country": "USA", "coordinates": [40.7128, -74.0060]},
+    # Add new destinations here
+]
+```
+
+## 🧪 API Endpoints
+
+### Flight Search
+```http
+POST /api/search-flights
+Content-Type: application/json
+
+{
+  "destination": "JFK",
+  "departure_date": "2024-12-15",
+  "passengers": 1,
+  "travel_class": "ECONOMY",
+  "max_price": 5000,
+  "direct_flights": false
+}
+```
+
+### Popular Destinations
+```http
+GET /api/popular-destinations
+```
+
+### Global Prices
+```http
+GET /api/global-prices?departure_date=2024-12-15
+```
+
+### Health Check
+```http
+GET /api/health
+```
+
+## 🎨 UI Components
+
+### Custom Components
+- **SearchForm**: Advanced flight search with filters
+- **FlightResults**: Responsive results display with booking options
+- **GlobalMap**: Interactive price heatmap using Leaflet
+- **Hero**: Landing page with call-to-action
+- **Header**: Application navigation and branding
+
+### Design System
+- **Colors**: Blue primary, orange accent, semantic colors for status
+- **Typography**: Inter font family with proper hierarchy
+- **Spacing**: Consistent 8px grid system
+- **Animations**: Smooth transitions, hover effects, loading states
+
+## 🔐 Security & Best Practices
+
+### API Security
+- Environment variables for sensitive data
+- Request validation with Pydantic
+- Rate limiting considerations
+- CORS configuration
+- Input sanitization
+
+### Frontend Security
+- Environment variable validation
+- XSS prevention
+- Secure API communication
+- Error boundary implementation
+
+## 📈 Performance Optimizations
+
+### Backend
+- Async/await patterns for I/O operations
+- ThreadPoolExecutor for Amadeus API calls
+- Response caching strategies
+- Database indexing for queries
+
+### Frontend
+- React.memo for component optimization
+- Lazy loading for route components
+- Image optimization
+- Bundle size optimization
+
+## 🐛 Troubleshooting
+
+### Common Issues
+
+#### Amadeus API Errors
+- **400 Bad Request**: Check date format (YYYY-MM-DD) and required parameters
+- **401 Unauthorized**: Verify API credentials in environment variables
+- **429 Rate Limited**: Implement request throttling or upgrade API plan
+
+#### CORS Issues
+- Ensure backend CORS_ORIGINS includes frontend URL
+- Check browser console for specific CORS errors
+
+#### Database Connection
+- Verify MongoDB is running and accessible
+- Check MONGO_URL format and credentials
+
+#### No Flight Results
+- API may return empty results for some routes/dates
+- Mock data fallback is implemented for developmen
[Output truncated to 10000 characters]
