# Changelog

All notable changes to ASTK (AgentSprint TestKit) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

## [0.2.0] - 2024-12-28

### 🎯 Major Features

- **OpenAI Evals API Integration**: Professional-grade agent evaluation using OpenAI's infrastructure
- **New CLI Commands**: `astk evals create`, `astk evals run`, `astk evals compare`
- **Professional Grader Prompts**: Expert-level evaluation for 4 agent types (general, code_qa, customer_service, research)
- **Comparative Analysis**: A/B testing between different models with detailed scoring
- **Beta Status**: Package promoted to Beta (Development Status 4)

### ✨ New Features

- Professional AI-powered grading with detailed explanations
- Logs-based evaluation for cost-effective testing
- Industry-standard evaluation methodology
- Enhanced CLI with evals integration
- Comprehensive examples and documentation

### 🔧 Improvements

- Fixed CLI benchmark command import issues
- Enhanced package description and metadata
- Updated development status to Beta
- Improved error handling and user feedback

### 📦 Dependencies

- Added optional `evals` dependency group: `openai>=1.50.0`, `pandas>=2.0.0`, `plotly>=5.0.0`
- Maintained backward compatibility with existing installations

### 📚 Documentation

- Added `OPENAI_EVALS_INTEGRATION.md` with comprehensive integration guide
- Added `EVALS_TRANSFORMATION_SUMMARY.md` with business impact analysis
- Updated README with OpenAI Evals examples and usage
- Added `examples/evals_example.py` with working integration demo

### 🚀 Breaking Changes

- None - Full backward compatibility maintained

## [0.1.3] - 2024-12-27

### 🔧 Bug Fixes

- **CI/CD Issues**: Resolved all test failures in GitHub Actions workflows
- **Dependencies**: Added missing `pyyaml>=6.0.0` dependency for YAML parsing
- **Python Compatibility**: Updated to support Python 3.9+ (was 3.11+ only)
- **License Classifier**: Changed from Apache to "Other/Proprietary License" to match CC BY-NC-ND 4.0
- **Version Consistency**: Synchronized versions across `setup.py`, `__init__.py`, and `cli.py`
- **Import Handling**: Added graceful import error handling in package initialization
- **Test Coverage**: Enhanced test suite with better error reporting and robustness

### Added

- **New Test Files**:
  - `tests/test_imports.py` for import validation
  - `tests/test_basic.py` for basic functionality verification
- **Dependency Check**: Added `check_deps.py` script for comprehensive dependency validation
- **Enhanced CI**: Improved CI pipeline with better diagnostics and error reporting
- **Dev Dependencies**: Added `pytest-cov>=4.0.0` for coverage reporting

### Changed

- **Contact Email**: Updated all contact emails from `stan@blackbox-dev.com` to `admin@blackbox-dev.com`
- **CI Robustness**: Made CI tests more resilient with proper fallbacks and error handling
- **Package Metadata**: Updated Python classifiers to include 3.9 and 3.10

### Technical Improvements

- Enhanced import error handling with try/catch blocks
- Added comprehensive dependency validation
- Improved test infrastructure with pytest fixtures
- Better CI diagnostics and troubleshooting

## [0.1.2] - 2024-12-27

### Added

- **Comprehensive Documentation**: Added extensive article content about ASTK framework
- **Enhanced Benchmarking**: Improved benchmark scenarios and reporting
- **Better CLI Integration**: Enhanced command-line interface with more robust error handling

### Changed

- **Package Metadata**: Updated package description and metadata
- **License**: Transitioned to Creative Commons BY-NC-ND 4.0 license

### Fixed

- **Minor Bug Fixes**: Various small improvements and stability enhancements

## [0.1.1] - 2024-12-26

### Added

- **Initial CLI Implementation**: Basic command-line interface for running benchmarks
- **Core Testing Framework**: Fundamental testing and benchmarking capabilities
- **Example Agents**: Sample agent implementations for testing

### Fixed

- **Package Structure**: Improved package organization and imports
- **Documentation**: Enhanced README and setup instructions

## [0.1.0] - 2024-12-25

### Added

- **Initial Release**: First public release of ASTK
- **Core Framework**: Basic agent testing and benchmarking framework
- **Schema Validation**: Pydantic-based configuration and validation
- **Metrics Collection**: Basic performance and quality metrics
- **Agent Runner**: Core execution engine for running agent tests

### Features

- Support for Python scripts, REST APIs, and class-based agents
- Configurable test scenarios and success criteria
- JSON and YAML output formats
- Basic CI/CD integration support
