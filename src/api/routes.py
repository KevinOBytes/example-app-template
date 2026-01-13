"""
API Routes for the AI Agent Application.
"""
from fastapi import APIRouter, HTTPException, Body
from typing import Dict, Any, Optional
from pydantic import BaseModel
import logging

from src.agents.sample_agent import SampleAgent

logger = logging.getLogger(__name__)
router = APIRouter()


class AgentTaskRequest(BaseModel):
    """Request model for agent tasks."""
    task: str
    context: Optional[Dict[str, Any]] = None
    agent_config: Optional[Dict[str, Any]] = None


class AgentTaskResponse(BaseModel):
    """Response model for agent tasks."""
    status: str
    result: Dict[str, Any]


@router.post("/agent/execute", response_model=AgentTaskResponse)
async def execute_agent_task(request: AgentTaskRequest):
    """
    Execute an agent task.
    
    Args:
        request: Agent task request with task description and optional context
        
    Returns:
        Task execution result
    """
    try:
        logger.info(f"Received agent task: {request.task}")
        
        # Initialize agent with custom config if provided
        agent_config = request.agent_config or {}
        agent = SampleAgent(**agent_config)
        
        # Execute the task
        result = await agent.execute(request.task, request.context)
        
        return AgentTaskResponse(
            status="success",
            result=result
        )
    except Exception as e:
        logger.error(f"Error executing agent task: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/agent/history")
async def get_agent_history():
    """
    Get agent execution history.
    
    Returns:
        List of agent execution records
    """
    try:
        agent = SampleAgent()
        history = agent.get_execution_history()
        return {
            "status": "success",
            "count": len(history),
            "history": history
        }
    except Exception as e:
        logger.error(f"Error retrieving agent history: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/agent/analyze")
async def analyze_data(data: str = Body(..., embed=True)):
    """
    Analyze data using the agent.
    
    Args:
        data: Data to analyze
        
    Returns:
        Analysis results
    """
    try:
        agent = SampleAgent()
        result = await agent.analyze(data)
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        logger.error(f"Error analyzing data: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/agent/generate")
async def generate_content(prompt: str = Body(..., embed=True)):
    """
    Generate content using the agent.
    
    Args:
        prompt: Generation prompt
        
    Returns:
        Generated content
    """
    try:
        agent = SampleAgent()
        result = await agent.generate(prompt)
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        logger.error(f"Error generating content: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
