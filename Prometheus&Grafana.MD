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
