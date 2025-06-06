# Changelog

All notable changes to AgentSprint TestKit will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [0.1.2] - 2024-01-XX

### ✨ Enhanced GitHub Actions & CLI

- **Streamlined CI/CD**: Simplified GitHub Actions workflows for better reliability
- **Updated CI Workflow**: Focus on package testing across Python 3.9-3.12 and multiple OS
- **Improved ASTK Template**: Updated reusable workflow with sophisticated metrics and reporting
- **CLI Redesign**: Main `astk` command now uses the sophisticated benchmark runner with 12 scenarios
- **Package Entry Points**: Fixed console scripts to use working `simple_benchmark.py` and `simple_run.py`
- **Documentation Updates**: All references updated from `pip install astk` to `pip install agent-sprint-testkit`

### 🔧 Technical Improvements

- **Module Structure**: Added proper `__init__.py` to scripts directory for package imports
- **Cross-Platform Testing**: CI now tests on Ubuntu and macOS with multiple Python versions
- **Simplified Workflows**: Removed complex OpenTelemetry and benchmarking infrastructure in favor of working solutions

### 📚 Documentation

- **Workflow Documentation**: Updated all GitHub Actions to match current package structure
- **Package References**: Fixed all documentation to use correct PyPI package name
- **CLI Examples**: Updated help text and examples to match current functionality

## [0.1.1] - 2024-01-XX

### Added

- PyPI package distribution as `agent-sprint-testkit`
- Global CLI installation with `astk` command
- Project initialization with `astk init`
- Enhanced README with pip installation instructions
- GitHub Actions CI/CD workflow templates

### Changed

- Updated installation method to use `pip install agent-sprint-testkit`
- Reorganized CLI commands with primary `astk` interface
- Updated documentation to reflect PyPI package status

### Fixed

- Fixed PyPI metadata classifiers for successful upload
- Resolved package naming conflicts

## [0.1.0] - 2024-03-XX

### Added

- Initial project setup with core components:
  - Scenario-as-Code DSL with Pydantic models
  - Synthetic persona generation using DeepEval
  - Quality metrics with OpenTelemetry integration
  - Chaos testing and fault injection
  - Docker container support
  - CLI interface
- Benchmark infrastructure:

  - Metrics collection (latency, throughput, resource usage)
  - OpenTelemetry integration with Prometheus export
  - Example benchmark scenarios
  - CI integration with automated threshold checks
  - Results archival and analysis

- Initial release
