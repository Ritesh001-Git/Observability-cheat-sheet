# 📈 Metrics
### What are Metrics?

Metrics are historical/periodic measurements of events or system behavior used to understand the health and performance of a system.

Examples:

- CPU utilization
- Memory utilization
- Disk utilization
- HTTP request count
- HTTP request latency
- Pod status
- Number of replicas
- Application signups
- User activity

### 🔍 Metrics vs Monitoring

This is an important distinction.

Metrics	Monitoring
Raw measurements/data	System/process that uses the data
Represents historical information	Collects, visualizes and evaluates metrics
Example: CPU = 85%	Dashboard showing CPU over time
Example: HTTP latency = 5s	Alert when latency exceeds a threshold
Data itself	Metrics + dashboards + alerts
In simple terms
Metrics
   ↓
Monitoring System
   ├── Dashboards
   └── Alerts

Monitoring is a superset of metrics.

A monitoring system can:

Collect/scrape metrics
Store metrics
Visualize metrics
Evaluate metrics
Trigger alerts
📊 Types of Metrics

Metrics can exist at different levels of a system.

1. Infrastructure Metrics

Used to monitor infrastructure such as AWS EC2 instances / Kubernetes nodes.

Examples:

CPU utilization
Memory utilization
Disk utilization
Network-related metrics
2. Kubernetes Metrics

Used to understand the health of the Kubernetes cluster.

Examples:

Pod status
Pod crashes
CrashLoopBackOff
Deployment status
Number of replicas
HPA replica count
Kubernetes events
3. Application Metrics

Used to monitor application behavior.

Examples:

HTTP requests
HTTP request latency
Request count
Error count
Application-specific business metrics
User signups
User deactivations
User activity
🔄 Monitoring Flow

Metrics can reach the monitoring system using two mechanisms:

Push

The application/system pushes metrics to the monitoring system.

Application
    │
    │ Push Metrics
    ▼
Monitoring System
Pull / Scrape

The monitoring system pulls metrics from the target.

Monitoring System
       │
       │ Scrape / Pull
       ▼
     Target

In Prometheus, pull/scrape is the commonly used mechanism.

Scraping = Pulling metrics from a target.
