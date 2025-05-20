# AgentSprint TestKit (ASTK)

A CI-first behavioural-coverage and regression-gating framework that lets engineers ship brand-new AI agents with confidence in <15 minutes.

## Features

- 🚀 **Fast CI Integration**: <10 min median CI run over 200 synthetic conversations
- 🎭 **Synthetic Personas**: Auto-generates diverse user dialogues to stress test agents
- 🔍 **Comprehensive Coverage**: ≥90% scenario branch-coverage reporting
- 🛡️ **Safety First**: Red-team fuzzing and hallucination detection
- 📊 **Rich Telemetry**: OpenTelemetry integration for coverage, latency & cost metrics
- 🔄 **Regression Prevention**: Semantic diffing against production baseline
- 🎮 **Chaos Engineering**: Protocol-level fault injection and edge case testing

## Quick Start

1. Install ASTK:

```bash
pip install astk
```

2. Add to your CI pipeline:

```yaml
# .github/workflows/astk-ci.yml
name: ASTK Agent Tests
on: [pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: astk-dev/astk-action@v1
        with:
          agent-entrypoint: "./my_agent.py"
          scenario-file: "./tests/scenarios.yaml"
```

3. Define test scenarios:

```yaml
# tests/scenarios.yaml
task: "file_qna"
persona:
  archetype: "impatient_mobile_user"
  temperature: 0.9
protocol: "A2A"
success:
  regex: "(?i)here's"
budgets:
  latency_ms: 3000
chaos:
  - "drop_tool:search"
  - "inject_latency:1500"
```

## Documentation

For detailed documentation, visit [docs.astk.dev](https://docs.astk.dev)

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

Apache-2.0
