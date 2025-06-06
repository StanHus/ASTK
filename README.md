# AgentSprint TestKit (ASTK) 🚀

> Universal AI agent benchmarking and testing framework with professional-grade multi-layer evaluation

ASTK is a comprehensive testing framework for AI agents that evaluates performance, intelligence, and capabilities through diverse scenarios. Test your agents against real-world tasks like file analysis, code comprehension, complex reasoning, and professional-grade multi-layer evaluation using OpenAI's infrastructure.

## Usage Example

Please see https://github.com/StanHus/astk-test

## 🎯 Features

- **🧠 Intelligent Benchmarks**: 8 diverse scenarios testing different AI capabilities
- **🔬 Rigorous Multi-Layer Evaluation**: NEW! Professional-grade assessment using multiple OpenAI evaluators
- **📊 Performance Metrics**: Response time, success rate, and quality analysis
- **🔧 Easy Installation**: Simple pip install from PyPI
- **🌐 Universal Testing**: Works with CLI agents, REST APIs, Python modules, and more
- **🤖 Agent Ready**: Compatible with LangChain, OpenAI, and custom agents
- **📁 Built-in Examples**: File Q&A agent and project templates
- **⚙️ GitHub Actions**: Ready-to-use CI/CD workflow templates
- **🎯 OpenAI Evals Integration**: Professional-grade evaluation using OpenAI's infrastructure
- **⚡ Multiple Evaluation Tiers**: From basic testing to expert-level assessment

## 📋 Quick Start

### 1. Install from PyPI

```bash
# Standard installation
pip install agent-sprint-testkit

# With OpenAI Evals support for rigorous evaluation
pip install agent-sprint-testkit[evals]
```

### 2. Verify Installation

```bash
python -m astk.cli --help
```

### 3. Set API Key

```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 4. Initialize a Project

```bash
python -m astk.cli init my-agent-tests
cd my-agent-tests
```

### 5. Run Your First Benchmark

```bash
# Traditional ASTK benchmark (quick)
python -m astk.cli benchmark examples/agents/file_qa_agent.py

# NEW: Rigorous multi-layer evaluation (professional-grade)
python -m astk.cli rigorous run my_agent.py

# OpenAI Evals integration (enterprise)
python -m astk.cli evals create my_agent.py --eval-type code_qa --grader gpt-4
```

## 🔬 NEW: Rigorous Multi-Layer Evaluation

Experience professional-grade AI agent assessment with our new multi-layer evaluation system:

### ✨ Key Features

- **🎯 Multiple Evaluation Layers**: Each scenario uses 2-4 different OpenAI models as specialized evaluators
- **🏆 Expert-Level Assessment**: 4-tier difficulty system from foundational to expert integration
- **🧠 Domain-Specific Grading**: Specialized evaluation prompts for security, ethics, systems thinking, etc.
- **📊 Comprehensive Scoring**: Detailed dimension scores with weighted overall assessment
- **💰 Cost Transparent**: Built-in cost estimation and budgeting controls
- **⚡ Parallel Execution**: Optional parallel processing for faster results

### 🎯 Quick Start - Rigorous Evaluation

```bash
# Run rigorous multi-layer evaluation
python -m astk.cli rigorous run my_agent.py

# With custom evaluators and cost limit
python -m astk.cli rigorous run my_agent.py \
  --evaluators gpt-4 o1-preview gpt-4-turbo \
  --max-cost 15.0 \
  --parallel

# Use custom scenarios file
python -m astk.cli rigorous run my_agent.py \
  --scenarios path/to/my_scenarios.yaml \
  --output-format detailed \
  --save-results
