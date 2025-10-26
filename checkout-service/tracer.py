import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

def configure_tracer(app):
    # Get the service name from environment variables
    service_name = os.environ.get("OTEL_SERVICE_NAME", "unknown-service")

    # Create a resource to identify this service
    resource = Resource(attributes={"service.name": service_name})

    # Set up a tracer provider
    provider = TracerProvider(resource=resource)

    # Set up an exporter to send traces to Tempo/Collector via OTLP
    otlp_exporter = OTLPSpanExporter(
        endpoint=os.environ.get("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317"),
        insecure=True  # Use insecure connection for local development
    )

    # Use a BatchSpanProcessor to send traces in batches
    processor = BatchSpanProcessor(otlp_exporter)
    provider.add_span_processor(processor)

    # Set the global tracer provider
    trace.set_tracer_provider(provider)

    # Instrument Flask and Requests
    FlaskInstrumentor().instrument_app(app)
    RequestsInstrumentor().instrument()

    return trace.get_tracer(__name__)
