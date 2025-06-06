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
