# 🔍 Logging overview
- Logging is crucial in any distributed system, especially in Kubernetes, to monitor application behavior, detect issues, and ensure the smooth functioning of microservices.


## 🚀 Importance:
- **Debugging**: Logs provide critical information when debugging issues in applications.
- **Auditing**: Logs serve as an audit trail, showing what actions were taken and by whom.
- **Performance** Monitoring: Analyzing logs can help identify performance bottlenecks.
- **Security**: Logs help in detecting unauthorized access or malicious activities.

## 🛠️ Tools Available for Logging in Kubernetes
- 🗂️ EFK Stack (Elasticsearch, Fluentbit, Kibana)
- 🗂️ EFK Stack (Elasticsearch, FluentD, Kibana)
- 🗂️ ELK Stack (Elasticsearch, Logstash, Kibana)
- 📊 Promtail + Loki + Grafana

## 📦 EFK Stack (Elasticsearch, Fluentbit, Kibana)
- EFK is a popular logging stack used to collect, store, and analyze logs in Kubernetes.
- **Elasticsearch**: Stores and indexes log data for easy retrieval.
- **Fluentbit**: A lightweight log forwarder that collects logs from different sources and sends them to Elasticsearch.
- **Kibana**: A visualization tool that allows users to explore and analyze logs stored in Elasticsearch.

# 🏠 Architecture
<img width="1000" height="800" alt="architecture" src="https://github.com/user-attachments/assets/f4d16c1e-3009-46b7-9ea8-3adb6140d2f2" />

## ELK vs EFK Stack

| Feature | ELK Stack | EFK Stack |
|---|---|---|
| **Full Form** | Elasticsearch, Logstash, Kibana | Elasticsearch, Fluent Bit, Kibana |
| **Log Collector** | Filebeat | Fluent Bit |
| **Log Processor** | Logstash | Fluent Bit |
| **Log Storage & Search** | Elasticsearch | Elasticsearch |
| **Log Visualization** | Kibana | Kibana |
| **Log Collection Agent** | **Filebeat** | **Fluent Bit** |
| **Log Processing** | Mainly handled by **Logstash** | Handled by **Fluent Bit** |
| **Architecture** | Kubernetes → Filebeat → Logstash → Elasticsearch → Kibana | Kubernetes → Fluent Bit → Elasticsearch → Kibana |
| **Runs on Kubernetes** | Filebeat usually runs as a **DaemonSet**; Logstash usually runs as a Deployment | Fluent Bit usually runs as a **DaemonSet** |
| **Log Parsing** | Filebeat can perform basic parsing; Logstash provides advanced parsing and transformation | Fluent Bit provides parsing, filtering, transformation, and enrichment |
| **Kubernetes Metadata** | Filebeat can add Kubernetes metadata | Fluent Bit can add Kubernetes metadata |
| **Log Transformation** | Primarily performed by Logstash | Performed by Fluent Bit |
| **Configuration Complexity** | Generally higher because Filebeat and Logstash are separate components | Generally simpler because Fluent Bit can collect and process logs in one component |
| **Resource Usage** | Typically higher because both Filebeat and Logstash are involved | Typically lower due to Fluent Bit's lightweight design |
| **Scalability** | Filebeat can scale across nodes and Logstash can be scaled separately | Fluent Bit can run on each node and forward logs directly to Elasticsearch |
| **Best Suited For** | Pipelines requiring advanced log processing and transformation | Lightweight Kubernetes logging and efficient log collection |
| **Typical Data Flow** | `Pods → Filebeat → Logstash → Elasticsearch → Kibana` | `Pods → Fluent Bit → Elasticsearch → Kibana` |

```
ELK with Filebeat

In the ELK stack, Filebeat is commonly used as the log shipper/collector:

Kubernetes Pods
       │
       ▼
Container Log Files
       │
       ▼
   Filebeat
       │
       │ Collects Logs
       │ Adds Metadata
       ▼
   Logstash
       │
       │ Parse / Filter / Transform
       ▼
 Elasticsearch
       │
       ▼
    Kibana

So, the roles are:

Filebeat      → Collects and ships logs
Logstash      → Processes and transforms logs
Elasticsearch → Stores and indexes logs
Kibana        → Searches and visualizes logs
EFK

In EFK, Fluent Bit generally performs the collection and processing:

Kubernetes Pods
       │
       ▼
Container Log Files
       │
       ▼
  Fluent Bit
       │
       │ Collect + Process
       │ Add Metadata
       ▼
 Elasticsearch
       │
       ▼
    Kibana

So:

Fluent Bit    → Collects + Processes logs
Elasticsearch → Stores + Indexes logs
Kibana        → Searches + Visualizes logs
```