```

### 📊 Evaluation Tiers

| Tier          | Focus                   | Scenarios                                      | Evaluators                     | Pass Threshold |
| ------------- | ----------------------- | ---------------------------------------------- | ------------------------------ | -------------- |
| **🎯 Tier 1** | Foundational Competency | Mathematical reasoning, Technical explanations | GPT-4, O1-preview              | 7.0+           |
| **🧠 Tier 2** | Advanced Cognitive      | Creative problem-solving, Ethical dilemmas     | GPT-4, O1-preview, GPT-4-turbo | 7.5+           |
| **⚡ Tier 3** | Expert Integration      | Systems analysis, Security assessment          | 4 specialized evaluators       | 8.0+           |
| **🚀 Tier 4** | Extreme Edge Cases      | Logical paradoxes, Crisis coordination         | 3-4 expert evaluators          | 8.5+           |

### 🧪 Sample Rigorous Scenarios

**Foundational Reasoning** - Multi-step mathematical problem with step verification

```yaml
- Mathematical reasoning with explicit step verification
- Technical architecture explanations with domain expertise validation
```

**Creative Constraint Problem** - Food delivery app for offline/SMS/cash environments

```yaml
- Design offline-first solutions with cultural sensitivity evaluation
- Business model viability assessed by multiple expert perspectives
```

**Ethical AI Dilemma** - Healthcare ICU bed allocation with competing moral frameworks

```yaml
- Medical ethics principles application
- Legal and practical implementation assessment
- Philosophical framework analysis
```

**Complex Systems Analysis** - Universal Basic Income systemic impact assessment

```yaml
- 6-domain analysis: economic, social, political, technological, environmental, international
- Systemic thinking evaluation with feedback loop identification
- Policy implementation and monitoring recommendations
```

### 💰 Cost Management

```bash
# Set cost limits
python -m astk.cli rigorous run my_agent.py --max-cost 10.0

# Check estimated costs before running
python -m astk.cli rigorous run my_agent.py --dry-run

# Use cost-effective evaluator combinations
python -m astk.cli rigorous run my_agent.py --evaluators gpt-4 gpt-4-turbo
```

**Estimated Costs:**

- Complete rigorous suite (9 scenarios): ~$6.50
- Single expert scenario: ~$0.50-$1.30
- Foundational scenarios: ~$0.30-$0.40

## 🚀 Installation Options

### Option 1: Global Installation (Recommended)

```bash
# Standard installation
pip install agent-sprint-testkit

# With all optional features
pip install agent-sprint-testkit[evals,dev,docker]
```

### Option 2: Development Setup

```bash
# Clone repository
git clone https://github.com/your-org/astk.git
cd astk

# Create virtual environment
python3.11 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
pip install -e .[evals,dev]
```

## 💻 CLI Commands

### Core Commands

```bash
# Initialize new project with templates
python -m astk.cli init <project-name>

# Run intelligent benchmarks
python -m astk.cli benchmark <agent-path>

# Generate detailed reports
python -m astk.cli report <results-dir>

# Show example usage
python -m astk.cli examples
```

### 🔬 Rigorous Multi-Layer Evaluation Commands

```bash
# Run complete rigorous evaluation suite
python -m astk.cli rigorous run <agent-path>

# Custom evaluation with specific parameters
python -m astk.cli rigorous run <agent-path> \
  --scenarios path/to/scenarios.yaml \
  --evaluators gpt-4 o1-preview gpt-4-turbo \
  --parallel \
  --max-cost 20.0 \
  --output-format detailed \
  --save-results \
  --fail-fast

# Available options:
# --scenarios: Custom scenarios YAML file
# --evaluators: OpenAI models to use (gpt-4, o1-preview, gpt-4-turbo)
# --parallel: Run scenarios in parallel (faster, more expensive)
# --max-cost: Maximum total cost in USD
# --output-format: json, yaml, or detailed markdown
# --save-results: Save comprehensive results to file
# --fail-fast: Stop on first scenario failure
# --retry-failures: Number of retry attempts (default: 1)
```

### 🎯 OpenAI Evals Integration

```bash
# Create professional evaluation
python -m astk.cli evals create my_agent.py --eval-type code_qa --grader gpt-4

# Run evaluation from logs
python -m astk.cli evals run <eval-id>

# Compare two models
python -m astk.cli evals compare <eval-id> gpt-4o-mini gpt-4-turbo

# Available eval types: general, code_qa, customer_service, research
# Available graders: gpt-4, gpt-4-turbo, o3, o3-mini
```

### Legacy Script Commands (still supported)

```bash
# Run intelligent benchmark
python scripts/simple_benchmark.py <agent-path>

