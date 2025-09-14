# Health Administrative Tool

A comprehensive healthcare administrative system with AI integration for patient data management, relationship building, and secure data handling.

## Features

- **Secure Patient Database**: HIPAA-compliant patient data storage with encryption
- **AI Integration**: Ollama 8B model for intelligent patient insights and recommendations
- **Modern GUI**: Cross-platform desktop application built with CustomTkinter
- **Mobile Interface**: Responsive web interface for mobile access
- **Patient Relationship Management**: Track interactions and build patient relationships
- **Data Security**: End-to-end encryption and secure authentication

## Architecture

- **Backend**: FastAPI with SQLAlchemy for robust API and database management
- **Frontend**: CustomTkinter for desktop GUI, HTML/CSS/JS for web interface
- **AI**: Ollama integration for local AI inference
- **Database**: PostgreSQL with encrypted patient data
- **Security**: JWT authentication, bcrypt password hashing, data encryption

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

3. Initialize database:
```bash
alembic upgrade head
```

4. Start the application:
```bash
python main.py
```

## Project Structure

```
├── app/
│   ├── api/           # FastAPI routes and endpoints
│   ├── core/          # Core configuration and security
│   ├── db/            # Database models and connections
│   ├── models/        # Pydantic models
│   └── services/      # Business logic and AI integration
├── gui/               # Desktop GUI application
├── web/               # Web interface
├── tests/             # Test files
└── docs/              # Documentation
```

## Security

This application implements healthcare-grade security measures:
- Patient data encryption at rest and in transit
- HIPAA-compliant data handling
- Secure authentication and authorization
- Audit logging for all patient data access
