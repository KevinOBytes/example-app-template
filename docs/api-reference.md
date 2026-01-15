# API Reference

## Overview

The AI Agent Application provides a RESTful API built with FastAPI. All endpoints return JSON responses and follow consistent patterns for error handling and status codes.

## Base URL

- **Local Development**: `http://localhost:8000`
- **Docker**: `http://localhost:8000`
- **Production**: Configure with your domain

## API Documentation

Interactive API documentation is available at:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Authentication

Currently, the template does not enforce authentication by default. To add authentication:

1. Implement JWT token generation
2. Add authentication middleware
3. Protect routes with dependencies

Example:
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

security = HTTPBearer()

async def verify_token(credentials = Depends(security)):
    # Verify JWT token
    pass
```

## Common Response Formats

### Success Response
```json
{
  "status": "success",
  "result": { ... },
  "timestamp": "2024-01-13T18:00:00Z"
}
```

### Error Response
```json
{
  "status": "error",
  "detail": "Error message",
  "timestamp": "2024-01-13T18:00:00Z"
}
```

## Endpoints

### Root Endpoints

#### `GET /`

Get root endpoint information.

**Response**
```json
{
  "message": "AI Agent Application is running",
  "version": "1.0.0",
  "timestamp": "2024-01-13T18:00:00.000Z"
}
```

**Status Codes**
- `200 OK`: Success

---

#### `GET /health`

Health check endpoint for monitoring and Docker health checks.

**Response**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-13T18:00:00.000Z",
  "environment": "development"
}
```

**Status Codes**
- `200 OK`: Application is healthy
- `503 Service Unavailable`: Application is unhealthy

---

#### `GET /info`

Get application information and configuration.

**Response**
```json
{
  "app_name": "ai-agent-app",
  "environment": "development",
  "debug": true,
  "agent_config": {
    "max_iterations": 10,
    "timeout": 300,
    "model": "gpt-4",
    "temperature": 0.7
  }
}
```

**Status Codes**
- `200 OK`: Success

---

### Agent Endpoints

#### `POST /api/v1/agent/execute`

Execute an agent task.

**Request Body**
```json
{
  "task": "Analyze the sentiment of this text",
  "context": {
    "source": "user_input",
    "metadata": {}
  },
  "agent_config": {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_iterations": 10
  }
}
```

**Parameters**
- `task` (string, required): Task description or query
- `context` (object, optional): Additional context for the task
- `agent_config` (object, optional): Override default agent configuration
  - `model` (string): AI model to use
  - `temperature` (float): Model temperature (0.0-2.0)
  - `max_iterations` (integer): Maximum iterations (1-100)
  - `timeout` (integer): Timeout in seconds (1-3600)

**Response**
```json
{
  "status": "success",
  "result": {
    "status": "success",
    "task": "Analyze the sentiment of this text",
    "response": "Processed task: Analyze the sentiment of this text",
    "agent": "sample-agent",
    "model": "gpt-4",
    "context_provided": true,
    "timestamp": "2024-01-13T18:00:00.000Z"
  }
}
```

**Status Codes**
- `200 OK`: Task executed successfully
- `400 Bad Request`: Invalid request parameters
- `500 Internal Server Error`: Execution error

**Example**
```bash
curl -X POST http://localhost:8000/api/v1/agent/execute \
  -H "Content-Type: application/json" \
  -d '{
    "task": "Summarize this document",
    "context": {
      "document_id": "12345"
    }
  }'
```

---

#### `GET /api/v1/agent/history`

Get agent execution history.

**Response**
```json
{
  "status": "success",
  "count": 5,
  "history": [
    {
      "timestamp": "2024-01-13T18:00:00.000Z",
      "agent": "sample-agent",
      "task": "Previous task",
      "result": { ... },
      "duration": 1.23,
      "model": "gpt-4"
    }
  ]
}
```

**Status Codes**
- `200 OK`: Success
- `500 Internal Server Error`: Error retrieving history

**Example**
```bash
curl http://localhost:8000/api/v1/agent/history
```

---

#### `POST /api/v1/agent/analyze`

Analyze data using the agent.

**Request Body**
```json
{
  "data": "Text to analyze"
}
```

**Parameters**
- `data` (string, required): Data to analyze

**Response**
```json
{
  "status": "success",
  "result": {
    "status": "success",
    "task": "Analyze: Text to analyze",
    "response": "Processed task: Analyze: Text to analyze",
    "agent": "sample-agent",
    "model": "gpt-4",
    "context_provided": true,
    "timestamp": "2024-01-13T18:00:00.000Z"
  }
}
```

**Status Codes**
- `200 OK`: Analysis completed
- `400 Bad Request`: Invalid data
- `500 Internal Server Error`: Analysis error

