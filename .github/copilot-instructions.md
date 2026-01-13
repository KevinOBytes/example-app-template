# GitHub Copilot Instructions for AI Agent Application

## Project Overview
This is an AI Agent Application template designed for Docker-based development with Windmill integration. The application is built using Python, FastAPI, and follows modern async patterns.

## Code Style and Conventions

### Python Style
- Follow PEP 8 style guidelines
- Use type hints for all function signatures
- Prefer async/await patterns for I/O operations
- Use Pydantic for data validation and settings management
- Keep functions focused and under 50 lines when possible

### Documentation
- All modules should have docstrings
- All public functions and classes should have docstrings
- Use Google-style docstrings format
- Include type information in docstrings

### Error Handling
- Use specific exception types
- Always log errors with appropriate context
- Return structured error responses from API endpoints
- Use try/except blocks for external service calls

## Architecture Patterns

### Agent Pattern
- All agents should inherit from `BaseAgent`
- Implement the `execute` method for agent logic
- Use dependency injection for configuration
- Log all agent executions for monitoring

### API Design
- Use FastAPI router pattern for organizing endpoints
- Implement request/response models with Pydantic
- Include proper HTTP status codes
- Add OpenAPI documentation for all endpoints

### Configuration
- Use environment variables for all configuration
- Provide sensible defaults
- Document all environment variables in .env.example
- Never commit secrets to version control

## Testing Guidelines
- Write tests for all business logic
- Use pytest and pytest-asyncio
- Mock external services
- Test both success and failure cases

## Docker Best Practices
- Use multi-stage builds when appropriate
- Run as non-root user
- Include health checks
- Minimize image layers
- Use .dockerignore to exclude unnecessary files

## Windmill Integration
- Use Windmill for workflow orchestration
- Keep workflows modular and reusable
- Document workflow inputs and outputs
- Handle workflow failures gracefully

## Security Considerations
- Never log sensitive data (API keys, tokens, passwords)
- Validate all input data
- Use parameterized queries for database operations
- Implement rate limiting for public endpoints
- Keep dependencies updated

## Suggested Improvements
When suggesting code improvements, consider:
1. Performance optimizations
2. Better error handling
3. Improved logging and monitoring
4. Code modularity and reusability
5. Test coverage
6. Documentation clarity

## Common Tasks

### Adding a New Agent
1. Create a new file in `src/agents/`
2. Inherit from `BaseAgent`
3. Implement the `execute` method
4. Add configuration to settings if needed
5. Register in `src/agents/__init__.py`
6. Add API endpoints in `src/api/routes.py`

### Adding a New API Endpoint
1. Define request/response models in `src/models/`
2. Add endpoint function in `src/api/routes.py`
3. Include proper error handling
4. Add documentation
5. Write tests

### Adding Environment Variables
1. Add to `src/config.py` Settings class
2. Document in `.env.example`
3. Update README.md if user-facing
4. Set defaults for development

## Code Review Checklist
- [ ] Code follows project style guidelines
- [ ] All functions have type hints and docstrings
- [ ] Error handling is implemented
- [ ] Logging is appropriate
- [ ] Tests are included (if applicable)
- [ ] Documentation is updated
- [ ] No secrets are committed
- [ ] Environment variables are documented