# Quick agent runner
python scripts/simple_run.py <agent-path>
```

## 🔬 Rigorous Evaluation Deep Dive

### 📋 Complete Scenario List

**Tier 1: Foundational Competency**

- `foundational_reasoning_chain` - Mathematical reasoning with step verification
- `technical_depth_assessment` - Microservices vs monolithic architecture analysis

**Tier 2: Advanced Cognitive**

- `creative_constraint_problem` - Offline food delivery app design
- `ethical_ai_dilemma` - Healthcare ICU bed allocation ethics

**Tier 3: Expert Integration**

- `complex_systems_analysis` - Universal Basic Income systemic analysis
- `adversarial_security_analysis` - Cryptocurrency exchange security assessment

**Tier 4: Extreme Edge Cases**

- `paradox_resolution_challenge` - AI logical paradoxes and self-reference
- `multi_modal_crisis_coordination` - Hurricane + COVID + cyberattack crisis management

**Chaos Engineering**

- `adversarial_input_resistance` - Prompt injection and manipulation resistance

### 🎓 Evaluation Methodology

Each scenario employs sophisticated multi-layer evaluation:

1. **Basic Validation Layer**: Regex pattern matching and semantic scoring
2. **Primary OpenAI Evaluation**: Main grader with comprehensive rubric
3. **Specialist Evaluations**: Domain experts (security, ethics, systems thinking)
4. **Cross-Validation**: Multiple models for consensus scoring

**Scoring Dimensions:**

- Technical Accuracy (30-40%)
- Completeness & Depth (25-30%)
- Reasoning Quality (20-25%)
- Practical Value & Implementation (10-20%)

### 📊 Results & Reporting

Comprehensive results include:

```json
{
  "session_id": "20241210_143022",
  "summary": {
    "total_scenarios": 9,
    "scenarios_passed": 7,
    "pass_rate": 0.778,
    "average_score": 7.8,
    "total_cost_usd": 6.45,
    "total_duration_ms": 28500
  },
  "category_performance": {
    "reasoning": 8.2,
    "technical_knowledge": 7.9,
    "creativity": 7.1,
    "ethics": 8.5,
    "security": 6.8
  },
  "detailed_results": [...]
}
```

### 🎯 Custom Scenarios

Create your own rigorous scenarios:

```yaml
scenarios:
  - name: "my_custom_scenario"
    task: "custom_analysis"
    description: "Custom multi-layer evaluation scenario"
    difficulty: "expert"
    category: "custom"
    persona:
      archetype: "domain_expert"
      temperature: 0.4
      traits: ["analytical", "thorough", "critical"]
    protocol: "A2A"
    input_prompt: |
      Your complex scenario prompt here...
    success:
      regex: "(?i)(key|concepts|here)"
      semantic_score: 0.85
      openai_evaluations:
        - evaluator: "gpt-4"
          prompt: |
            Evaluate this response as a domain expert:
            1. Technical accuracy (40%)
            2. Depth of analysis (30%) 
            3. Practical applicability (20%)
            4. Innovation (10%)
            Score 1-10 per dimension with detailed feedback.
          pass_threshold: 8.0
        - evaluator: "o1-preview"
          prompt: |
            Verify logical consistency and identify gaps...
          pass_threshold: 7.5
    budgets:
      latency_ms: 30000
      cost_usd: 0.8
      tokens: 4000
```

## 🎯 OpenAI Evals Integration

ASTK integrates with OpenAI's professional Evals API for enterprise-grade agent evaluation:

### ✨ Key Benefits

- **🏆 Professional-grade evaluation** using OpenAI's infrastructure
- **🎯 AI-powered grading** with detailed scoring explanations
- **⚖️ Easy A/B testing** between agent versions
- **📊 Comparative analysis** with industry benchmarks
- **💰 Cost-effective** by leveraging existing logs

### 🛠️ Quick Start with Evals

```bash
# 1. Install with Evals support
pip install agent-sprint-testkit[evals]

# 2. Set up OpenAI API key
export OPENAI_API_KEY=your_key_here

# 3. Create evaluation for your agent
python -m astk.cli evals create my_agent.py --eval-type code_qa --grader gpt-4

# 4. Run evaluation
python -m astk.cli evals run eval_12345

# 5. View results in OpenAI dashboard
```

### 📊 Evaluation Types

| Type               | Description                 | Use Case                         |
| ------------------ | --------------------------- | -------------------------------- |
| `general`          | General-purpose evaluation  | All-around agent testing         |
| `code_qa`          | Code analysis and Q&A       | Developer tools, code assistants |
| `customer_service` | Customer support scenarios  | Support bots, help systems       |
| `research`         | Research and analysis tasks | Research assistants, analysts    |

### 🎓 Example Usage

```python
# Create and run evaluation programmatically
from astk.evals_integration import OpenAIEvalsAdapter

adapter = OpenAIEvalsAdapter()
eval_id = adapter.create_eval_from_scenarios(
    scenarios=my_scenarios,
    eval_name="My Agent Evaluation",
    grader_model="gpt-4"
)

