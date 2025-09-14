# Health Administrative Tool - Windows Setup Guide

## 🏥 AI-Powered Patient Management System

This guide will help you set up and run the Health Administrative Tool on Windows with your specific Python installation.

## 🚀 Quick Start (Recommended)

### Step 1: Install Dependencies
Double-click `install_dependencies.bat` to automatically install all required Python packages.

### Step 2: Setup AI (Ollama)
Double-click `setup_ollama.bat` to install and configure the AI model.

### Step 3: Start the Application
Double-click `start_health_admin.bat` to launch the complete system.

## 📋 Manual Setup (Alternative)

### Prerequisites
- **Python**: Located at `C:\Users\AGrac\AppData\Local\Programs\Python\Python313\python.exe`
- **Internet Connection**: Required for downloading AI models
- **RAM**: Minimum 8GB (16GB recommended for AI features)

### 1. Install Ollama
1. Go to [https://ollama.ai/download](https://ollama.ai/download)
2. Download the Windows installer
3. Run the installer
4. Open Command Prompt and run:
   ```cmd
   ollama pull llama2:8b
   ```

### 2. Install Python Dependencies
Open Command Prompt in the project directory and run:
```cmd
C:\Users\AGrac\AppData\Local\Programs\Python\Python313\python.exe -m pip install -r requirements.txt
```

### 3. Start the Application
```cmd
C:\Users\AGrac\AppData\Local\Programs\Python\Python313\python.exe start_gui.py
```

## 🎮 Available Batch Files

### `start_health_admin.bat` - Main Launcher
- **Purpose**: Starts the complete Health Administrative Tool
- **Features**: 
  - Checks Python installation
  - Verifies dependencies
  - Checks Ollama status
  - Launches GUI application
- **Usage**: Double-click to start

### `install_dependencies.bat` - Dependency Installer
- **Purpose**: Installs all required Python packages
- **Features**:
  - Creates virtual environment
  - Installs requirements
  - Tests imports
- **Usage**: Run once during initial setup

### `setup_ollama.bat` - AI Setup
- **Purpose**: Sets up Ollama and AI models
- **Features**:
  - Checks Ollama installation
  - Downloads llama2:8b model
  - Tests AI functionality
- **Usage**: Run once during initial setup

### `run_demo.bat` - System Demo
- **Purpose**: Runs a comprehensive system demonstration
- **Features**:
  - Creates demo data
  - Shows AI features
  - Demonstrates all capabilities
- **Usage**: Run to see the system in action

## 🔧 Configuration

### Environment File
The system will automatically create a `.env` file from `env.example`. You can edit this file to customize:
- Database settings
- Security keys
- AI model configuration
- Application settings

### Python Path
If your Python installation is different, edit the batch files and change:
```batch
set PYTHON_PATH=C:\Users\AGrac\AppData\Local\Programs\Python\Python313\python.exe
```
to your actual Python path.

## 🖥️ Access Points

Once running, you can access the system through:

- **Desktop GUI**: Automatically opens with the main launcher
- **Web Interface**: http://localhost:8000
- **API Documentation**: http://localhost:8000/api/docs
- **Mobile Interface**: http://localhost:8000 (responsive design)

## 🎯 Features

### Patient Management
- Secure patient records with encryption
- Document upload and management
- Medical history tracking
- Insurance information
- Emergency contacts

### AI-Powered Insights
- Patient relationship analysis
- Health trend identification
- Risk assessment
- Medication reviews
- Sentiment analysis

### Security & Compliance
- HIPAA-compliant audit logging
- Data encryption
- Role-based access control
- Secure authentication

### User Interfaces
- Modern desktop GUI
- Mobile-responsive web interface
- Real-time data synchronization
- Intuitive healthcare design

## 🐛 Troubleshooting

### Common Issues

#### "Python not found"
- Verify Python is installed at the specified path
- Update the `PYTHON_PATH` in batch files if needed

#### "Dependencies not installed"
- Run `install_dependencies.bat`
- Check internet connection
- Verify Python version (3.8+ required)

#### "Ollama not detected"
- Install Ollama from https://ollama.ai/download
- Run `setup_ollama.bat`
- Ensure Ollama service is running

#### "AI model not working"
- Check if llama2:8b model is installed: `ollama list`
- Pull the model: `ollama pull llama2:8b`
- Verify sufficient RAM (8GB+ recommended)

#### "Port 8000 already in use"
- Close other applications using port 8000
- Restart the application
- Check for other running instances

### Performance Tips

#### For Better AI Performance:
- Use a model with more parameters if you have sufficient RAM
- Close other applications to free up memory
- Use SSD storage for faster model loading

#### For Better Database Performance:
- Use PostgreSQL instead of SQLite for production
- Regular database maintenance
- Monitor disk space

## 📞 Support

### Getting Help
1. Check the console output for error messages
2. Verify all prerequisites are installed
3. Try running components separately
4. Check the `.env` configuration file

### System Requirements Check
```cmd
# Check Python version
C:\Users\AGrac\AppData\Local\Programs\Python\Python313\python.exe --version

# Check if Ollama is running
ollama list

# Check dependencies
C:\Users\AGrac\AppData\Local\Programs\Python\Python313\python.exe -c "import fastapi, customtkinter, sqlalchemy"
```

## 🎉 Success!

Once everything is set up, you'll have a fully functional AI-powered healthcare administrative system with:

- ✅ Secure patient data management
- ✅ AI-powered insights and recommendations
- ✅ Modern desktop and mobile interfaces
- ✅ Document management capabilities
- ✅ HIPAA-compliant security features
- ✅ Real-time dashboard and analytics

## 📚 Additional Resources

- **Setup Guide**: `SETUP_GUIDE.md` - Comprehensive installation instructions
- **Project Summary**: `PROJECT_SUMMARY.md` - Complete system overview
- **API Documentation**: Available at http://localhost:8000/api/docs when running

---

**Built with ❤️ for the future of healthcare technology**
