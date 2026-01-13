# Security Policy

## Supported Versions

This template uses the latest stable versions of all dependencies with security patches applied.

| Component | Version | Status |
|-----------|---------|--------|
| Python | 3.11+ | ✅ Supported |
| FastAPI | 0.109.1 | ✅ Patched |
| aiohttp | 3.13.3 | ✅ Patched |
| python-multipart | 0.0.18 | ✅ Patched |

## Security Patches Applied

### aiohttp 3.13.3 (Updated from 3.9.1)
- **CVE**: Zip bomb vulnerability in HTTP Parser auto_decompress feature
  - Affected: <= 3.13.2
  - Fixed in: 3.13.3
  
- **CVE**: Denial of Service when parsing malformed POST requests
  - Affected: < 3.9.4
  - Fixed in: 3.9.4
  
- **CVE**: Directory traversal vulnerability
  - Affected: >= 1.0.5, < 3.9.2
  - Fixed in: 3.9.2

### FastAPI 0.109.1 (Updated from 0.109.0)
- **CVE**: Content-Type Header ReDoS (Regular Expression Denial of Service)
  - Affected: <= 0.109.0
  - Fixed in: 0.109.1

### python-multipart 0.0.18 (Updated from 0.0.6)
- **CVE**: Denial of Service via deformed multipart/form-data boundary
  - Affected: < 0.0.18
  - Fixed in: 0.0.18
  
- **CVE**: Content-Type Header ReDoS
  - Affected: <= 0.0.6
  - Fixed in: 0.0.7

## Reporting a Vulnerability

If you discover a security vulnerability in this template:

1. **Do NOT** open a public issue
2. Email the repository maintainer directly
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will respond within 48 hours and work on a fix as soon as possible.

## Security Best Practices

This template implements several security best practices:

### 1. Environment-Based Configuration
- ✅ Secrets stored in environment variables
- ✅ `.env` files excluded from version control
- ✅ `.env.example` provides template without secrets

### 2. Container Security
- ✅ Non-root user execution in Docker containers
- ✅ Minimal base images (Python slim)
- ✅ Multi-stage builds to reduce attack surface
- ✅ Regular dependency updates

### 3. Input Validation
- ✅ Pydantic models for all API inputs
- ✅ Type validation and constraints
- ✅ Sanitization of user input

### 4. API Security
- ✅ CORS configuration (adjust for production)
- ✅ Health check endpoints
- ✅ Structured error responses (no info leakage)

### 5. Dependency Management
- ✅ Pinned versions in requirements.txt
- ✅ Regular security audits
- ✅ Automated vulnerability scanning

## Recommended Production Security Enhancements

Before deploying to production, implement:

### 1. Authentication & Authorization
```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

security = HTTPBearer()

async def verify_token(credentials = Depends(security)):
    # Implement JWT verification
    pass
```

### 2. Rate Limiting
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.get("/api/endpoint")
@limiter.limit("5/minute")
async def limited_endpoint():
    pass
```

### 3. HTTPS/TLS
- Use TLS certificates (Let's Encrypt)
- Configure HTTPS in reverse proxy (nginx, Traefik)
- Redirect HTTP to HTTPS

### 4. Secret Management
- Use HashiCorp Vault, AWS Secrets Manager, or similar
- Rotate secrets regularly
- Never log secrets

### 5. Database Security
- Use connection pooling with limits
- Implement parameterized queries (SQLAlchemy does this)
- Regular backups with encryption
- Restrict database access by IP

### 6. Monitoring & Logging
- Implement centralized logging (ELK, Loki)
- Monitor for suspicious activity
- Set up alerts for security events
- Regular log analysis

### 7. Network Security
- Use private networks for internal services
- Implement firewall rules
- Restrict ports and protocols
- Use VPN for administrative access

## Security Checklist

Before deploying to production:

- [ ] Update all dependencies to latest secure versions
- [ ] Configure HTTPS/TLS
- [ ] Implement authentication and authorization
- [ ] Set up rate limiting
- [ ] Configure CORS properly (not allow_origins=["*"])
- [ ] Use secret management system
- [ ] Enable security headers (HSTS, CSP, X-Frame-Options)
- [ ] Set up monitoring and alerting
- [ ] Regular security audits
- [ ] Penetration testing
- [ ] Disaster recovery plan
- [ ] Incident response plan

## Dependency Updates

To check for security updates:

```bash
# Using pip-audit
pip install pip-audit
pip-audit

# Using safety
pip install safety
safety check
```

## Regular Maintenance

- Update dependencies monthly
- Review security advisories weekly
- Scan for vulnerabilities before each deployment
- Conduct security audits quarterly

## Additional Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [FastAPI Security Documentation](https://fastapi.tiangolo.com/tutorial/security/)
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)
- [Python Security](https://python.readthedocs.io/en/latest/library/security_warnings.html)

## Contact

For security concerns, please contact the repository maintainer.

---

**Last Updated**: January 2026  
**Security Audit**: All known vulnerabilities patched
