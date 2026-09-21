# Distributed Tracing with Jaeger

## 1. What is Distributed Tracing?

Distributed tracing is used to track a request as it moves through an application and its services.

A **trace** represents the complete request, while a **span** represents an individual operation within that trace.

Example:

```text
FastAPI Request
      |
      +-- GET /users
             |
             +-- get-users
                    |
                    +-- database-query
```

Tracing helps identify:

- Where a request spends time
- Which operation is slow
- Where an error occurred
- How different services interact

## 🕵️‍♂️ What is Jaeger?
- Jaeger is an open-source, end-to-end distributed tracing system used for monitoring and troubleshooting microservices-based architectures. It helps developers understand how requests flow through a complex system, by tracing the path a request takes and measuring how long each step in that path takes.

## ❓ Why Use Jaeger?
- In modern applications, especially microservices architectures, a single user request can touch multiple services. When something goes wrong, it’s challenging to pinpoint the source of the problem. Jaeger helps by:

- 🐢 **Identifying bottlenecks**: See where your application spends most of its time.
- 🔍 **Finding root causes of errors**: Trace errors back to their source.
- ⚡ **Optimizing performance**: Understand and improve the latency of services.


## 📚 Core Concepts of Jaeger

- 🛤️ **Trace**: A trace represents the journey of a request as it travels through various services. Think of it as a detailed map that shows every stop a request makes in your system.
- 📏 **Span**: Each trace is made up of multiple spans. A span is a single operation within a trace, such as an API call or a database query. It has a start time and a duration.
- 🏷️ **Tags**: Tags are key-value pairs that provide additional context about a span. For example, a tag might indicate the HTTP method used (GET, POST) or the status code returned.
- 📝 **Logs**: Logs in a span provide details about what’s happening during that operation. They can capture events like errors or important checkpoints.
- 🔗 **Context Propagation**: For Jaeger to trace requests across services, it needs to propagate context. This means each service in the call chain passes along the trace information to the next service.

## Components of Jaeger
- **Jaeger consists of several components:**
- **Agent**: Collects traces from your application.
- **Collector**: Receives traces from the agent and processes them.
- **Query**: Provides a UI to view traces.
- **Storage**: Stores traces for later retrieval (often a database like *Elasticsearch*).

## What is OpenTelemetry
OpenTelemetry in Jaeger refers to the standard framework used to generate, collect, and transport trace data from applications so it can be ingested, stored, and visualized by Jaeger.

### 🏗️ Core Architecture Components

OpenTelemetry splits its architecture into independent layers to stay flexible, modular, and extensible:

| Component | What It Is & What It Does |
| :--- | :--- |
| **API** | Defines the data types and programming syntax used to instrument code. Each language has its own API layer, which acts as the entry point for generating data. |
| **SDK** | The bridge that implements the API definitions for a specific language (Java, Python, Go, etc.). It manages data processing, batching, and sampling behind the scenes. |
| **Collector** | A standalone proxy service that acts as a central pipeline. It receives telemetry data from applications, filters or cleans it, and exports it to your chosen monitoring backend. |
| **OTLP** | **OpenTelemetry Protocol**, the default wire format used to transmit data efficiently between the application SDK, the Collector, and final backends via gRPC or HTTP. |

### 🔀 System Integration Overview

* **OpenTelemetry (The Instrumentation Layer):** Provides vendor-neutral APIs, SDKs, and the OpenTelemetry Protocol (OTLP) to generate and export traces directly from your application code without locking you into a specific vendor.
* **Jaeger (The Backend and Visualization Layer):** Acts as the receiver, storage engine, and Web UI for those traces, letting you inspect request flows, debug bottlenecks, and analyze latency across microservices.

### How They Work Together
Modern versions of Jaeger natively support OpenTelemetry data via OTLP (OpenTelemetry Protocol).

| Feature | OpenTelemetry | Jaeger |
| :--- | :--- | :--- |
| **Primary Role** | Generation, collection, and export | Storage, querying, and visualization |
| **Data Signals** | Traces, metrics, logs, and profiling | Traces exclusively |
| **User Interface** | None (relies on backends) | Includes a rich Web UI |
| **Vendor Agnostic** | Yes (exports to many tools) | Yes (open-source backend) |

## Architecture

<img width="1536" height="1024" alt="ChatGPT Image Sep 21, 2026, 03_30_47 PM" src="https://github.com/user-attachments/assets/16361a0a-811f-4949-820f-e8010ca0c983" />

