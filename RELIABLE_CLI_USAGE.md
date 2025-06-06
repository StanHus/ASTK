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

# NEW: Rigorous multi-layer evaluation
python -m astk.cli rigorous run examples/agents/file_qa_agent.py
python -m astk.cli rigorous run my_agent.py --max-cost 10.0 --parallel

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
astk rigorous run my_agent.py
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

### 🔬 Rigorous Multi-Layer Evaluation Commands

```bash
# Run complete rigorous evaluation suite
python -m astk.cli rigorous run <agent-path>

# Run with specific evaluators
python -m astk.cli rigorous run <agent-path> --evaluators gpt-4 o1-preview

# Run with cost limit and parallel execution
python -m astk.cli rigorous run <agent-path> --max-cost 15.0 --parallel

# Run with custom scenarios
python -m astk.cli rigorous run <agent-path> --scenarios my_scenarios.yaml

# Run with detailed output and save results
python -m astk.cli rigorous run <agent-path> \
  --output-format detailed \
  --save-results \
  --max-cost 10.0

# Run with fail-fast mode
python -m astk.cli rigorous run <agent-path> --fail-fast

# Available evaluators: gpt-4, o1-preview, gpt-4-turbo
# Output formats: json, yaml, detailed
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
# 1. Install ASTK with evaluation support
pip install agent-sprint-testkit[evals]

# 2. Verify installation
python -m astk.cli --help

# 3. Set API key
export OPENAI_API_KEY="your-key-here"

# 4. Run first benchmark
python -m astk.cli benchmark examples/agents/file_qa_agent.py

# 5. Run rigorous evaluation
python -m astk.cli rigorous run examples/agents/file_qa_agent.py
```

### Project Setup

```bash
# Create new project
python -m astk.cli init my-agent-tests
cd my-agent-tests

# Run traditional benchmarks
python -m astk.cli benchmark agents/my_agent.py

# Run rigorous multi-layer evaluation
python -m astk.cli rigorous run agents/my_agent.py --max-cost 8.0

# Generate reports
python -m astk.cli report astk_results/
```

### 🔬 Rigorous Evaluation Workflow

```bash
# Install with full evaluation support
pip install agent-sprint-testkit[evals]

# Set OpenAI API key
export OPENAI_API_KEY="sk-your-key-here"

# Quick rigorous evaluation
python -m astk.cli rigorous run my_agent.py

# Professional evaluation with custom parameters
python -m astk.cli rigorous run my_agent.py \
  --evaluators gpt-4 o1-preview gpt-4-turbo \
  --max-cost 12.0 \
  --parallel \
  --output-format detailed \
  --save-results

# Cost-conscious evaluation
python -m astk.cli rigorous run my_agent.py \
  --evaluators gpt-4 \
  --max-cost 5.0 \
  --fail-fast
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
pip install agent-sprint-testkit[evals]

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
python -m astk.cli rigorous run my_agent.py  # This always works
```

### Issue: OpenAI API errors in rigorous evaluation

```bash
# Check API key is set
echo $OPENAI_API_KEY

# Test API connection
python -c "import openai; print('OpenAI client ready')"

# Start with lower cost limit
python -m astk.cli rigorous run my_agent.py --max-cost 3.0 --evaluators gpt-4
```

### Issue: Rigorous evaluation costs too much

```bash
# Use fewer evaluators
python -m astk.cli rigorous run my_agent.py --evaluators gpt-4

# Set strict cost limits
python -m astk.cli rigorous run my_agent.py --max-cost 5.0

# Use fail-fast to stop early
python -m astk.cli rigorous run my_agent.py --fail-fast --max-cost 3.0
```

## 📝 Best Practices

1. **Always use `python -m astk.cli`** in documentation and scripts
2. **Test commands** with the module format first
3. **Include full paths** when referencing agents or results
4. **Set environment variables** before running commands
5. **Use virtual environments** for project isolation
6. **Set cost limits** for rigorous evaluation to avoid unexpected charges
7. **Start with single evaluator** and scale up for production assessment

## 🎯 Summary

**Use this format for 100% reliability:**

```bash
# Traditional benchmark
python -m astk.cli benchmark examples/agents/file_qa_agent.py

# Professional rigorous evaluation
python -m astk.cli rigorous run examples/agents/file_qa_agent.py --max-cost 8.0
```

**Instead of this potentially unreliable format:**

```bash
astk benchmark examples/agents/file_qa_agent.py
astk rigorous run examples/agents/file_qa_agent.py
```

This ensures your ASTK commands work consistently across all environments and installations! 🚀

## 💡 Pro Tips

### Cost-Effective Rigorous Testing

```bash
# For development/testing - use single evaluator
python -m astk.cli rigorous run my_agent.py --evaluators gpt-4 --max-cost 3.0

# For production assessment - use multiple evaluators
python -m astk.cli rigorous run my_agent.py \
  --evaluators gpt-4 o1-preview gpt-4-turbo \
  --max-cost 15.0 \
  --parallel
```

### Targeted Evaluation

```bash
# Create custom scenario subset for specific testing
python -m astk.cli rigorous run my_agent.py \
  --scenarios examples/benchmarks/scenarios/custom_subset.yaml \
  --max-cost 5.0
```
