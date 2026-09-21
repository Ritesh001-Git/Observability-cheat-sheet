from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
import time


# -----------------------------
# OpenTelemetry configuration
# -----------------------------

resource = Resource.create({
    "service.name": "fastapi-tracing-demo"
})

provider = TracerProvider(
    resource=resource
)

exporter = OTLPSpanExporter(
    endpoint="jaeger.tracing.svc.cluster.local:4317",
    insecure=True
)

processor = BatchSpanProcessor(exporter)

provider.add_span_processor(processor)

trace.set_tracer_provider(provider)

tracer = trace.get_tracer(__name__)


# -----------------------------
# FastAPI
# -----------------------------

app = FastAPI()


# Automatically instrument FastAPI
FastAPIInstrumentor.instrument_app(app)


# -----------------------------
# Routes
# -----------------------------

@app.get("/")
def home():

    with tracer.start_as_current_span("home-operation") as span:

        span.set_attribute(
            "app.operation",
            "home"
        )

        time.sleep(0.2)

        return {
            "message": "FastAPI tracing demo",
            "status": "success"
        }


@app.get("/users")
def users():

    with tracer.start_as_current_span("get-users"):

        with tracer.start_as_current_span(
            "database-query"
        ) as db_span:

            db_span.set_attribute(
                "db.system",
                "fake-database"
            )

            time.sleep(0.3)

        return {
            "users": [
                {
                    "id": 1,
                    "name": "Ritesh"
                },
                {
                    "id": 2,
                    "name": "John"
                }
            ]
        }


@app.get("/orders")
def orders():

    with tracer.start_as_current_span(
        "get-orders"
    ):

        with tracer.start_as_current_span(
            "order-processing"
        ):

            time.sleep(0.5)

        return {
            "orders": [
                {
                    "id": 101,
                    "amount": 500
                },
                {
                    "id": 102,
                    "amount": 750
                }
            ]
        }


@app.get("/slow")
def slow():

    with tracer.start_as_current_span(
        "slow-operation"
    ):

        time.sleep(2)

        return {
            "message": "Slow operation completed"
        }


@app.get("/error")
def error():

    with tracer.start_as_current_span(
        "error-operation"
    ) as span:

        try:

            raise ValueError(
                "Demo application error"
            )

        except ValueError as exc:

            span.record_exception(exc)

            span.set_status(
                trace.Status(
                    trace.StatusCode.ERROR,
                    "Demo application error"
                )
            )

            return {
                "error": str(exc)
            }