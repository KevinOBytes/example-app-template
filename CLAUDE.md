# Claude AI Assistant - Project Context and Guidelines

## Project Context

This is an AI Agent Application Template designed for building intelligent agent-based applications using Python, Docker, and Windmill. The template provides a foundation for creating, deploying, and orchestrating AI agents that can perform various tasks.

## Architecture Overview

The application follows a modular architecture:

```
├── src/
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration management
│   ├── agents/              # AI agent implementations
│   │   ├── base_agent.py    # Abstract base class for agents
│   │   └── sample_agent.py  # Example agent implementation
│   ├── api/                 # API routes and endpoints
│   │   └── routes.py        # FastAPI route definitions
│   ├── models/              # Pydantic data models
│   └── utils/               # Utility functions
├── docs/                    # Documentation and diagrams
├── Dockerfile               # Container definition
└── docker-compose.yml       # Multi-container orchestration
```

## Key Design Patterns

### 1. Agent Pattern
All agents inherit from `BaseAgent` which provides:
- Common initialization and configuration
- Execution tracking and history
- Logging and monitoring hooks
- Abstract interface for custom implementations

### 2. Configuration Management
Using Pydantic Settings for:
- Type-safe configuration
- Environment variable loading
- Validation and defaults
- Easy testing and mocking

### 3. API Design
RESTful API with:
- Clear request/response models
- Proper error handling
- OpenAPI/Swagger documentation
- Async operations for performance

## When Assisting with This Project

### Understanding the Codebase

1. **Agent Development**
   - Check `src/agents/base_agent.py` for the interface
   - See `src/agents/sample_agent.py` for implementation example
   - Agents should be stateless when possible
   - Use async/await for I/O operations

2. **API Endpoints**
   - Routes are defined in `src/api/routes.py`
   - All endpoints should have proper error handling
   - Use Pydantic models for validation
   - Include docstrings and OpenAPI tags

3. **Configuration**
   - Settings are in `src/config.py`
   - Environment variables in `.env` (not committed)
   - Example configuration in `.env.example`
   - Use `settings` singleton for access

### Code Suggestions

When suggesting code changes:

1. **Follow existing patterns**
   - Match the style and structure of existing code
   - Use the same import conventions
   - Follow the established error handling approach

2. **Maintain type safety**
   - Include type hints for all functions
   - Use Pydantic models for data validation
   - Leverage Optional, Dict, List from typing

3. **Consider async context**
   - Use `async def` for I/O operations
   - Use `await` for async function calls
   - Consider concurrency implications

4. **Include documentation**
   - Add docstrings to new functions/classes
   - Update README.md if adding features
   - Update INSTRUCTIONS.md for developer workflow changes

### Common Tasks and How to Help

#### Adding a New Agent

```python
# Template for new agent
from src.agents.base_agent import BaseAgent
from typing import Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)

class MyCustomAgent(BaseAgent):
    def __init__(self, **kwargs):
        super().__init__(name="my-custom-agent", **kwargs)
        # Custom initialization
    
    async def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute custom agent logic.
        
        Args:
            task: Task description
            context: Optional context data
            
        Returns:
            Execution result dictionary
        """
        try:
            # Implement agent logic here
            result = {"status": "success", "data": "..."}
            return result
        except Exception as e:
            logger.error(f"Error in agent execution: {str(e)}")
            return {"status": "error", "error": str(e)}
```

#### Adding API Endpoints

```python
@router.post("/my-endpoint")
async def my_endpoint(request: MyRequestModel):
    """
    Endpoint description.
    
    Args:
        request: Request model with validated data
        
    Returns:
        Response with results
    """
    try:
        # Process request
        result = await some_async_operation(request)
        return {"status": "success", "result": result}
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
```

#### Configuration Changes

1. Add to `src/config.py` Settings class
2. Add to `.env.example` with documentation
3. Use in code via `settings.NEW_VARIABLE`

### Integration Points

#### Windmill Workflows
- Windmill runs on port 8080
- Can call application API endpoints
- Use for orchestration and scheduling
- Python scripts can import application modules

#### Docker Environment
- Application runs on port 8000
- PostgreSQL on port 5432
- Redis on port 6379
- All services on `ai-agent-network`

#### External APIs
- OpenAI for GPT models
- Anthropic for Claude models
- Google for other AI services
- Configure keys in `.env`

## Error Handling Philosophy

1. **Be specific with exceptions**
   - Catch specific exception types
   - Don't use bare `except:` clauses
   - Log with appropriate context

2. **Return structured errors**
   - Use consistent error response format
   - Include error type and message
   - Add context when helpful

3. **Fail gracefully**
   - Provide meaningful error messages
   - Don't expose internal details in production
   - Log full details for debugging

## Performance Considerations

1. **Use async for I/O**
   - Database queries
   - API calls
   - File operations

2. **Implement caching**
   - Use Redis for session/temporary data
   - Cache expensive computations
   - Set appropriate TTLs

3. **Monitor resource usage**
   - Log execution times
   - Track agent iterations
   - Monitor memory usage

## Security Considerations

1. **Never log secrets**
   - API keys
   - Tokens
   - Passwords

2. **Validate all input**
   - Use Pydantic models
   - Check bounds and formats
   - Sanitize user input

3. **Use secure defaults**
   - HTTPS in production
   - Strong secret keys
   - Limited CORS origins

## Testing Guidance

When writing tests:
- Use pytest and pytest-asyncio
- Mock external services
- Test both success and failure paths
- Include edge cases
- Use fixtures for common setup

Example test structure:
```python
import pytest
from src.agents.sample_agent import SampleAgent

@pytest.mark.asyncio
async def test_sample_agent_execute():
    agent = SampleAgent()
    result = await agent.execute("test task")
    assert result["status"] == "success"
    assert "response" in result
```

## Deployment Checklist

When helping with deployment:
1. Verify all secrets are in environment variables
2. Check APP_ENV is set to "production"
3. Ensure APP_DEBUG is False
4. Confirm database migrations are current
5. Verify health checks are passing
6. Test external API connectivity
7. Review logs for errors

## Common Questions and Answers

**Q: How do I add a new AI model provider?**
A: Add API key to config, create new agent class, implement execute method, add to routes.

**Q: How do I scale the application?**
A: Use Docker Compose scale or Kubernetes, ensure stateless design, use Redis for shared state.

**Q: How do I debug agent execution?**
A: Check execution history via `/api/v1/agent/history`, review logs, use DEBUG log level.

**Q: How do I integrate with Windmill?**
A: Create Windmill workflow that calls app API endpoints, pass data as JSON, handle responses.

## Best Practices Summary

✅ DO:
- Use type hints and Pydantic models
- Write docstrings and documentation
- Handle errors gracefully
- Use async for I/O operations
- Log important events
- Keep agents focused and modular
- Test thoroughly

❌ DON'T:
- Commit secrets or .env files
- Use blocking I/O in async functions
- Ignore errors silently
- Create tightly coupled components
- Skip validation
- Log sensitive data
- Mix business logic with API routes

## How to Use This File

This file serves as a reference for Claude AI when:
1. Reviewing code in this project
2. Suggesting improvements or changes
3. Answering questions about architecture
4. Helping debug issues
5. Assisting with new feature development

Always consider the patterns and principles outlined here when providing assistance with this codebase.
