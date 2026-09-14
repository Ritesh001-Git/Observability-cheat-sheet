# EFK Stack (Elasticsearch, Fluentbit, Kibana)
The EFK Stack is used for collecting, storing, and visualizing logs from applications running in Kubernetes.

## Workflow
```
Kubernetes Pods
      │
      │ Generate Logs
      ▼
Container Log Files
(/var/log/containers/)
      │
      ▼
Fluent Bit
      │
      │ Collects + Filters + Adds Kubernetes Metadata
      ▼
Elasticsearch
      │
      │ Stores + Indexes Logs
      ▼
Kibana
      │
      │ Searches + Visualizes Logs
      ▼
User / Developer
```

## How everything works together
### Kubernetes Pods
Your applications run inside Pods and continuously generate logs.

### Fluent Bit
Fluent Bit runs on every Kubernetes node, usually as a DaemonSet. It collects container logs from the node.

### Log Processing
Fluent Bit can filter logs and add Kubernetes information such as:
- Pod name
- Namespace
- Container name
- Labels

### Elasticsearch
Fluent Bit sends the processed logs to Elasticsearch. Elasticsearch stores and indexes the logs so they can be searched quickly.

### Kibana
Kibana connects to Elasticsearch and provides a web interface where you can:
- Search logs
- Filter logs
- View errors
- Create dashboards
- Analyze application behavior
