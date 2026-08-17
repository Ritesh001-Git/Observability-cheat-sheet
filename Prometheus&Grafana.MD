# 🚀 Prometheus

**Prometheus** is an open-source monitoring and metrics platform widely used in Kubernetes environments.

It is a **CNCF project** and has strong integration with the Kubernetes ecosystem.

Prometheus can:

- Scrape metrics
- Store metrics
- Query metrics
- Provide an HTTP API/UI
- Work with exporters
- Discover monitoring targets
- Trigger alerts through Alertmanager

---

# 🏗️ Prometheus Architecture

High-level architecture:

```text
                   ┌────────────────────┐
                   │   Kubernetes / AWS  │
                   │     Resources       │
                   └─────────┬──────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Exporters     │
                    │                  │
                    │ Node Exporter    │
                    │ Kube-State-Metrics│
                    └────────┬─────────┘
                             │
                         Scrape/Pull
                             │
                             ▼
                    ┌──────────────────┐
                    │    Prometheus    │
                    │      Server      │
                    ├──────────────────┤
                    │ Retrieval/Scraper│
                    │ TSDB             │
                    │ HTTP Server      │
                    └───────┬──────────┘
                            │
               ┌────────────┴────────────┐
               ▼                         ▼
        ┌──────────────┐         ┌──────────────┐
        │   Grafana    │         │ Alertmanager │
        │  Dashboards  │         │    Alerts    │
        └──────────────┘         └──────────────┘
```

---

# 🧩 Main Prometheus Components

## 1. Prometheus Server

The main Prometheus component responsible for collecting, storing, and querying metrics.

### Important responsibilities:

- Scrapes metrics from targets
- Stores time-series data
- Provides query interface
- Exposes HTTP API
- Works with Alertmanager

---

## 2. Retrieval / Scraper

The retrieval component is responsible for **pulling/scraping metrics** from configured targets.

```text
Prometheus
    │
    │ Pull / Scrape
    ▼
Exporters / Applications
```

---

## 3. Time-Series Database (TSDB)

Prometheus stores metrics as **time-series data**.

Time is an important part of the stored data.

Conceptually:

```text
timestamp + metric + value + labels
```

Example:

```text
10:00 → CPU = 45%
10:01 → CPU = 52%
10:02 → CPU = 71%
10:03 → CPU = 85%
```

This allows you to analyze metrics over time.

---

## 4. HTTP Server

Prometheus exposes an HTTP interface through which users and tools can query metrics.

---

## 5. Alertmanager

**Alertmanager** handles alerts generated from Prometheus.

It can be configured to notify teams through different notification channels.

Example:

```text
CPU > 80%
     ↓
Prometheus Alert Rule
     ↓
Alertmanager
     ↓
Slack / Email / Notification
```

---

# 🔎 PromQL

**PromQL = Prometheus Query Language**

PromQL is used to query metrics stored in Prometheus.

### Example use cases:

- Get CPU utilization
- Query metrics for the last 30 minutes
- Filter metrics
- Aggregate metrics
- Analyze time-series data

Conceptually:

```text
User
  │
  │ PromQL Query
  ▼
Prometheus HTTP Server
  │
  ▼
Time-Series Database
  │
  ▼
Query Result
```

---

# 🔎 Service Discovery

Prometheus can use **Service Discovery** to automatically discover monitoring targets.

For example, if a Kubernetes cluster has 100 applications, Service Discovery can help Prometheus identify which applications should be scraped.

```text
Kubernetes
    │
    ▼
Service Discovery
    │
    ├── Application A
    ├── Application B
    ├── Application C
    └── Application D
             │
             ▼
        Prometheus
```

This avoids manually configuring every target.

---

# 🔌 Prometheus Exporters

An **exporter** is an add-on/component that exposes metrics in a format Prometheus can scrape.

Different exporters provide different types of metrics.

| Component | Purpose |
|---|---|
| Node Exporter | Infrastructure/node metrics |
| Kube-State-Metrics | Kubernetes object/state metrics |
| Application `/metrics` endpoint | Application metrics |
| Database Exporters | Database-specific metrics |

---

# 🖥️ Node Exporter

**Node Exporter** provides infrastructure-level metrics from Kubernetes nodes/VMs.

It can expose metrics such as:

- CPU utilization
- Memory utilization
- Disk utilization
- System-level information

Conceptually:

```text
Kubernetes Node / VM
        │
        ▼
  Node Exporter
        │
        │ Metrics
        ▼
   Prometheus
```

Node Exporter obtains system-level information from the node and exposes it for Prometheus to scrape.

---

# ☸️ Kube-State-Metrics

**Kube-State-Metrics (KSM)** exposes metrics about the state of Kubernetes resources.

It communicates with the **Kubernetes API Server**.

Examples of information:

- Pod status
- Deployment status
- Replica count
- Kubernetes resources
- Kubernetes object states
- Pod failures/events-related information

Architecture:

```text
Kubernetes API Server
          │
          ▼
  Kube-State-Metrics
          │
          │ Metrics
          ▼
     Prometheus
```

### Important distinction

**Node Exporter**

> Gets information from the underlying node/VM.