# Run comparative evaluation
results = adapter.run_comparative_evaluation(
    eval_id=eval_id,
    baseline_model="gpt-4o-mini",
    test_model="gpt-4-turbo"
)
```

## 🤖 Available Agents

### File Q&A Agent (`examples/agents/file_qa_agent.py`)

A LangChain-powered agent that can:

- **📁 List files** in directories
- **📖 Read file contents** and summarize
- **🔍 Answer questions** about file data
- **🧭 Navigate** directory structures

**Example Usage:**

```bash
# Direct agent usage
python examples/agents/file_qa_agent.py "What Python files are in this project?"

# Run with simple runner
python scripts/simple_run.py examples/agents/file_qa_agent.py

# Run rigorous multi-layer evaluation
python -m astk.cli rigorous run examples/agents/file_qa_agent.py
```

## 🧪 Benchmark Scenarios

The intelligent benchmark tests 8 diverse scenarios:

| Scenario                    | Test                               | Capability                 |
| --------------------------- | ---------------------------------- | -------------------------- |
| **📁 File Discovery**       | Find Python files and entry points | File system navigation     |
| **⚙️ Config Analysis**      | Analyze configuration files        | Technical comprehension    |
| **📖 README Comprehension** | Read and explain project           | Document analysis          |
| **🏗️ Code Structure**       | Analyze directory structure        | Architecture understanding |
| **📚 Documentation Search** | Explore documentation              | Information retrieval      |
| **🔗 Dependency Analysis**  | Analyze requirements/dependencies  | Technical analysis         |
| **💡 Example Exploration**  | Discover example code              | Code comprehension         |
| **🧪 Test Discovery**       | Find testing framework             | Development understanding  |

## 📊 Results & Metrics

Benchmarks generate comprehensive results:

```json
{
  "success_rate": 1.0,
  "total_duration_seconds": 25.4,
  "average_scenario_duration": 3.2,
  "average_response_length": 847,
  "scenarios": [...]
}
```

**Metrics Include:**

- ✅ **Success Rate**: Percentage of completed scenarios
- ⏱️ **Response Time**: Duration for each scenario
- 📝 **Response Quality**: Length and content analysis
- 🎯 **Scenario Details**: Individual query results

## 🛠️ Available Tools

### 🚀 ASTK CLI (Primary Interface)

```bash
# Initialize project with templates
python -m astk.cli init my-project

# Run rigorous multi-layer evaluation
python -m astk.cli rigorous run <agent-path>

# Generate HTML/JSON reports
python -m astk.cli report <results-dir>

# View usage examples
python -m astk.cli examples
```

### 🧪 Legacy Script Runners (Still Supported)

```bash
# Direct benchmark execution
python scripts/simple_benchmark.py <agent-path>

# Basic agent runner
python scripts/simple_run.py <agent-path>
```

## 🏗️ Project Structure

```
ASTK/
├── 🤖 examples/
│   ├── agents/                  # Example AI agents
│   │   └── file_qa_agent.py     # LangChain File Q&A agent
│   └── benchmarks/scenarios/    # Rigorous evaluation scenarios
│       └── rigorous_multilayer_scenarios.yaml  # NEW! 9 expert scenarios
├── 📊 scripts/                  # Benchmark and utility scripts
│   ├── simple_benchmark.py      # Intelligent benchmark runner ⭐
│   ├── simple_run.py            # Basic agent runner
│   └── astk.py                  # Advanced CLI (WIP)
├── 🧠 astk/                     # Core ASTK framework
│   ├── benchmarks/              # Benchmark modules
│   ├── cli.py                   # Command-line interface ⭐ NEW: Rigorous commands
│   ├── evals_integration.py     # OpenAI Evals integration ⭐ Enhanced
│   ├── schema.py                # Data schemas ⭐ Enhanced for multi-layer
│   └── *.py                     # Core modules
├── 📁 benchmark_results/        # Generated benchmark results
├── ⚙️ config/                   # Configuration files
└── 📖 docs/                     # Documentation
```

## 🎮 Usage Examples

### Run Agent Directly

```bash
python examples/agents/file_qa_agent.py "Analyze the setup.py file"
```

### Quick Agent Test

```bash
python scripts/simple_run.py examples/agents/file_qa_agent.py
```

### Full Intelligence Benchmark

```bash
python scripts/simple_benchmark.py examples/agents/file_qa_agent.py
```

### Rigorous Multi-Layer Evaluation

```bash
# Complete rigorous evaluation
python -m astk.cli rigorous run examples/agents/file_qa_agent.py

