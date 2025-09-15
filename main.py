from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager
from app.core.config import settings
from app.api import auth, patients, dashboard, chat, billing
from app.db.database import engine
from app.db import models
import uvicorn
import os

# Create database tables
models.Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan event handler"""
    # Startup
    print(f"🚀 Starting {settings.app_name} v{settings.app_version}")
    print(f"📊 API Documentation: http://localhost:8000/api/docs")
    print(f"🌐 Web Interface: http://localhost:8000")
    print(f"🤖 AI Model: {settings.ollama_model}")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down Health Administrative Tool")

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="A comprehensive healthcare administrative system with AI integration",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(auth.router, prefix="/api")
app.include_router(patients.router, prefix="/api")
app.include_router(dashboard.router, prefix="/api")
app.include_router(chat.router, prefix="/api")
app.include_router(billing.router, prefix="/api")

# Serve static files for web interface
if os.path.exists("web/static"):
    app.mount("/static", StaticFiles(directory="web/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main web interface"""
    if os.path.exists("web/index.html"):
        with open("web/index.html", "r") as f:
            return HTMLResponse(content=f.read())
    else:
        return HTMLResponse(content="""
        <html>
            <head>
                <title>Health Administrative Tool</title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 40px; }
                    .container { max-width: 800px; margin: 0 auto; }
                    .header { text-align: center; margin-bottom: 40px; }
                    .api-link { display: inline-block; margin: 10px; padding: 10px 20px; 
                               background: #007bff; color: white; text-decoration: none; 
                               border-radius: 5px; }
                    .api-link:hover { background: #0056b3; }
                </style>
            </head>
            <body>
                <div class="container">
                    <div class="header">
                        <h1>🏥 Health Administrative Tool</h1>
                        <p>AI-Powered Patient Management System</p>
                    </div>
                    <div style="text-align: center;">
                        <a href="/api/docs" class="api-link">API Documentation</a>
                        <a href="/api/redoc" class="api-link">API ReDoc</a>
                    </div>
                    <div style="margin-top: 40px;">
                        <h2>Features</h2>
                        <ul>
                            <li>🔐 Secure patient data management with encryption</li>
                            <li>🤖 AI-powered insights and recommendations</li>
                            <li>📱 Mobile-responsive web interface</li>
                            <li>🖥️ Desktop GUI application</li>
                            <li>📊 Patient relationship tracking</li>
                            <li>🔍 Advanced search and filtering</li>
                        </ul>
                    </div>
                </div>
            </body>
        </html>
        """)

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app_name": settings.app_name,
        "version": settings.app_version,
        "debug": settings.debug
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level="info"
    )
