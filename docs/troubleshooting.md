# Troubleshooting Guide

## Common Issues

### Docker Issues

**Docker daemon not running:**
```bash
# Check status
docker info

# Start Docker Desktop (Windows/Mac) or:
sudo systemctl start docker  # Linux
```

**Out of disk space:**
```bash
docker system prune -a  # Remove unused images/containers
docker system df         # Check disk usage
```

**Port already in use:**
```bash
# Find the process
lsof -i :8080           # Linux/Mac
netstat -ano | findstr :8080  # Windows

# Change the port in docker-compose.yml or stop the conflicting process
```

### Git Issues

**Permission denied:**
```bash
# Check SSH key
ssh -T git@github.com

# Or use HTTPS instead of SSH
git remote set-url origin https://github.com/...
```

### Validation Script Fails

1. Read the FAIL message and hint carefully
2. Re-do the specific step mentioned
3. Check the module README for the exact commands
4. Make sure you are in the correct directory
5. Verify all prerequisites from previous modules

## Getting Help

1. Check this troubleshooting guide first
2. Search the module README for your error
3. Check docs/interview-questions.md for concept clarification
4. Open an issue on this repository with:
   - Module number
   - Exact error message
   - Steps you took
   - Your OS and Docker version