# With custom parameters
python -m astk.cli rigorous run examples/agents/file_qa_agent.py \
  --evaluators gpt-4 o1-preview \
  --max-cost 10.0 \
  --output-format detailed \
  --save-results
```

### Custom Queries

```bash
python examples/agents/file_qa_agent.py "What is the purpose of the astk directory?"
```

## 🔧 Troubleshooting

### Common Issues

**📦 Installation Problems**

```bash
# Update pip and reinstall
pip install --upgrade pip
pip install --upgrade agent-sprint-testkit

# Verify installation
python -m astk.cli --version
python -c "import astk; print('ASTK loaded successfully')"
```

**🛠️ CLI Command Issues**

For 100% reliable CLI usage that works across all environments:

```bash
# Always use this format (recommended)
python -m astk.cli benchmark examples/agents/file_qa_agent.py
python -m astk.cli rigorous run examples/agents/file_qa_agent.py

# Instead of this (may fail with PATH issues)
astk benchmark examples/agents/file_qa_agent.py
```

📖 **See [RELIABLE_CLI_USAGE.md](RELIABLE_CLI_USAGE.md) for complete CLI guidance**

**🔑 OpenAI API Issues**

```bash
# Verify API key is set
echo $OPENAI_API_KEY

# Set API key
export OPENAI_API_KEY="sk-..."

# Test API access
python -c "import openai; print('OpenAI client ready')"
```

**💰 Cost Management for Rigorous Evaluation**

```bash
# Check estimated costs before running
python -m astk.cli rigorous run my_agent.py --dry-run

# Set strict cost limits
python -m astk.cli rigorous run my_agent.py --max-cost 5.0

# Use fewer evaluators to reduce costs
python -m astk.cli rigorous run my_agent.py --evaluators gpt-4
```

**🐍 Development Environment Issues**

```bash
# For development setup
git clone https://github.com/your-org/astk.git
cd astk
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e .[evals,dev]
```

**🤖 Agent Compatibility**

The framework supports multiple agent types:

- **CLI agents**: Accept queries as command-line arguments
- **Python modules**: Have a `chat()` method
- **REST APIs**: Expose `/chat` endpoint
- **Custom formats**: Use adapter patterns as needed

## 🚀 Creating Your Own Agent

Create a new agent that responds to command-line arguments:

```python
#!/usr/bin/env python3
import sys

async def main():
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        # Process query and return response
        print(f"Agent: {response}")
    else:
        # Default behavior
        print("Agent: Ready!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```

Then benchmark it:

```bash
# Traditional benchmark
python scripts/simple_benchmark.py path/to/your_agent.py

# Rigorous multi-layer evaluation
python -m astk.cli rigorous run path/to/your_agent.py
```

## 📈 Performance Tips

- **⚡ Faster Responses**: Use GPT-3.5-turbo for speed
- **🧠 Better Intelligence**: Use GPT-4 for complex reasoning
- **💰 Cost Optimization**: Monitor token usage and use `--max-cost` limits
- **🔧 Custom Scenarios**: Create domain-specific rigorous scenarios
- **⚡ Parallel Processing**: Use `--parallel` for faster rigorous evaluation
- **🎯 Targeted Testing**: Use specific scenario categories for focused evaluation

## 🤝 Contributing

1. Create new agents in `examples/agents/`
2. Add benchmark scenarios in `scripts/simple_benchmark.py`
3. Create rigorous scenarios in `examples/benchmarks/scenarios/`
4. Test with: `python -m astk.cli rigorous run your_agent.py`

## 📄 License

Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License

For commercial use or derivative works, please contact: admin@blackbox-dev.com  
See LICENSE file for complete details.

---

**🎯 Ready to benchmark your AI agents? Start with:**

```bash
# Install globally
pip install agent-sprint-testkit[evals]

# Quick benchmark
python -m astk.cli benchmark examples/agents/file_qa_agent.py

# Professional rigorous evaluation
python -m astk.cli rigorous run examples/agents/file_qa_agent.py

# Enterprise OpenAI Evals integration
python -m astk.cli evals create my_agent.py --grader gpt-4
```

**🚀 Get started in 3 commands:**

```bash
pip install agent-sprint-testkit[evals]
python -m astk.cli init my-tests
python -m astk.cli rigorous run examples/agents/file_qa_agent.py
```
