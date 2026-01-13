"""
Base Agent class for AI agent implementations.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


class BaseAgent(ABC):
    """
    Base class for all AI agents in the application.
    Provides common functionality and interface for agent implementations.
    """
    
    def __init__(
        self,
        name: str,
        model: str = "gpt-4",
        temperature: float = 0.7,
        max_iterations: int = 10,
        timeout: int = 300
    ):
        """
        Initialize the base agent.
        
        Args:
            name: Agent name/identifier
            model: AI model to use
            temperature: Model temperature for response generation
            max_iterations: Maximum iterations for agent execution
            timeout: Timeout in seconds for agent execution
        """
        self.name = name
        self.model = model
        self.temperature = temperature
        self.max_iterations = max_iterations
        self.timeout = timeout
        self.execution_history: List[Dict[str, Any]] = []
        
        logger.info(f"Initialized agent: {name} with model: {model}")
    
    @abstractmethod
    async def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute the agent task.
        
        Args:
            task: Task description or query
            context: Optional context dictionary with additional information
            
        Returns:
            Dictionary containing execution results
        """
        pass
    
    def log_execution(self, task: str, result: Dict[str, Any], duration: float):
        """
        Log agent execution for debugging and monitoring.
        
        Args:
            task: Task that was executed
            result: Execution result
            duration: Execution duration in seconds
        """
        execution_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "agent": self.name,
            "task": task,
            "result": result,
            "duration": duration,
            "model": self.model
        }
        self.execution_history.append(execution_record)
        logger.info(f"Agent {self.name} executed task in {duration:.2f}s")
    
    def get_execution_history(self) -> List[Dict[str, Any]]:
        """
        Get agent execution history.
        
        Returns:
            List of execution records
        """
        return self.execution_history
    
    def clear_history(self):
        """Clear execution history."""
        self.execution_history.clear()
        logger.info(f"Cleared execution history for agent: {self.name}")
