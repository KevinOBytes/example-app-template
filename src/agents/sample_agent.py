"""
Sample Agent implementation demonstrating agent pattern.
"""
from typing import Dict, Any, Optional
import asyncio
from datetime import datetime
import logging

from src.agents.base_agent import BaseAgent
from src.config import settings

logger = logging.getLogger(__name__)


class SampleAgent(BaseAgent):
    """
    Sample agent implementation that demonstrates how to create custom agents.
    This agent can be extended with actual AI model integration.
    """
    
    def __init__(self, **kwargs):
        """Initialize the sample agent."""
        super().__init__(
            name="sample-agent",
            model=kwargs.get("model", settings.AGENT_MODEL),
            temperature=kwargs.get("temperature", settings.AGENT_TEMPERATURE),
            max_iterations=kwargs.get("max_iterations", settings.AGENT_MAX_ITERATIONS),
            timeout=kwargs.get("timeout", settings.AGENT_TIMEOUT)
        )
    
    async def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute the sample agent task.
        
        Args:
            task: Task description or query
            context: Optional context dictionary
            
        Returns:
            Dictionary containing execution results
        """
        start_time = datetime.utcnow()
        logger.info(f"Executing task: {task}")
        
        try:
            # Simulate some processing
            await asyncio.sleep(0.5)
            
            # Process the task (this is where you'd integrate with actual AI models)
            result = {
                "status": "success",
                "task": task,
                "response": f"Processed task: {task}",
                "agent": self.name,
                "model": self.model,
                "context_provided": context is not None,
                "timestamp": datetime.utcnow().isoformat()
            }
            
            # Add context information if provided
            if context:
                result["context_keys"] = list(context.keys())
            
            # Log execution
            duration = (datetime.utcnow() - start_time).total_seconds()
            self.log_execution(task, result, duration)
            
            return result
            
        except Exception as e:
            logger.error(f"Error executing task: {str(e)}")
            duration = (datetime.utcnow() - start_time).total_seconds()
            error_result = {
                "status": "error",
                "task": task,
                "error": str(e),
                "timestamp": datetime.utcnow().isoformat()
            }
            self.log_execution(task, error_result, duration)
            return error_result
    
    async def analyze(self, data: str) -> Dict[str, Any]:
        """
        Analyze provided data.
        
        Args:
            data: Data to analyze
            
        Returns:
            Analysis results
        """
        return await self.execute(f"Analyze: {data}", {"operation": "analyze"})
    
    async def generate(self, prompt: str) -> Dict[str, Any]:
        """
        Generate content based on prompt.
        
        Args:
            prompt: Generation prompt
            
        Returns:
            Generated content
        """
        return await self.execute(f"Generate: {prompt}", {"operation": "generate"})
