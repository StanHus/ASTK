# ASTK + OpenAI Evals API Integration Proposal

## 🌟 Vision

Transform ASTK from a basic benchmarking tool into a sophisticated AI agent evaluation platform powered by OpenAI's new Evals API.

## 🔄 Current vs Future State

### Current ASTK (v0.1.3)

```python
# Basic pattern matching
success_criteria = {
    "regex": "(?i)here's",
    "semantic_score": 0.8
}
```

### Future ASTK with Evals API

```python
# AI-powered evaluation with detailed scoring
evaluation_criteria = {
    "type": "score_model",
    "model": "o3",
    "grader_prompt": custom_grader_prompt,
    "range": [1, 10],
    "dimensions": ["accuracy", "completeness", "clarity", "usefulness"]
}
```

## 🛠️ Implementation Plan

### Phase 1: Core Integration

Add OpenAI Evals API support to ASTK:

```python
# New astk/evals_integration.py
class OpenAIEvalsAdapter:
    def __init__(self, client: openai.OpenAI):
        self.client = client

    def create_eval_from_astk_scenarios(self, scenarios: List[ScenarioConfig]):
        """Convert ASTK scenarios to OpenAI Evals format"""
        return self.client.evals.create(
            name="ASTK Agent Evaluation",
            data_source_config={"type": "logs"},
            testing_criteria=self._build_criteria_from_scenarios(scenarios)
        )

    def run_comparative_evaluation(self, baseline_agent: str, test_agent: str):
        """Compare two agents using OpenAI Evals"""
        # Implementation here
```

### Phase 2: Enhanced Grading

Replace basic regex/semantic matching with AI-powered grading:

```python
# Enhanced grader prompts for different agent types
AGENT_GRADER_PROMPTS = {
    "code_qa": """
    You are evaluating an AI agent's ability to answer questions about code.

    Score on these dimensions:
    1. **Technical Accuracy (40%)** - Correctness of code analysis
    2. **Completeness (30%)** - Coverage of relevant details
    3. **Clarity (20%)** - Clear, well-structured explanation
    4. **Practicality (10%)** - Actionable insights and context

    Return JSON with detailed scoring...
    """,

    "general_reasoning": """
    You are evaluating an AI agent's reasoning capabilities.

    Score on these dimensions:
    1. **Logical Consistency (35%)** - Sound reasoning process
    2. **Problem Decomposition (25%)** - Breaking down complex issues
    3. **Evidence Usage (25%)** - Proper use of given information
    4. **Conclusion Quality (15%)** - Well-supported final answers

    Return JSON with detailed scoring...
    """
}
```

### Phase 3: Advanced Features

#### A. Automatic Agent Comparison

```python
# New CLI command
astk compare baseline_agent.py test_agent.py --eval-type code_qa
```

#### B. Logs-Based Evaluation

```python
# Evaluate based on existing agent logs
astk eval-from-logs --agent-name my_agent --days 7 --grader o3
```

#### C. Continuous Evaluation

```python
# Monitor agent performance over time
astk monitor my_agent.py --eval-frequency daily --alert-threshold 6.0
```

## 📊 New ASTK Architecture

```
ASTK v2.0 Architecture:
┌─────────────────────────────────────────────────────┐
│                    ASTK Core                        │
├─────────────────────────────────────────────────────┤
│  Agent Runners  │  Scenario Engine  │  Collectors   │
├─────────────────────────────────────────────────────┤
│               OpenAI Evals Integration              │
├─────────────────────────────────────────────────────┤
│  Grader Prompts │ Eval Management │ Comparative      │
│                 │                 │ Analysis         │
├─────────────────────────────────────────────────────┤
│            Enhanced Reporting Engine                │
├─────────────────────────────────────────────────────┤
│ Dashboard │ Trend Analysis │ Performance Alerts      │
└─────────────────────────────────────────────────────┘
```

## 🎯 Benefits

### For Developers

- **Professional-grade evaluation** using OpenAI's infrastructure
- **Detailed scoring** with explanations for each dimension
- **Easy A/B testing** between agent versions
- **Automated grading** removes subjective bias

### For Teams

- **Standardized evaluation** across projects
- **Historical tracking** of agent performance
- **Collaborative evaluation** with shared standards
- **Cost-effective** by leveraging existing logs

## 🚀 Migration Path

### Immediate (v0.1.4)

```python
# Add basic OpenAI Evals support
pip install agent-sprint-testkit[evals]

# New evaluation command
astk eval-openai my_agent.py --grader gpt-4 --criteria accuracy,clarity
```

### Near-term (v0.2.0)

- Full Evals API integration
- Pre-built grader prompts for common agent types
- Comparative evaluation dashboard
- Logs-based evaluation

### Long-term (v0.3.0)

- Real-time monitoring and alerting
- Custom evaluation pipelines
- Integration with popular agent frameworks
- Enterprise features (team management, etc.)

## 📋 Technical Requirements

### Dependencies

```python
# Additional requirements for Evals integration
openai>=1.50.0  # Latest with Evals API
pandas>=2.0.0   # For data analysis
plotly>=5.0.0   # For interactive charts
```

### Configuration

```yaml
# astk.yaml
evals:
  openai_api_key: ${OPENAI_API_KEY}
  default_grader: "gpt-4"
  evaluation_dimensions:
    - accuracy
    - completeness
    - clarity
    - usefulness
  pass_threshold: 6.0
```

## 💡 Example Use Cases

### 1. Code QA Agent Evaluation

```python
astk eval my_code_qa_agent.py \
  --eval-type code_analysis \
  --grader o3 \
  --compare-to baseline_agent.py
```

### 2. Customer Support Agent Testing

```python
astk eval support_agent.py \
  --eval-type customer_service \
  --criteria "helpfulness,accuracy,empathy" \
  --from-logs --days 30
```

### 3. Research Assistant Evaluation

```python
astk eval research_agent.py \
  --eval-type research_quality \
  --grader gpt-4 \
  --benchmark industry_standard
```

## 🎉 Impact

This integration would position ASTK as:

- **Industry-leading** agent evaluation platform
- **Production-ready** for enterprise use
- **Cost-effective** by leveraging OpenAI infrastructure
- **Comprehensive** covering all aspects of agent performance

The combination of ASTK's scenario management with OpenAI's professional evaluation infrastructure creates a powerful, comprehensive agent testing solution that goes far beyond current offerings.

## Next Steps

1. **Prototype** basic OpenAI Evals integration (1-2 weeks)
2. **Design** new CLI interface and configuration system
3. **Implement** grader prompt library for common agent types
4. **Beta test** with select users
5. **Launch** ASTK v0.2.0 with full Evals integration

This would make ASTK the go-to tool for professional AI agent evaluation and testing.
