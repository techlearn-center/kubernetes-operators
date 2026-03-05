# Module 01: Kubernetes API Fundamentals

| | |
|---|---|
| **Time** | 4 hours |
| **Difficulty** | Intermediate |
| **Prerequisites** | Basic Kubernetes knowledge, kubectl installed |

---

## Learning Objectives

- Understand the Kubernetes API server and resource model
- Use kubectl to interact with the API directly
- Understand API groups, versions, and resource types
- Explore the API with kubectl api-resources and api-versions

---

## Hands-On Lab

### Exercise 1: Explore the K8s API

```bash
# List all API resources
kubectl api-resources | head -20

# List API groups
kubectl api-versions

# Get raw API response
kubectl get pods -o json | jq '.items[0].metadata'

# Watch resources in real-time
kubectl get pods -w
```

### Exercise 2: Understand Resource Structure

Every Kubernetes resource has:

```yaml
apiVersion: apps/v1      # API group/version
kind: Deployment          # Resource type
metadata:                 # Name, namespace, labels, annotations
  name: myapp
  namespace: default
spec:                     # Desired state (what you want)
  replicas: 3
status:                   # Actual state (what K8s reports)
  availableReplicas: 3
```

The **controller pattern**: You declare desired state in `spec`, a controller watches for changes and reconciles `status` to match `spec`.

### Exercise 3: API Server Direct Access

```bash
# Start a proxy to the API server
kubectl proxy --port=8001 &

# Access the API directly
curl http://localhost:8001/api/v1/namespaces/default/pods
curl http://localhost:8001/apis/apps/v1/namespaces/default/deployments
```

---

## Self-Check Questions

1. What is the difference between `spec` and `status`?
2. What is a controller and what does reconciliation mean?
3. How do API groups organize resources?
4. What does `kubectl apply` do at the API level?

**Next: [Module 02 →](../02-custom-resource-definitions/)**
