"""
Data models for the AI Agent Application.
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
from datetime import datetime
from enum import Enum


class AgentStatus(str, Enum):
    """Agent execution status."""
    IDLE = "idle"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Task(BaseModel):
    """Task model."""
    id: Optional[str] = None
    description: str
    context: Optional[Dict[str, Any]] = None
    status: AgentStatus = AgentStatus.IDLE
    created_at: datetime = Field(default_factory=datetime.utcnow)
    completed_at: Optional[datetime] = None
    result: Optional[Dict[str, Any]] = None


class AgentConfig(BaseModel):
    """Agent configuration model."""
    name: str
    model: str = "gpt-4"
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_iterations: int = Field(default=10, ge=1, le=100)
    timeout: int = Field(default=300, ge=1, le=3600)


class ExecutionRecord(BaseModel):
    """Agent execution record model."""
    timestamp: datetime
    agent: str
    task: str
    result: Dict[str, Any]
    duration: float
    model: str


class HealthStatus(BaseModel):
    """Health check status model."""
    status: str
    timestamp: datetime
    environment: str
    components: Optional[Dict[str, bool]] = None
