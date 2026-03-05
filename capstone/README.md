# Capstone: Production Kubernetes Operator

Build a complete operator that manages a custom application lifecycle:

## Requirements
- [ ] CRD with validation, status subresource, and printer columns
- [ ] Controller with create, update, delete reconciliation
- [ ] Deployment, Service, and ConfigMap management
- [ ] Status reporting with conditions
- [ ] RBAC configuration
- [ ] Helm chart or OLM bundle for distribution
- [ ] Unit and integration tests
- [ ] CI pipeline that builds and tests the operator

## Architecture
```
MyApp CR → Operator Controller → Creates:
  - Deployment (manages pods)
  - Service (network access)
  - ConfigMap (configuration)
  - HPA (autoscaling)
```
