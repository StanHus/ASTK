# ASTK Reliable CLI Usage Guide 🛠️

> **Avoid installation confusion with these reliable command patterns**

This guide shows you the most reliable ways to run ASTK commands that work regardless of your PATH configuration or installation method.

## 🎯 Recommended Command Format

### ✅ Always Works (Recommended)

Use the Python module format for all ASTK commands:

```bash
# Main CLI commands
python -m astk.cli --help
python -m astk.cli benchmark examples/agents/file_qa_agent.py
python -m astk.cli init my-project
python -m astk.cli examples
python -m astk.cli report results/

# OpenAI Evals integration
python -m astk.cli evals create my_agent.py --eval-type code_qa
python -m astk.cli evals run eval_12345
python -m astk.cli evals compare eval_12345 gpt-4o-mini gpt-4-turbo
```

### ⚠️ May Not Work (PATH dependent)

These commands only work if ASTK is properly installed in your PATH:

```bash
# These might fail with "command not found"
astk benchmark examples/agents/file_qa_agent.py
astk init my-project
astk examples
```

## 🔧 Why Use `python -m astk.cli`?

### ✅ Benefits:

- **Always works** regardless of PATH configuration
- **No installation confusion** with pip/venv issues
- **Consistent across environments** (dev, CI, production)
- **Works in any Python environment** where ASTK is installed
- **No need for console script registration**

### ❌ Traditional `astk` command issues:

- Requires proper PATH configuration
- May fail after pip installs or virtual environment switches
- Console scripts might not register properly
- Different behavior across operating systems

## 📋 Complete Command Reference

### Core Commands

```bash
# Show help
python -m astk.cli --help

# Initialize new project
python -m astk.cli init <project-name>

# Run benchmark
python -m astk.cli benchmark <agent-path>

# Generate reports
python -m astk.cli report <results-dir>

# Show examples
python -m astk.cli examples

# Show version
python -m astk.cli --version
```

### OpenAI Evals Integration

```bash
# Create evaluation
python -m astk.cli evals create <agent-path> [options]

# Run evaluation
python -m astk.cli evals run <eval-id>

# Compare models
python -m astk.cli evals compare <eval-id> <baseline> <test-model>
```

### Direct Script Access

For advanced users, you can also run scripts directly:

```bash
# Benchmark script
python scripts/simple_benchmark.py <agent-path>

# Agent runner
python scripts/simple_run.py <agent-path>
```

## 🚀 Quick Start Examples

### Basic Workflow

```bash
# 1. Install ASTK
pip install agent-sprint-testkit

# 2. Verify installation
python -m astk.cli --help

# 3. Set API key
export OPENAI_API_KEY="your-key-here"

# 4. Run first benchmark
python -m astk.cli benchmark examples/agents/file_qa_agent.py
```

### Project Setup

```bash
# Create new project
python -m astk.cli init my-agent-tests
cd my-agent-tests

# Run benchmarks
python -m astk.cli benchmark agents/my_agent.py

# Generate reports
python -m astk.cli report astk_results/
```

### OpenAI Evals Workflow

```bash
# Install with evals support
pip install agent-sprint-testkit[evals]

# Create evaluation
python -m astk.cli evals create my_agent.py --eval-type code_qa --grader gpt-4

# Run evaluation (returns eval ID)
python -m astk.cli evals run eval_67890

# Compare models
python -m astk.cli evals compare eval_67890 gpt-4o-mini gpt-4-turbo
```

## 🔍 Troubleshooting

### Issue: "No module named 'astk'"

```bash
# Solution: Install ASTK
pip install agent-sprint-testkit

# Verify installation
python -c "import astk; print('ASTK loaded successfully')"
```

### Issue: "Command not found: astk"

```bash
# Solution: Use module format instead
python -m astk.cli --help
# Instead of: astk --help
```

### Issue: Virtual environment confusion

```bash
# Always use python -m format in any environment
source .venv/bin/activate  # Activate your venv
python -m astk.cli benchmark my_agent.py  # This always works
```

## 📝 Best Practices

1. **Always use `python -m astk.cli`** in documentation and scripts
2. **Test commands** with the module format first
3. **Include full paths** when referencing agents or results
4. **Set environment variables** before running commands
5. **Use virtual environments** for project isolation

## 🎯 Summary

**Use this format for 100% reliability:**

```bash
python -m astk.cli benchmark examples/agents/file_qa_agent.py
```

**Instead of this potentially unreliable format:**

```bash
astk benchmark examples/agents/file_qa_agent.py
```

This ensures your ASTK commands work consistently across all environments and installations! 🚀
