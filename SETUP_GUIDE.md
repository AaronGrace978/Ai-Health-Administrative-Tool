# Health Administrative Tool - Setup Guide

## 🏥 AI-Powered Patient Management System

This comprehensive setup guide will help you get the Health Administrative Tool running on your system with full AI integration using Ollama.

## 📋 Prerequisites

### System Requirements
- **Operating System**: Windows 10/11, macOS, or Linux
- **Python**: 3.8 or higher
- **RAM**: Minimum 8GB (16GB recommended for AI features)
- **Storage**: At least 5GB free space
- **Internet**: Required for initial setup and AI model downloads

### Required Software
1. **Python 3.8+** - [Download from python.org](https://www.python.org/downloads/)
2. **Git** - [Download from git-scm.com](https://git-scm.com/downloads)
3. **Ollama** - [Download from ollama.ai](https://ollama.ai/download)

## 🚀 Quick Start

### 1. Install Ollama and AI Model

#### Windows/macOS:
```bash
# Download and install Ollama from https://ollama.ai/download
# Then pull the 8B model:
ollama pull llama2:8b
```

#### Linux:
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull the 8B model
ollama pull llama2:8b
```

### 2. Clone and Setup Project

```bash
# Clone the repository (if using git)
git clone <repository-url>
cd "Health Administrative Tool"

# Or if you already have the files, navigate to the directory
cd "D:\Health Administrative Tool"
```

### 3. Install Python Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy environment template
copy env.example .env

# Edit .env file with your settings
# Key settings to configure:
# - SECRET_KEY: Generate a secure random key
# - DATABASE_URL: SQLite (default) or PostgreSQL
# - OLLAMA_BASE_URL: http://localhost:11434 (default)
# - OLLAMA_MODEL: llama2:8b (default)
```

### 5. Initialize Database

```bash
# Create database tables
python -c "from app.db.database import engine; from app.db import models; models.Base.metadata.create_all(bind=engine)"
```

### 6. Start the Application

#### Option A: Start Backend and GUI Together
```bash
python start_gui.py
```

#### Option B: Start Components Separately
```bash
# Terminal 1: Start backend server
python main.py

# Terminal 2: Start GUI application
python gui/main_gui.py
```

### 7. Access the Application

- **Desktop GUI**: Automatically opens when using `start_gui.py`
- **Web Interface**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/docs
- **Mobile Interface**: http://localhost:8000 (responsive design)

## 🔧 Configuration Options

### Environment Variables (.env file)

```env
# Database Configuration
DATABASE_URL=sqlite:///./health_admin.db
# For PostgreSQL: DATABASE_URL=postgresql://user:password@localhost:5432/health_admin

# Security
SECRET_KEY=your-super-secret-key-change-this-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# AI Configuration
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2:8b

# Application Settings
APP_NAME=Health Administrative Tool
APP_VERSION=1.0.0
DEBUG=True

# Encryption
ENCRYPTION_KEY=your-32-character-encryption-key-here
```

### AI Model Options

The system supports various Ollama models:

```bash
# Popular 8B models
ollama pull llama2:8b          # Meta's Llama 2 (recommended)
ollama pull codellama:8b       # Code-focused model
ollama pull mistral:7b         # Mistral 7B (smaller, faster)

# Larger models (require more RAM)
ollama pull llama2:13b         # 13B parameter model
ollama pull llama2:70b         # 70B parameter model (requires 40GB+ RAM)
```

Update the `OLLAMA_MODEL` in your `.env` file to use a different model.

## 🏥 First-Time Setup

### 1. Create Admin User

When you first start the application:

1. Open the GUI or web interface
2. Click "Register New User"
3. Create an admin account with role "admin"
4. Use this account to manage the system

### 2. Add Your First Patient

1. Navigate to the Patients section
2. Click "Add Patient"
3. Fill in the required information:
   - Patient ID (unique identifier)
   - First and Last Name
   - Contact information
   - Medical information
4. Save the patient record

### 3. Test AI Features

1. Go to the AI Insights section
2. Select a patient
3. Choose an analysis type:
   - Relationship Analysis
   - Health Trend Analysis
   - Risk Assessment
   - Medication Review
4. Generate AI insights

## 📱 Features Overview

### Desktop GUI Application
- **Modern Interface**: Built with CustomTkinter for a professional look
- **Patient Management**: Full CRUD operations with encrypted data
- **Document Management**: Upload and manage PDFs, Word docs, images
- **AI Integration**: Real-time AI insights and recommendations
- **Dashboard**: Comprehensive statistics and activity monitoring

### Web Interface
- **Mobile Responsive**: Works on phones, tablets, and desktops
- **Real-time Updates**: Live data synchronization
- **Secure Authentication**: JWT-based security
- **API Integration**: Full REST API access

### AI Features
- **Patient Relationship Analysis**: AI-powered relationship scoring
- **Health Trend Analysis**: Identify patterns in patient data
- **Risk Assessment**: Automated risk evaluation
- **Medication Reviews**: AI-assisted medication analysis
- **Sentiment Analysis**: Analyze patient interaction sentiment

### Security Features
- **Data Encryption**: All sensitive data encrypted at rest
- **HIPAA Compliance**: Audit logging and access controls
- **Secure Authentication**: JWT tokens with expiration
- **Role-based Access**: Provider, Admin, and Nurse roles

## 🔒 Security Best Practices

### Production Deployment

1. **Change Default Secrets**:
   ```env
   SECRET_KEY=generate-a-secure-random-key-here
   ENCRYPTION_KEY=generate-a-32-character-key-here
   ```

2. **Use PostgreSQL**:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/health_admin
   ```

3. **Enable HTTPS**: Use a reverse proxy like Nginx with SSL certificates

4. **Regular Backups**: Set up automated database backups

5. **Monitor Logs**: Review audit logs regularly for suspicious activity

### HIPAA Compliance

- All patient data is encrypted using AES-256
- Comprehensive audit logging for all data access
- Role-based access controls
- Secure authentication and session management
- Data retention policies can be implemented

## 🐛 Troubleshooting

### Common Issues

#### 1. Ollama Connection Error
```
Error: Could not connect to Ollama server
```
**Solution**: 
- Ensure Ollama is running: `ollama serve`
- Check if the model is installed: `ollama list`
- Verify the OLLAMA_BASE_URL in .env

#### 2. Database Connection Error
```
Error: Database connection failed
```
**Solution**:
- Check DATABASE_URL in .env file
- Ensure database file permissions (SQLite)
- Verify PostgreSQL connection (if using PostgreSQL)

#### 3. GUI Won't Start
```
Error: ImportError: No module named 'customtkinter'
```
**Solution**:
- Install dependencies: `pip install -r requirements.txt`
- Activate virtual environment
- Check Python version (3.8+ required)

#### 4. AI Analysis Fails
```
Error: AI analysis service temporarily unavailable
```
**Solution**:
- Check Ollama server status
- Verify model is loaded: `ollama list`
- Check system RAM (8GB+ recommended)
- Try a smaller model if RAM is limited

### Performance Optimization

#### For Better AI Performance:
- Use a model with more parameters (13B or 70B) if you have sufficient RAM
- Close other applications to free up memory
- Use SSD storage for faster model loading

#### For Better Database Performance:
- Use PostgreSQL instead of SQLite for production
- Add database indexes for frequently queried fields
- Regular database maintenance and cleanup

## 📞 Support

### Getting Help

1. **Check Logs**: Look at console output for error messages
2. **Verify Prerequisites**: Ensure all required software is installed
3. **Test Components**: Try starting backend and GUI separately
4. **Check Configuration**: Verify .env file settings

### System Requirements Check

```bash
# Check Python version
python --version

# Check if Ollama is running
ollama list

# Check if dependencies are installed
pip list | grep -E "(fastapi|customtkinter|sqlalchemy)"
```

## 🎯 Next Steps

After successful setup:

1. **Create User Accounts**: Set up accounts for all healthcare providers
2. **Import Patient Data**: Add existing patient records
3. **Configure AI Models**: Experiment with different models for your use case
4. **Set Up Backups**: Implement regular data backups
5. **Train Staff**: Familiarize your team with the interface
6. **Monitor Usage**: Review audit logs and system performance

## 📚 Additional Resources

- **API Documentation**: http://localhost:8000/api/docs
- **Ollama Documentation**: https://ollama.ai/docs
- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **CustomTkinter Documentation**: https://customtkinter.tomschimansky.com/

---

**Congratulations!** You now have a fully functional AI-powered healthcare administrative system. The system is designed to grow with your needs and can be customized for specific healthcare workflows.
