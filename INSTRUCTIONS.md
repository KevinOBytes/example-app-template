# AI Agent Application Template - Developer Instructions

## Quick Start Guide

### Prerequisites
- Docker and Docker Compose installed
- Python 3.11+ (for local development)
- Git

### Initial Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd example-app-template
   ```

2. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual API keys and configuration
   ```

3. **Start with Docker Compose**
   ```bash
   docker-compose up -d
   ```

4. **Access the application**
   - Main API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Windmill: http://localhost:8080

## Development Workflow

### Local Development (without Docker)

1. **Set up Python environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run the application**
   ```bash
   python -m uvicorn src.main:app --reload --port 8000
   ```

3. **Run with debug mode**
   ```bash
   export APP_DEBUG=true
   export LOG_LEVEL=DEBUG
   python src/main.py
   ```

### Docker Development

1. **Build the image**
   ```bash
   docker-compose build
   ```

2. **View logs**
   ```bash
   docker-compose logs -f app
   ```

3. **Access container shell**
   ```bash
   docker-compose exec app bash
   ```

4. **Restart services**
   ```bash
   docker-compose restart app
   ```

## Creating Custom Agents

### Step 1: Define Your Agent Class

Create a new file in `src/agents/` (e.g., `custom_agent.py`):

```python
from src.agents.base_agent import BaseAgent
from typing import Dict, Any, Optional

class CustomAgent(BaseAgent):
    def __init__(self, **kwargs):
        super().__init__(name="custom-agent", **kwargs)
    
    async def execute(self, task: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        # Your agent logic here
        result = {
            "status": "success",
            "data": "processed data"
        }
        return result
```

### Step 2: Register Your Agent

Add to `src/agents/__init__.py`:
```python
from src.agents.custom_agent import CustomAgent
```

### Step 3: Add API Endpoints

Update `src/api/routes.py` to expose your agent:
```python
@router.post("/custom/execute")
async def execute_custom_agent(request: AgentTaskRequest):
    agent = CustomAgent()
    result = await agent.execute(request.task, request.context)
    return result
```

## Windmill Integration

### Creating a Windmill Workflow

1. Access Windmill UI at http://localhost:8080
2. Create a new workflow
3. Add Python script steps that call your API endpoints
4. Configure inputs and outputs
5. Test and deploy

### Example Windmill Script

```python
import requests

def main(task_description: str):
    response = requests.post(
        "http://app:8000/api/v1/agent/execute",
        json={"task": task_description}
    )
    return response.json()
```

## Testing

### Running Tests
```bash
pytest
```

### Running with Coverage
```bash
pytest --cov=src --cov-report=html
```

### Testing API Endpoints
```bash
# Health check
curl http://localhost:8000/health

# Execute agent task
curl -X POST http://localhost:8000/api/v1/agent/execute \
  -H "Content-Type: application/json" \
  -d '{"task": "Test task", "context": {}}'
```

## Configuration

### Environment Variables

Key environment variables (see `.env.example` for complete list):

- `APP_ENV`: Environment (development/production)
- `APP_PORT`: Application port (default: 8000)
- `OPENAI_API_KEY`: OpenAI API key for GPT models
- `ANTHROPIC_API_KEY`: Anthropic API key for Claude models
- `DATABASE_URL`: PostgreSQL connection string
- `REDIS_URL`: Redis connection string
- `WINDMILL_URL`: Windmill server URL

### Adding New Configuration

1. Add to `src/config.py` Settings class
2. Document in `.env.example`
3. Update this file if user-facing

## Deployment

### Docker Production Deployment

1. **Set production environment variables**
   ```bash
   export APP_ENV=production
   export APP_DEBUG=false
   ```

2. **Build production image**
   ```bash
   docker-compose -f docker-compose.yml build
   ```

3. **Deploy**
   ```bash
   docker-compose up -d
   ```

### Health Monitoring

The application includes health check endpoints:
- `/health`: Basic health check
- `/info`: Application information

## Troubleshooting

### Common Issues

1. **Port already in use**
   - Change `APP_PORT` in .env
   - Or stop conflicting service: `lsof -ti:8000 | xargs kill`

2. **Database connection errors**
   - Verify PostgreSQL is running: `docker-compose ps`
   - Check DATABASE_URL in .env

3. **Import errors**
   - Ensure you're in the project root
   - Verify virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

4. **Docker build failures**
   - Clear Docker cache: `docker-compose build --no-cache`
   - Check Docker daemon is running

## Best Practices

### Code Organization
- Keep agents focused on single responsibilities
- Use type hints consistently
- Write docstrings for all public interfaces
- Follow the existing project structure

### Security
- Never commit .env files
- Rotate API keys regularly
- Use environment variables for secrets
- Keep dependencies updated

### Performance
- Use async/await for I/O operations
- Implement caching where appropriate
- Monitor memory usage in production
- Use connection pooling for databases

## Getting Help

- Check the documentation in `/docs`
- Review GitHub Copilot instructions in `.github/copilot-instructions.md`
- See Claude-specific guidance in `CLAUDE.md`
- Refer to the architecture diagram in `/docs/architecture.md`

## Next Steps

1. Configure your API keys in `.env`
2. Review the sample agent implementation
3. Create your first custom agent
4. Set up Windmill workflows
5. Deploy to your environment