**Kube-State-Metrics**

> Gets Kubernetes resource/state information from the Kubernetes API Server.

---

# 📱 Application Metrics

Applications can expose their own metrics through a metrics endpoint.

A common pattern is:

```text
/metrics
```

For example:

```text
Application
     │
     └── /metrics
            │
            ▼
        Prometheus
```

Application metrics can include:

- HTTP request count
- HTTP request latency
- Error rate
- User signups
- User activity
- Business-specific metrics

Prometheus can use **Service Discovery** to find applications and scrape their `/metrics` endpoints.


# 📊 Grafana

**Grafana** is primarily used for **visualizing metrics**.

Prometheus + Grafana are commonly used together as a monitoring stack.

```text
Prometheus
    │
    │ Metrics
    ▼
 Grafana
    │
    ├── Graphs
    ├── Dashboards
    └── Visualizations
```

### Why Grafana?

Raw metrics can be difficult to understand.

Grafana converts metrics into:

- Graphs
- Charts
- Dashboards
- Panels
- Time-based visualizations

This makes system health easier to understand.

---

# 🚨 Alerting

Monitoring isn't only about visualization.

You can define rules such as:

```text
IF CPU > 80%
THEN trigger alert
```

Another example:

```text
IF HTTP latency > 10 seconds
multiple times
THEN notify development team
```

Alert flow:

```text
Metric
  ↓
Prometheus
  ↓
Alert Rule
  ↓
Alertmanager
  ↓
Notification
```

Possible notification destinations include:

- Slack
- Email
- Other notification systems

---

# ☸️ Installing Prometheus on Kubernetes

Prometheus can be installed on Kubernetes using **Helm**.

The example environment uses:

- AWS EKS
- Kubernetes
- Helm
- Prometheus
- Grafana
- Alertmanager

### Basic installation flow

```text
1. Create Kubernetes cluster
2. Configure required AWS/Kubernetes integration
3. Install/configure Helm
4. Add Prometheus Helm repository
5. Create monitoring namespace
6. Install Prometheus stack
7. Verify pods
8. Access Prometheus/Grafana/Alertmanager
```

---

## 📦 Monitoring Namespace

A dedicated namespace can be created for monitoring components:

```bash
kubectl create namespace monitoring
```

Prometheus and Grafana can then be installed into the `monitoring` namespace.

---

# 🔐 EKS + OIDC

When running Prometheus-related workloads in AWS EKS, an **OIDC provider** can be associated with the cluster.

This allows Kubernetes service accounts to interact with AWS IAM roles/policies through **IAM Roles for Service Accounts (IRSA)**.

Conceptually:

```text
Kubernetes Service Account
          │
          ▼
      OIDC Provider
          │
          ▼
       IAM Role
          │
          ▼
     AWS Services
```

---

# 🌐 Accessing Prometheus Locally

For learning/testing, Kubernetes **port forwarding** can be used instead of exposing services through Ingress.

Example pattern:

```bash
kubectl port-forward ...
```

This allows access to services such as:

- Prometheus UI
- Grafana
- Alertmanager

For production environments, an **Ingress + Ingress Controller** can be used instead of temporary port forwarding.

---

# 🔗 Prometheus + Grafana Integration

Grafana can use Prometheus as a **data source**.

High-level flow:

```text
Prometheus
    │
    │ Metrics
    ▼
 Grafana
    │
    ▼
Dashboards
```

To integrate them:

1. Open Grafana
2. Add a new data source
3. Select Prometheus
4. Provide the Prometheus URL
5. Save/test the connection
6. Build or use dashboards

---

# 🧠 Three Primary Metric Sources

For a Kubernetes-based environment, remember these three important sources:

| Source | Metrics |
|---|---|
| **Node Exporter** | Infrastructure/node metrics |
| **Kube-State-Metrics** | Kubernetes resource/state metrics |
| **Application `/metrics`** | Application-specific metrics |

### Easy way to remember

```text
Node Exporter
     ↓
Infrastructure

Kube-State-Metrics
     ↓
Kubernetes

/metrics
     ↓
Application
```

Prometheus scrapes metrics from all of these sources.

---

# 🔄 Complete Monitoring Flow

```text
                  ┌───────────────────────┐
                  │      AWS / Nodes      │
                  └───────────┬───────────┘
                              │
                              ▼
                       Node Exporter
                              │
                              │
Kubernetes API ──────► Kube-State-Metrics
                              │
                              │
Application ─────────► /metrics endpoint
                              │
                              ▼
                    ┌──────────────────┐
                    │    Prometheus    │
                    │                  │
                    │ Scrape           │
                    │ Store            │
                    │ Query            │
                    └───────┬──────────┘
                            │
                ┌───────────┴───────────┐
                ▼                       ▼
             Grafana              Alertmanager
                │                       │
                ▼                       ▼
           Dashboards              Notifications
```

---

# ⚔️ Prometheus Alternatives

Some alternatives/competitors mentioned include:

- Nagios
- InfluxDB
- Graphite

Prometheus is especially popular in Kubernetes environments because of its strong Kubernetes/CNCF ecosystem integration.
