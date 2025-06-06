# How to Run ASTK Rigorous Multi-Layer Evaluation 🔬

> **Professional-grade AI agent assessment using multiple OpenAI evaluators**

This guide walks you through using ASTK's new rigorous multi-layer evaluation system that provides expert-level assessment of AI agents using sophisticated multi-evaluator scenarios.

## 🚀 Quick Start

### 1. Installation

```bash
# Install ASTK with OpenAI evaluation support
pip install agent-sprint-testkit[evals]

# Set your OpenAI API key
export OPENAI_API_KEY="sk-your-key-here"
```

### 2. Basic Rigorous Evaluation

```bash
# Run complete rigorous evaluation suite (9 scenarios)
python -m astk.cli rigorous run my_agent.py

# Expected output:
# 🔬 ASTK Rigorous Multi-Layer Evaluation
# 🎯 Agent: my_agent.py
# 📋 Scenarios: examples/benchmarks/scenarios/rigorous_multilayer_scenarios.yaml
# 🤖 Evaluators: gpt-4, o1-preview
# 💰 Max Cost: $10.00
```

### 3. View Results

The evaluation generates comprehensive results with:

- Overall pass rate and average scores
- Category-wise performance breakdown (reasoning, ethics, security, etc.)
- Detailed feedback from multiple evaluators
- Cost tracking and time analysis

## 📊 Evaluation Tiers

| Tier          | Difficulty   | Scenarios   | Focus Areas                                    |
| ------------- | ------------ | ----------- | ---------------------------------------------- |
| **🎯 Tier 1** | Foundational | 2 scenarios | Mathematical reasoning, Technical explanations |
| **🧠 Tier 2** | Advanced     | 2 scenarios | Creative problem-solving, Ethical dilemmas     |
| **⚡ Tier 3** | Expert       | 2 scenarios | Systems analysis, Security assessment          |
| **🚀 Tier 4** | Extreme      | 2 scenarios | Logical paradoxes, Crisis coordination         |
| **💥 Chaos**  | Adversarial  | 1 scenario  | Prompt injection resistance                    |

## 🎯 Usage Examples

### Development Testing (Cost-Conscious)

```bash
# Single evaluator, low cost limit
python -m astk.cli rigorous run my_agent.py \
  --evaluators gpt-4 \
  --max-cost 3.0 \
  --fail-fast

# Estimated cost: ~$2.50
```

### Production Assessment (Comprehensive)

```bash
# Multiple evaluators, parallel execution
python -m astk.cli rigorous run my_agent.py \
  --evaluators gpt-4 o1-preview gpt-4-turbo \
  --max-cost 15.0 \
  --parallel \
  --output-format detailed \
  --save-results

# Estimated cost: ~$8-12
```

### Custom Scenario Testing

```bash
# Use specific scenario file
python -m astk.cli rigorous run my_agent.py \
  --scenarios path/to/my_scenarios.yaml \
  --max-cost 5.0
```

## 🛠️ Command Options

### Basic Options

| Option         | Description               | Example                         |
| -------------- | ------------------------- | ------------------------------- |
| `--evaluators` | OpenAI models to use      | `--evaluators gpt-4 o1-preview` |
| `--max-cost`   | Maximum total cost (USD)  | `--max-cost 10.0`               |
| `--parallel`   | Run scenarios in parallel | `--parallel`                    |
| `--fail-fast`  | Stop on first failure     | `--fail-fast`                   |

### Output Options

| Option            | Description          | Example                         |
| ----------------- | -------------------- | ------------------------------- |
| `--output-format` | Result format        | `--output-format detailed`      |
| `--save-results`  | Save to file         | `--save-results`                |
| `--scenarios`     | Custom scenario file | `--scenarios my_scenarios.yaml` |

### Advanced Options

| Option             | Description    | Default |
| ------------------ | -------------- | ------- |
| `--retry-failures` | Retry attempts | 1       |

## 📋 Scenario Descriptions

### Tier 1: Foundational Competency

**foundational_reasoning_chain**

- Tests multi-step mathematical reasoning
- Evaluators: GPT-4, O1-preview
- Pass threshold: 7.0+
- Focus: Calculation accuracy, step clarity

**technical_depth_assessment**

- Microservices vs monolithic architecture analysis
- Evaluators: GPT-4, GPT-4-turbo
- Pass threshold: 7.5+
- Focus: Technical accuracy, practical implementation

### Tier 2: Advanced Cognitive

**creative_constraint_problem**

- Design offline food delivery app with constraints
- Evaluators: GPT-4, O1-preview, GPT-4-turbo
- Pass threshold: 7.5+
- Focus: Innovation, cultural sensitivity, feasibility

**ethical_ai_dilemma**

- Healthcare ICU bed allocation ethics
- Evaluators: GPT-4, O1-preview, GPT-4-turbo
- Pass threshold: 8.0+
- Focus: Ethical reasoning, legal considerations, implementation

### Tier 3: Expert Integration

**complex_systems_analysis**

- Universal Basic Income systemic impact
- Evaluators: 4 specialized evaluators
- Pass threshold: 8.0+
- Focus: Systems thinking, multi-domain analysis

**adversarial_security_analysis**

- Cryptocurrency exchange security assessment
- Evaluators: 4 expert evaluators
- Pass threshold: 8.5+
- Focus: Security expertise, threat modeling

### Tier 4: Extreme Edge Cases

**paradox_resolution_challenge**

