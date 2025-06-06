# ASTK v0.2.0 Release Summary

## 🚀 Major Release: OpenAI Evals Integration

**Release Date**: December 28, 2024  
**Version**: 0.2.0  
**Status**: Beta (Development Status 4)

## 🎯 What's New

### **🌟 OpenAI Evals API Integration**

ASTK now integrates with OpenAI's professional Evals API, transforming it from a basic testing tool into a sophisticated evaluation platform.

#### **New CLI Commands**

```bash
# Create professional evaluations
astk evals create my_agent.py --eval-type code_qa --grader gpt-4

# Run evaluations from logs
astk evals run eval_12345

# Compare models A/B testing
astk evals compare eval_12345 gpt-4o-mini gpt-4-turbo
```

#### **Professional Grader Prompts**

- **Code QA**: Expert software engineer evaluation
- **Customer Service**: Professional customer support assessment
- **Research**: Academic-quality research evaluation
- **General**: Comprehensive all-purpose grading

#### **Evaluation Types**

- `general` - General-purpose evaluation
- `code_qa` - Code analysis and Q&A
- `customer_service` - Customer support scenarios
- `research` - Research and analysis tasks

#### **Grader Models**

- `gpt-4` - Comprehensive evaluation
- `gpt-4-turbo` - Fast professional grading
- `o3` - Latest OpenAI model
- `o3-mini` - Cost-effective option

## 📦 Package Updates

### **Version Synchronization**

- ✅ `setup.py`: 0.1.3 → 0.2.0
- ✅ `astk/__init__.py`: 0.1.3 → 0.2.0
- ✅ `astk/cli.py`: 0.1.3 → 0.2.0
- ✅ `pyproject.toml`: 0.1.3 → 0.2.0
- ✅ `tests/test_imports.py`: 0.1.3 → 0.2.0

### **Development Status**

- **Before**: Alpha (Development Status 3)
- **After**: Beta (Development Status 4)

### **Enhanced Description**

- **Before**: "AgentSprint TestKit - Benchmark your AI agents"
- **After**: "AgentSprint TestKit - Professional AI agent evaluation with OpenAI Evals integration"

### **Python Version Support**

- **Before**: Python 3.11+
- **After**: Python 3.9+ (broader compatibility)

## 🔧 Technical Changes

### **New Dependencies**

Added optional `evals` dependency group:

```python
"evals": [
    "openai>=1.50.0",
    "pandas>=2.0.0",
    "plotly>=5.0.0",
    "numpy>=1.24.0",
]
```

### **Enhanced Package Exports**

```python
# Core exports (always available)
from astk import ScenarioConfig, PersonaConfig, SuccessCriteria

# Optional exports (if openai installed)
from astk import OpenAIEvalsAdapter
```

### **Fixed CLI Issues**

- ✅ Resolved `run_benchmark_cli` import error
- ✅ Fixed benchmark command to call scripts properly
- ✅ Enhanced error handling and user feedback

## 📚 New Documentation

### **Comprehensive Guides**

- 📖 `OPENAI_EVALS_INTEGRATION.md` - Complete integration guide
- 📈 `EVALS_TRANSFORMATION_SUMMARY.md` - Business impact analysis
- 💻 `examples/evals_example.py` - Working integration demo
- 📋 Updated `README.md` with Evals examples

### **Updated Configuration**

- 🔧 `pyproject.toml` - Enhanced metadata and dependencies
- 📝 `CHANGELOG.md` - Comprehensive v0.2.0 changelog
- ✅ `tests/test_imports.py` - New evals integration tests

## 🚀 Installation & Usage

### **Standard Installation**

```bash
pip install agent-sprint-testkit
```

### **With OpenAI Evals Support**

```bash
pip install "agent-sprint-testkit[evals]"
```

### **Development Installation**

```bash
pip install -e ".[evals,dev]"
```

### **Quick Start**

```bash
# Set API key
export OPENAI_API_KEY="your-key-here"

# Create evaluation
astk evals create examples/agents/file_qa_agent.py --eval-type code_qa

# Traditional benchmark (still works)
astk benchmark examples/agents/file_qa_agent.py
```

## 🎯 Backward Compatibility

✅ **Full backward compatibility maintained**

- All existing CLI commands work unchanged
- All existing APIs remain functional
- No breaking changes introduced
- Optional dependencies don't affect core functionality

## 🌟 Key Benefits

### **For Developers**

- 🏆 Professional-grade evaluation using OpenAI infrastructure
- 🎯 AI-powered grading with detailed explanations
- ⚖️ Easy A/B testing between agent versions
- 📊 Industry-standard evaluation methodology

### **For Organizations**

- 💰 Cost-effective by leveraging existing logs
- 📈 Scalable professional evaluation platform
- 🔧 Easy integration with existing workflows
- 🎓 Standardized evaluation across teams

## 🚀 What's Next

### **Immediate Benefits**

- Start using professional evaluations today
- Leverage OpenAI's infrastructure for quality assessment
- Compare agent performance with industry standards
- Get detailed feedback for agent improvements

### **Future Roadmap**

- Real-time monitoring and alerting
- Custom evaluation pipelines
- Enterprise features and team management
- Integration with popular agent frameworks

---

**🎉 ASTK v0.2.0 transforms agent testing from basic benchmarking to professional evaluation!**

**Try it now:**

```bash
pip install "agent-sprint-testkit[evals]"
astk evals create my_agent.py --eval-type code_qa --grader gpt-4
```
