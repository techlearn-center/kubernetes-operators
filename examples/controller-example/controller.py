"""
Simple Kubernetes Operator in Python using kopf.
This watches MyApp custom resources and creates Deployments + Services.
"""
import kopf
import kubernetes
import yaml

@kopf.on.create('example.com', 'v1', 'myapps')
def create_fn(spec, name, namespace, logger, **kwargs):
    """Called when a MyApp resource is created."""
    replicas = spec.get('replicas', 1)
    image = spec.get('image', 'nginx:latest')
    port = spec.get('port', 80)

    logger.info(f"Creating MyApp: {name} with {replicas} replicas of {image}")

    # Create Deployment
    deployment = {
        'apiVersion': 'apps/v1',
        'kind': 'Deployment',
        'metadata': {'name': name, 'namespace': namespace},
        'spec': {
            'replicas': replicas,
            'selector': {'matchLabels': {'app': name}},
            'template': {
                'metadata': {'labels': {'app': name}},
                'spec': {
                    'containers': [{
                        'name': name,
                        'image': image,
                        'ports': [{'containerPort': port}]
                    }]
                }
            }
        }
    }

    # Create Service
    service = {
        'apiVersion': 'v1',
        'kind': 'Service',
        'metadata': {'name': name, 'namespace': namespace},
        'spec': {
            'selector': {'app': name},
            'ports': [{'port': port, 'targetPort': port}],
            'type': 'ClusterIP'
        }
    }

    api = kubernetes.client.ApiClient()
    apps_api = kubernetes.client.AppsV1Api(api)
    core_api = kubernetes.client.CoreV1Api(api)

    kopf.adopt(deployment)
    kopf.adopt(service)

    apps_api.create_namespaced_deployment(namespace, deployment)
    core_api.create_namespaced_service(namespace, service)

    return {'message': f'Created deployment and service for {name}'}


@kopf.on.update('example.com', 'v1', 'myapps')
def update_fn(spec, name, namespace, logger, **kwargs):
    """Called when a MyApp resource is updated."""
    replicas = spec.get('replicas', 1)
    image = spec.get('image', 'nginx:latest')

    logger.info(f"Updating MyApp: {name} to {replicas} replicas of {image}")

    api = kubernetes.client.AppsV1Api()
    patch = {
        'spec': {
            'replicas': replicas,
            'template': {
                'spec': {
                    'containers': [{'name': name, 'image': image}]
                }
            }
        }
    }
    api.patch_namespaced_deployment(name, namespace, patch)
    return {'message': f'Updated {name}'}


@kopf.on.delete('example.com', 'v1', 'myapps')
def delete_fn(name, namespace, logger, **kwargs):
    """Called when a MyApp resource is deleted. Children auto-deleted via ownership."""
    logger.info(f"MyApp {name} deleted. Owned resources will be garbage collected.")
