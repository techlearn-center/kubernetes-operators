# Module 02: Custom Resource Definitions (CRDs)

| | |
|---|---|
| **Time** | 4 hours |
| **Difficulty** | Intermediate |

---

## Hands-On Lab

### Exercise 1: Create a CRD

```bash
# Apply the CRD
kubectl apply -f examples/crd-example/myapp-crd.yaml

# Verify it exists
kubectl get crd myapps.example.com

# Create an instance
kubectl apply -f examples/crd-example/myapp-instance.yaml

# List MyApp resources
kubectl get myapps
kubectl get ma  # Short name

# Describe it
kubectl describe myapp demo-app
```

### Exercise 2: CRD Validation

Try creating an invalid resource:

```yaml
apiVersion: example.com/v1
kind: MyApp
metadata:
  name: bad-app
spec:
  replicas: 999  # Exceeds maximum of 10 - will be rejected!
  image: nginx
  port: 80
```

```bash
kubectl apply -f bad-app.yaml
# Error: spec.replicas must be <= 10
```

The OpenAPI schema validation in the CRD **prevents bad data** from being stored.

**Next: [Module 03 →](../03-controller-runtime-basics/)**
