# Manual Smart Garden API

A FastAPI-based application for managing a smart garden system manually.

## Features

- User management with authentication
- Plant management
- Sensor and actuator control
- RESTful API with automatic documentation

## Prerequisites

- Python 3.8+
- pip or conda

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd ManualSmartGarden
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   ```bash
   alembic upgrade head
   ```

## Running the Application

1. **Start the server:**
   ```bash
   python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Access the application:**
   - API Base URL: http://localhost:8000
   - Interactive Documentation: http://localhost:8000/docs
   - OpenAPI Schema: http://localhost:8000/openapi.json

## API Endpoints

- `GET /` - Welcome message
- `GET /docs` - Interactive API documentation (Swagger UI)
- Garden management endpoints (see documentation for details)

## Project Structure

```
ManualSmartGarden/
├── app/
│   ├── applications/     # Application services
│   ├── core/            # Core configurations
│   ├── domains/         # Domain entities and interfaces
│   ├── infrastructures/ # Database and persistence
│   └── interfaces/      # API endpoints
├── alembic/             # Database migrations
├── tests/               # Test files
└── requirements.txt     # Python dependencies
```

## Development

- The application uses FastAPI for the web framework
- SQLAlchemy for database ORM
- Alembic for database migrations
- Pydantic for data validation

## License

This project is for educational purposes. 