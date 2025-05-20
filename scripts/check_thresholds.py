#!/usr/bin/env python3
"""
Script to check benchmark results against configured thresholds
"""

import json
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional
import yaml
import click


class ThresholdViolation:
    def __init__(self, metric: str, value: float, threshold: float, is_warning: bool):
        self.metric = metric
        self.value = value
        self.threshold = threshold
        self.is_warning = is_warning

    def __str__(self):
        level = "WARNING" if self.is_warning else "ERROR"
        return f"{level}: {self.metric} = {self.value:.2f} (threshold: {self.threshold:.2f})"


def check_numeric_threshold(
    value: float,
    thresholds: Dict[str, float],
    metric: str,
    is_minimum: bool = False
) -> List[ThresholdViolation]:
    violations = []

    if is_minimum:
        if "min" in thresholds and value < thresholds["min"]:
            violations.append(ThresholdViolation(
                metric, value, thresholds["min"], False))
        elif "warning" in thresholds and value < thresholds["warning"]:
            violations.append(ThresholdViolation(
                metric, value, thresholds["warning"], True))
    else:
        if "max" in thresholds and value > thresholds["max"]:
            violations.append(ThresholdViolation(
                metric, value, thresholds["max"], False))
        elif "warning" in thresholds and value > thresholds["warning"]:
            violations.append(ThresholdViolation(
                metric, value, thresholds["warning"], True))

    return violations


def check_scenario_thresholds(
    result: Dict[str, Any],
    thresholds: Dict[str, Any],
    scenario_overrides: Optional[Dict[str, Any]] = None
) -> List[ThresholdViolation]:
    violations = []

    # Apply scenario-specific overrides if they exist
    scenario_name = result["scenario_name"]
    if scenario_overrides and scenario_name in scenario_overrides:
        thresholds = {**thresholds}  # Create a copy
        for metric, override in scenario_overrides[scenario_name].items():
            if metric in thresholds:
                thresholds[metric] = {**thresholds[metric], **override}

    # Check error rate
    violations.extend(check_numeric_threshold(
        result["error_rate"],
        thresholds["error_rate"],
        "error_rate"
    ))

    # Check latency metrics
    for percentile in ["p50", "p90", "p95", "p99"]:
        if percentile in thresholds["latency"]:
            violations.extend(check_numeric_threshold(
                result["latency"][percentile],
                thresholds["latency"][percentile],
                f"latency_{percentile}"
            ))

    # Check throughput metrics
    for metric in ["conversations_per_minute", "messages_per_minute"]:
        violations.extend(check_numeric_threshold(
            result["throughput"][metric],
            thresholds["throughput"][metric],
            f"throughput_{metric}",
            is_minimum=True
        ))

    # Check resource metrics
    for metric in ["peak_memory_mb", "total_tokens", "total_cost_usd"]:
        violations.extend(check_numeric_threshold(
            result["resources"][metric],
            thresholds["resources"][metric],
            f"resources_{metric}"
        ))

    # Check coverage
    violations.extend(check_numeric_threshold(
        result["coverage_percentage"],
        thresholds["coverage"],
        "coverage",
        is_minimum=True
    ))

    return violations


@click.command()
@click.option(
    "--results-file",
    type=click.Path(exists=True, path_type=Path),
    required=True,
    help="Path to benchmark results JSON file"
)
@click.option(
    "--thresholds-file",
    type=click.Path(exists=True, path_type=Path),
    default=Path("config/benchmark_thresholds.yaml"),
    help="Path to thresholds configuration YAML"
)
@click.option(
    "--fail-on-warning",
    is_flag=True,
    help="Exit with error on warning-level violations"
)
def main(results_file: Path, thresholds_file: Path, fail_on_warning: bool) -> None:
    """Check benchmark results against configured thresholds"""

    # Load results and thresholds
    results = json.loads(results_file.read_text())
    config = yaml.safe_load(thresholds_file.read_text())

    all_violations = []
    error_found = False

    # Check each scenario result
    for result in results["results"]:
        violations = check_scenario_thresholds(
            result,
            config["thresholds"],
            config.get("scenario_overrides")
        )

        if violations:
            click.echo(
                f"\nViolations for scenario '{result['scenario_name']}':")
            for v in violations:
                click.echo(f"  {v}")
                if not v.is_warning or fail_on_warning:
                    error_found = True
            all_violations.extend(violations)

    if not all_violations:
        click.echo("\nAll checks passed successfully!")
    elif error_found:
        sys.exit(1)


if __name__ == "__main__":
    main()