**Example**
```bash
curl -X POST http://localhost:8000/api/v1/agent/analyze \
  -H "Content-Type: application/json" \
  -d '{"data": "This is a sample text to analyze"}'
```

---

#### `POST /api/v1/agent/generate`

Generate content using the agent.

**Request Body**
```json
{
  "prompt": "Write a haiku about coding"
}
```

**Parameters**
- `prompt` (string, required): Generation prompt

**Response**
```json
{
  "status": "success",
  "result": {
    "status": "success",
    "task": "Generate: Write a haiku about coding",
    "response": "Processed task: Generate: Write a haiku about coding",
    "agent": "sample-agent",
    "model": "gpt-4",
    "context_provided": true,
    "timestamp": "2024-01-13T18:00:00.000Z"
  }
}
```

**Status Codes**
- `200 OK`: Generation completed
- `400 Bad Request`: Invalid prompt
- `500 Internal Server Error`: Generation error

**Example**
```bash
curl -X POST http://localhost:8000/api/v1/agent/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Explain quantum computing"}'
```

---

## Data Models

### AgentTaskRequest

```python
{
  "task": str,           # Required
  "context": dict,       # Optional
  "agent_config": dict   # Optional
}
```

### AgentTaskResponse

```python
{
  "status": str,
  "result": dict
}
```

### Task

```python
{
  "id": str,              # Optional
  "description": str,     # Required
  "context": dict,        # Optional
  "status": str,          # "idle" | "running" | "completed" | "failed"
  "created_at": str,      # ISO datetime
  "completed_at": str,    # ISO datetime, optional
  "result": dict          # Optional
}
```

### AgentConfig

```python
{
  "name": str,
  "model": str,           # Default: "gpt-4"
  "temperature": float,   # 0.0-2.0, Default: 0.7
  "max_iterations": int,  # 1-100, Default: 10
  "timeout": int          # 1-3600, Default: 300
}
```

## Error Codes

| Status Code | Description |
|-------------|-------------|
| 200 | Success |
| 400 | Bad Request - Invalid parameters |
| 401 | Unauthorized - Authentication required |
| 403 | Forbidden - Insufficient permissions |
| 404 | Not Found - Resource doesn't exist |
| 422 | Unprocessable Entity - Validation error |
| 429 | Too Many Requests - Rate limit exceeded |
| 500 | Internal Server Error - Server error |
| 503 | Service Unavailable - Service down |

## Rate Limiting

Rate limiting is not enforced by default. To implement rate limiting:

1. Add rate limiting middleware
2. Configure limits per endpoint
3. Return 429 status code when exceeded

Example implementation:
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.get("/api/endpoint")
@limiter.limit("5/minute")
async def limited_endpoint(request: Request):
    return {"message": "Success"}
```

## Pagination

For endpoints returning lists, implement pagination:

**Query Parameters**
- `page` (integer): Page number (default: 1)
- `per_page` (integer): Items per page (default: 20, max: 100)

**Response Format**
```json
{
  "items": [...],
  "page": 1,
  "per_page": 20,
  "total": 100,
  "pages": 5
}
```

## Versioning

The API uses URL versioning:
- Current version: `/api/v1/`
- Future versions: `/api/v2/`, etc.

## CORS Configuration

CORS is enabled for all origins in development. For production:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
```

## WebSocket Support

WebSocket support can be added for real-time features:

```python
from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # Handle WebSocket communication
```

## Testing the API

### Using curl

```bash
# Health check
curl http://localhost:8000/health

# Execute task
curl -X POST http://localhost:8000/api/v1/agent/execute \
  -H "Content-Type: application/json" \
  -d '{"task": "Test task"}'
```

### Using Python

```python
import requests

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())

# Execute task
response = requests.post(
    "http://localhost:8000/api/v1/agent/execute",
    json={
        "task": "Analyze this data",
        "context": {"source": "api_test"}
    }
)
print(response.json())
```

### Using JavaScript/TypeScript

```javascript
// Health check
fetch('http://localhost:8000/health')
  .then(response => response.json())
  .then(data => console.log(data));

// Execute task
fetch('http://localhost:8000/api/v1/agent/execute', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    task: 'Analyze this data',
    context: { source: 'javascript_test' }
  })
})
  .then(response => response.json())
  .then(data => console.log(data));
```

## Best Practices

1. **Always handle errors**: Check response status codes
2. **Use appropriate HTTP methods**: GET for reads, POST for writes
3. **Include proper headers**: Content-Type, Authorization
4. **Validate input**: Use the provided models
5. **Log requests**: For debugging and monitoring
6. **Implement retries**: For transient failures
7. **Use timeouts**: Prevent hanging requests
8. **Cache responses**: When appropriate

## Support

For API questions or issues:
- Check the interactive documentation at `/docs`
- Review the examples in this document
- See the main README.md for additional resources
