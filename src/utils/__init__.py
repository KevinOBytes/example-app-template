"""
Utility functions for the AI Agent Application.
"""
import logging
from typing import Dict, Any, Optional
from datetime import datetime
import json


def setup_logging(log_level: str = "INFO", log_format: str = "json") -> logging.Logger:
    """
    Set up application logging.
    
    Args:
        log_level: Logging level
        log_format: Log format (json or text)
        
    Returns:
        Configured logger
    """
    logger = logging.getLogger("ai-agent-app")
    logger.setLevel(getattr(logging, log_level.upper()))
    
    handler = logging.StreamHandler()
    if log_format == "json":
        formatter = logging.Formatter(
            '{"timestamp": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}'
        )
    else:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger


def validate_api_keys(config: Dict[str, Any]) -> Dict[str, bool]:
    """
    Validate that required API keys are configured.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        Dictionary of API key validation results
    """
    api_keys = {
        "openai": config.get("OPENAI_API_KEY"),
        "anthropic": config.get("ANTHROPIC_API_KEY"),
        "google": config.get("GOOGLE_API_KEY"),
    }
    
    return {
        key: value is not None and len(value) > 0 and value != f"your_{key}_api_key_here"
        for key, value in api_keys.items()
    }


def format_timestamp(dt: Optional[datetime] = None) -> str:
    """
    Format datetime as ISO string.
    
    Args:
        dt: Datetime to format (default: now)
        
    Returns:
        ISO formatted timestamp string
    """
    if dt is None:
        dt = datetime.utcnow()
    return dt.isoformat()


def safe_json_loads(json_str: str, default: Any = None) -> Any:
    """
    Safely load JSON string with error handling.
    
    Args:
        json_str: JSON string to parse
        default: Default value if parsing fails
        
    Returns:
        Parsed JSON or default value
    """
    try:
        return json.loads(json_str)
    except (json.JSONDecodeError, TypeError):
        return default
