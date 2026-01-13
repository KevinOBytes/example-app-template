"""
Main FastAPI application entry point for AI Agent Application.
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from datetime import datetime, timezone

from src.config import settings
from src.agents.base_agent import BaseAgent
from src.api import routes

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager."""
    logger.info("Starting AI Agent Application...")
    logger.info(f"Environment: {settings.APP_ENV}")
    logger.info(f"Debug mode: {settings.APP_DEBUG}")
    yield
    logger.info("Shutting down AI Agent Application...")


# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    description="AI Agent Application Template with Docker and Windmill integration",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(routes.router, prefix="/api/v1")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "AI Agent Application is running",
        "version": "1.0.0",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/health")
async def health_check():
    """Health check endpoint for Docker and monitoring."""
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "environment": settings.APP_ENV
    }


@app.get("/info")
async def info():
    """Application information endpoint."""
    return {
        "app_name": settings.APP_NAME,
        "environment": settings.APP_ENV,
        "debug": settings.APP_DEBUG,
        "agent_config": {
            "max_iterations": settings.AGENT_MAX_ITERATIONS,
            "timeout": settings.AGENT_TIMEOUT,
            "model": settings.AGENT_MODEL,
            "temperature": settings.AGENT_TEMPERATURE
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=settings.APP_PORT,
        reload=settings.APP_DEBUG
    )
