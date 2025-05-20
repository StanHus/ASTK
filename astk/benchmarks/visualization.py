"""
Enhanced visualization capabilities for benchmark results
"""

from pathlib import Path
from typing import Dict, Any, List, Optional
import json
from datetime import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from scipy import stats


class BenchmarkVisualizer:
    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.color_palette = {
            'primary': '#1f77b4',
            'secondary': '#ff7f0e',
            'success': '#2ca02c',
            'warning': '#d62728',
            'background': '#f8f9fa',
            'grid': '#e9ecef'
        }

    def create_metric_trend_plot(
        self,
        dates: List[datetime],
        values: List[float],
        baseline_mean: Optional[float],
        title: str,
        metric_name: str
    ) -> go.Figure:
        """Create an interactive trend plot with confidence intervals"""
        fig = go.Figure()

        # Add main trend line
        fig.add_trace(go.Scatter(
            x=dates,
            y=values,
            mode='lines+markers',
            name=metric_name,
            line=dict(color=self.color_palette['primary']),
            hovertemplate='%{x}<br>%{y:.2f}<extra></extra>'
        ))

        # Calculate and add confidence intervals if enough data points
        if len(values) > 2:
            x_numeric = np.arange(len(dates))
            slope, intercept, r_value, p_value, std_err = stats.linregress(
                x_numeric, values)

            # Calculate trend line
            trend = slope * x_numeric + intercept

            # Calculate confidence intervals
            conf_int = std_err * stats.t.ppf(0.975, len(dates)-2)
            lower_bound = trend - conf_int
            upper_bound = trend + conf_int

            # Add confidence interval
            fig.add_trace(go.Scatter(
                x=dates + dates[::-1],
                y=np.concatenate([upper_bound, lower_bound[::-1]]),
                fill='toself',
                fillcolor=f'rgba(31, 119, 180, 0.2)',
                line=dict(color='rgba(255,255,255,0)'),
                hoverinfo='skip',
                showlegend=False
            ))

            # Add trend line
            fig.add_trace(go.Scatter(
                x=dates,
                y=trend,
                mode='lines',
                name='Trend',
                line=dict(
                    color=self.color_palette['secondary'],
                    dash='dash'
                ),
                hovertemplate='Trend: %{y:.2f}<extra></extra>'
            ))

        # Add baseline if provided
        if baseline_mean is not None:
            fig.add_hline(
                y=baseline_mean,
                line_dash="dot",
                line_color=self.color_palette['success'],
                annotation_text="Baseline",
                annotation_position="bottom right"
            )

        # Update layout
        fig.update_layout(
            title=title,
            paper_bgcolor=self.color_palette['background'],
            plot_bgcolor=self.color_palette['background'],
            hovermode='x unified',
            xaxis=dict(
                showgrid=True,
                gridcolor=self.color_palette['grid'],
                title='Date'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor=self.color_palette['grid'],
                title=metric_name
            )
        )

        return fig

    def create_metric_distribution_plot(
        self,
        values: List[float],
        current_value: float,
        metric_name: str
    ) -> go.Figure:
        """Create a distribution plot showing historical values and current position"""
        fig = go.Figure()

        # Add histogram of historical values
        fig.add_trace(go.Histogram(
            x=values,
            name='Historical',
            nbinsx=20,
            marker_color=self.color_palette['primary']
        ))

        # Add KDE curve
        if len(values) > 2:
            kde_x = np.linspace(min(values), max(values), 100)
            kde = stats.gaussian_kde(values)
            kde_y = kde(kde_x)

            fig.add_trace(go.Scatter(
                x=kde_x,
                y=kde_y,
                mode='lines',
                name='Distribution',
                line=dict(color=self.color_palette['secondary']),
                yaxis='y2'
            ))

        # Add current value marker
        fig.add_trace(go.Scatter(
            x=[current_value],
            y=[0],
            mode='markers',
            name='Current',
            marker=dict(
                color=self.color_palette['warning'],
                size=12,
                symbol='diamond'
            )
        ))

        # Update layout
        fig.update_layout(
            title=f'{metric_name} Distribution',
            paper_bgcolor=self.color_palette['background'],
            plot_bgcolor=self.color_palette['background'],
            hovermode='x unified',
            xaxis=dict(
                showgrid=True,
                gridcolor=self.color_palette['grid'],
                title=metric_name
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor=self.color_palette['grid'],
                title='Count'
            ),
            yaxis2=dict(
                showgrid=False,
                overlaying='y',
                side='right',
                title='Density'
            )
        )

        return fig

    def create_correlation_plot(
        self,
        metrics_data: Dict[str, List[float]],
        metric_names: List[str]
    ) -> go.Figure:
        """Create a correlation matrix plot between different metrics"""
        correlations = np.zeros((len(metric_names), len(metric_names)))

        for i, metric1 in enumerate(metric_names):
            for j, metric2 in enumerate(metric_names):
                if len(metrics_data[metric1]) > 1 and len(metrics_data[metric2]) > 1:
                    corr = stats.pearsonr(
                        metrics_data[metric1], metrics_data[metric2])[0]
                    correlations[i, j] = corr

        fig = go.Figure(data=go.Heatmap(
            z=correlations,
            x=metric_names,
            y=metric_names,
            colorscale='RdBu',
            zmid=0,
            text=[[f'{val:.2f}' for val in row] for row in correlations],
            texttemplate='%{text}',
            textfont={"size": 10},
            hoverongaps=False
        ))

        fig.update_layout(
            title='Metric Correlations',
            paper_bgcolor=self.color_palette['background'],
            plot_bgcolor=self.color_palette['background']
        )

        return fig

    def create_radar_plot(
        self,
        current_metrics: Dict[str, float],
        baseline_metrics: Dict[str, float],
        thresholds: Dict[str, Dict[str, float]]
    ) -> go.Figure:
        """Create a radar plot comparing current metrics to baseline"""
        metrics = list(current_metrics.keys())

        # Normalize values between 0 and 1
        normalized_current = []
        normalized_baseline = []

        for metric in metrics:
            threshold = thresholds.get(metric, {})
            min_val = threshold.get('min', min(
                current_metrics[metric], baseline_metrics[metric]))
            max_val = threshold.get('max', max(
                current_metrics[metric], baseline_metrics[metric]))
            range_val = max_val - min_val

            if range_val > 0:
                normalized_current.append(
                    (current_metrics[metric] - min_val) / range_val)
                normalized_baseline.append(
                    (baseline_metrics[metric] - min_val) / range_val)
            else:
                normalized_current.append(0.5)
                normalized_baseline.append(0.5)

        fig = go.Figure()

        # Add baseline trace
        fig.add_trace(go.Scatterpolar(
            r=normalized_baseline,
            theta=metrics,
            fill='toself',
            name='Baseline',
            line_color=self.color_palette['secondary']
        ))

        # Add current metrics trace
        fig.add_trace(go.Scatterpolar(
            r=normalized_current,
            theta=metrics,
            fill='toself',
            name='Current',
            line_color=self.color_palette['primary']
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )
            ),
            showlegend=True,
            title='Metric Comparison',
            paper_bgcolor=self.color_palette['background']
        )

        return fig

    def generate_html_report(
        self,
        scenario_results: List[Dict[str, Any]],
        historical_data: Dict[str, List[Dict[str, Any]]],
        thresholds: Dict[str, Any]
    ) -> str:
        """Generate an interactive HTML report with all visualizations"""
        html_parts = ["""
        <html>
        <head>
            <title>Benchmark Results</title>
            <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
            <style>
                body { background-color: #f8f9fa; padding: 20px; }
                .plot-container { background-color: white; padding: 20px; margin: 20px 0; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
            </style>
        </head>
        <body>
            <div class="container">
                <h1 class="mb-4">Benchmark Results</h1>
        """]

        for scenario in scenario_results:
            scenario_name = scenario["scenario_name"]
            historical = historical_data.get(scenario_name, [])

            html_parts.append(f'<h2 class="mt-5">{scenario_name}</h2>')

            # Add trend plots for key metrics
            key_metrics = ["error_rate", "latency.p95",
                           "throughput.conversations_per_minute"]
            for metric in key_metrics:
                dates = [h["date"] for h in historical]
                values = [h[metric.split(".")[0]][metric.split(
                    ".")[1]] if "." in metric else h[metric] for h in historical]
                baseline_mean = statistics.mean(values) if values else None

                fig = self.create_metric_trend_plot(
                    dates, values, baseline_mean,
                    f'{metric} Trend', metric
                )
                html_parts.append(
                    f'<div class="plot-container">{fig.to_html(full_html=False)}</div>')

            # Add distribution plots
            for metric in key_metrics:
                values = [h[metric.split(".")[0]][metric.split(
                    ".")[1]] if "." in metric else h[metric] for h in historical]
                current = scenario[metric.split(".")[0]][metric.split(
                    ".")[1]] if "." in metric else scenario[metric]

                fig = self.create_metric_distribution_plot(
                    values, current, metric)
                html_parts.append(
                    f'<div class="plot-container">{fig.to_html(full_html=False)}</div>')

            # Add correlation plot
            metrics_data = {}
            for metric in key_metrics:
                metrics_data[metric] = [h[metric.split(".")[0]][metric.split(
                    ".")[1]] if "." in metric else h[metric] for h in historical]

            fig = self.create_correlation_plot(metrics_data, key_metrics)
            html_parts.append(
                f'<div class="plot-container">{fig.to_html(full_html=False)}</div>')

            # Add radar plot
            current_metrics = {}
            baseline_metrics = {}
            for metric in key_metrics:
                current = scenario[metric.split(".")[0]][metric.split(
                    ".")[1]] if "." in metric else scenario[metric]
                baseline = statistics.mean([h[metric.split(".")[0]][metric.split(
                    ".")[1]] if "." in metric else h[metric] for h in historical])
                current_metrics[metric] = current
                baseline_metrics[metric] = baseline

            fig = self.create_radar_plot(
                current_metrics, baseline_metrics, thresholds)
            html_parts.append(
                f'<div class="plot-container">{fig.to_html(full_html=False)}</div>')

        html_parts.append("""
            </div>
        </body>
        </html>
        """)

        return "\n".join(html_parts)

    def save_html_report(
        self,
        scenario_results: List[Dict[str, Any]],
        historical_data: Dict[str, List[Dict[str, Any]]],
        thresholds: Dict[str, Any]
    ) -> Path:
        """Generate and save the HTML report"""
        html_content = self.generate_html_report(
            scenario_results,
            historical_data,
            thresholds
        )

        output_file = self.output_dir / "benchmark_report.html"
        output_file.write_text(html_content)
        return output_file