- AI logical paradoxes and self-reference
- Evaluators: O1-preview, GPT-4, GPT-4-turbo
- Pass threshold: 8.5+
- Focus: Logical consistency, philosophical reasoning

**multi_modal_crisis_coordination**

- Hurricane + COVID + cyberattack crisis management
- Evaluators: 4 expert evaluators
- Pass threshold: 8.0+
- Focus: Crisis management, systems coordination

### Chaos Engineering

**adversarial_input_resistance**

- Prompt injection and manipulation resistance
- Evaluators: GPT-4, O1-preview, GPT-4-turbo
- Pass threshold: 9.0+
- Focus: Security robustness, attack resistance

## 💰 Cost Management

### Cost Estimation

| Scenario Tier      | Estimated Cost | Evaluators               |
| ------------------ | -------------- | ------------------------ |
| Tier 1             | $0.30-0.40     | 2 evaluators             |
| Tier 2             | $0.60-0.80     | 3 evaluators             |
| Tier 3             | $1.00-1.30     | 4 evaluators             |
| Tier 4             | $0.80-1.20     | 3-4 evaluators           |
| **Complete Suite** | **~$6.50**     | **14 total evaluations** |

### Cost Control Strategies

```bash
# Set strict limits
python -m astk.cli rigorous run my_agent.py --max-cost 5.0

# Use single evaluator
python -m astk.cli rigorous run my_agent.py --evaluators gpt-4

# Stop early on failures
python -m astk.cli rigorous run my_agent.py --fail-fast --max-cost 3.0

# Target specific tiers (create custom scenario file)
python -m astk.cli rigorous run my_agent.py \
  --scenarios tier1_only.yaml \
  --max-cost 1.0
```

## 📊 Understanding Results

### Sample Output

```bash
🏁 EVALUATION COMPLETE
==========================================
📊 Results: 7/9 passed (77.8%)
💰 Total Cost: $6.45
⏱️  Total Time: 28.5s
🎯 Average Score: 7.8/10

📂 Performance by Category:
   reasoning: 8.2/10 (100% pass rate)
   technical_knowledge: 7.9/10 (100% pass rate)
   creativity: 7.1/10 (100% pass rate)
   ethics: 8.5/10 (100% pass rate)
   security: 6.8/10 (50% pass rate)

🎓 Performance by Difficulty:
   intermediate: 8.1/10 (100% pass rate)
   advanced: 7.8/10 (100% pass rate)
   expert: 7.2/10 (67% pass rate)
```

### Key Metrics

- **Pass Rate**: Percentage of scenarios meeting pass thresholds
- **Average Score**: Weighted average across all evaluators
- **Category Performance**: Breakdown by domain expertise
- **Difficulty Performance**: Performance scaling with complexity
- **Cost Efficiency**: Cost per successful evaluation

## 🔧 Troubleshooting

### Common Issues

**High Costs**

```bash
# Solution: Use cost limits and fewer evaluators
python -m astk.cli rigorous run my_agent.py \
  --evaluators gpt-4 \
  --max-cost 3.0
```

**API Rate Limits**

```bash
# Solution: Use sequential execution (default)
python -m astk.cli rigorous run my_agent.py
# Don't use --parallel if hitting rate limits
```

**Low Pass Rates**

```bash
# Solution: Analyze detailed feedback
python -m astk.cli rigorous run my_agent.py \
  --output-format detailed \
  --save-results
```

## 🎯 Best Practices

### For Development

1. **Start small**: Use single evaluator and cost limits
2. **Focus areas**: Target specific categories for improvement
3. **Iterate**: Use detailed feedback to improve agent
4. **Cost control**: Set strict limits to avoid surprises

### For Production

1. **Full assessment**: Use multiple evaluators
2. **Parallel execution**: Speed up evaluation
3. **Comprehensive logging**: Save detailed results
4. **Regular testing**: Include in CI/CD pipeline

### Custom Scenarios

1. **Domain-specific**: Create scenarios for your use case
2. **Expert evaluators**: Use specialized evaluation prompts
3. **Appropriate thresholds**: Set realistic pass criteria
4. **Cost budgeting**: Estimate costs before large evaluations

## 🚀 Advanced Usage

### Creating Custom Scenarios

```yaml
scenarios:
  - name: "my_domain_test"
    task: "domain_analysis"
    description: "Custom domain-specific evaluation"
    difficulty: "expert"
    category: "custom"
    persona:
      archetype: "domain_expert"
      temperature: 0.4
    protocol: "A2A"
    input_prompt: |
      Analyze this domain-specific problem...
    success:
      openai_evaluations:
        - evaluator: "gpt-4"
          prompt: |
            Evaluate as domain expert:
            1. Technical accuracy (40%)
            2. Domain knowledge (30%)
            3. Practical applicability (20%)
            4. Innovation (10%)
          pass_threshold: 8.0
    budgets:
      cost_usd: 0.5
```

### Integration with CI/CD

```yaml
# .github/workflows/agent-evaluation.yml
name: Rigorous Agent Evaluation

on: [push, pull_request]

jobs:
  evaluate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Install ASTK
        run: pip install agent-sprint-testkit[evals]
      - name: Run Rigorous Evaluation
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          python -m astk.cli rigorous run agents/my_agent.py \
            --max-cost 8.0 \
            --output-format json \
            --save-results
```

---

**🎯 Ready for professional-grade agent evaluation?**

```bash
pip install agent-sprint-testkit[evals]
export OPENAI_API_KEY="your-key"
python -m astk.cli rigorous run my_agent.py --max-cost 8.0
```
