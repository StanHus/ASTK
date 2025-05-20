"""
Command-line interface for ASTK
"""

import asyncio
import json
import sys
from pathlib import Path
from typing import Optional

import click
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

from .runner import AgentRunner


def setup_telemetry(
    otlp_endpoint: Optional[str] = None,
    console_output: bool = False
) -> None:
    """
    Set up OpenTelemetry exporters

    Args:
        otlp_endpoint: Optional OTLP endpoint URL
        console_output: Whether to also output to console
    """
    # Set up tracing
    provider = TracerProvider()

    if otlp_endpoint:
        from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
        otlp_processor = BatchSpanProcessor(
            OTLPSpanExporter(endpoint=otlp_endpoint))
        provider.add_span_processor(otlp_processor)

    if console_output:
        console_processor = BatchSpanProcessor(ConsoleSpanExporter())
        provider.add_span_processor(console_processor)

    trace.set_tracer_provider(provider)

    # Set up metrics
    metric_readers = []

    if otlp_endpoint:
        from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
        metric_readers.append(
            PeriodicExportingMetricReader(
                OTLPMetricExporter(endpoint=otlp_endpoint)
            )
        )

    if console_output:
        metric_readers.append(
            PeriodicExportingMetricReader(
                ConsoleMetricExporter()
            )
        )

    metrics.set_meter_provider(
        MeterProvider(metric_readers=metric_readers)
    )


@click.group()
def cli():
    """AgentSprint TestKit - Agent testing and validation framework"""
    pass


@cli.command()
@click.argument(
    "agent_entrypoint",
    type=click.Path(exists=True, path_type=Path)
)
@click.argument(
    "scenario_file",
    type=click.Path(exists=True, path_type=Path)
)
@click.option(
    "--docker-image",
    help="Docker image to run agent in"
)
@click.option(
    "--otlp-endpoint",
    help="OTLP endpoint URL for telemetry export"
)
@click.option(
    "--console-output",
    is_flag=True,
    help="Output telemetry to console"
)
@click.option(
    "--output-file",
    type=click.Path(path_type=Path),
    help="Save results to JSON file"
)
def run(
    agent_entrypoint: Path,
    scenario_file: Path,
    docker_image: Optional[str],
    otlp_endpoint: Optional[str],
    console_output: bool,
    output_file: Optional[Path]
) -> None:
    """
    Run agent test scenarios

    AGENT_ENTRYPOINT: Path to agent entry point
    SCENARIO_FILE: Path to scenario config file
    """
    # Set up telemetry
    setup_telemetry(otlp_endpoint, console_output)

    try:
        # Run scenarios
        results = asyncio.run(
            AgentRunner.execute(
                agent_entrypoint,
                scenario_file,
                docker_image
            )
        )

        # Output results
        if output_file:
            output_file.write_text(json.dumps(results, indent=2))
        else:
            click.echo(json.dumps(results, indent=2))

        # Set exit code based on test results
        sys.exit(0 if results["failed"] == 0 else 1)

    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    cli()
