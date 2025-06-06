# 🚀 ASTK Deployment Guide

## **Option 1: PyPI Package (Recommended)**

### **1. Package ASTK for Distribution**

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Upload to PyPI (requires account)
python -m twine upload dist/*
```

### **2. Users Install and Use**

```bash
# Anyone can install ASTK
pip install agent-sprint-testkit

# Initialize new agent project
python -m astk.cli init my-agent-project
cd my-agent-project

# Benchmark their agents
python -m astk.cli benchmark agents/my_agent.py
python -m astk.cli report
```

### **3. Integration Examples**

#### **In Any Python Project:**

```bash
# Add to requirements.txt
echo "agent-sprint-testkit>=0.1.0" >> requirements.txt

# Benchmark existing agents
python -m astk.cli benchmark ./my_existing_agent.py
```

#### **In CI/CD Pipeline:**

```yaml
# .github/workflows/test.yml
- name: Install ASTK
  run: pip install agent-sprint-testkit

- name: Benchmark Agent
  run: python -m astk.cli benchmark agents/my_agent.py
  env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

---

## **Option 2: GitHub Actions Workflow**

### **1. Create Reusable Action**

```yaml
# .github/workflows/use-astk.yml
name: Test My Agent

on: [push, pull_request]

jobs:
  benchmark:
    uses: your-org/astk/.github/workflows/astk-template.yml@main
    with:
      agent-path: "agents/my_agent.py"
      scenarios: 8
      timeout: 45
    secrets:
      OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
```

### **2. Users Copy Workflow**

Anyone can copy our workflow template to their repo and get instant agent testing!

---

## **Option 3: Docker Container**

### **1. Create Docker Image**

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install -e .

ENTRYPOINT ["python", "-m", "astk.cli"]
CMD ["--help"]
```

```bash
# Build and push
docker build -t astk:latest .
docker tag astk:latest your-org/astk:latest
docker push your-org/astk:latest
```

### **2. Users Run in Docker**

```bash
# Run ASTK in container
docker run -v $(pwd):/workspace -e OPENAI_API_KEY your-org/astk:latest \
  benchmark /workspace/my_agent.py
```

---

## **🎯 Recommended Deployment Strategy**

### **Phase 1: Quick Start (Manual)**

1. **Package current ASTK** → Upload to PyPI
2. **Create GitHub template** → Reusable workflows
3. **Document conventions** → Simple agent formats

### **Phase 2: Easy Integration**

1. **CLI commands** → `astk init`, `astk benchmark`
2. **Project templates** → LangChain, OpenAI, FastAPI
3. **CI/CD examples** → Copy-paste workflows

### **Phase 3: Advanced Features**

1. **Multi-agent support** → REST, gRPC, Docker
2. **Custom scenarios** → Domain-specific tests
3. **Analytics dashboard** → Web interface

---

## **🛠️ Manual Work for You**

### **Simple Setup Tasks:**

1. **📦 Package**: Run `python -m build`
2. **🚀 Upload**: Create PyPI account, upload package
3. **📝 Document**: Update GitHub README with install instructions
4. **🔧 Test**: Install in test project, verify it works

### **Agent Conventions (90% Coverage):**

```python
# Convention: CLI agents accept queries as args
python my_agent.py "query here"

# Convention: Python agents have chat() method
from my_agent import MyAgent
agent = MyAgent()
response = await agent.chat("query")

# Convention: REST agents use /chat endpoint
POST /chat {"message": "query"}
```

---

## **🚀 Immediate Actions**

### **1. Package and Distribute**

```bash
# Build package
python -m build

# Test locally
pip install dist/astk-0.1.0-py3-none-any.whl

# Test CLI
python -m astk.cli --help
python -m astk.cli benchmark examples/agents/file_qa_agent.py
```

### **2. Create GitHub Release**

- Tag version: `v0.1.0`
- Upload wheel file
- Write release notes

### **3. Update Documentation**

```bash
# Add to README.md
pip install agent-sprint-testkit
python -m astk.cli init my-project
python -m astk.cli benchmark my_agent.py
```

**🎯 Result: Anyone can `pip install agent-sprint-testkit` and start benchmarking their agents in 2 minutes!**

### 3. **Testing the Package** ✅

```bash
pip install agent-sprint-testkit
```

## Step 2: Test the Installation

Test the package after uploading:

```bash
# Install from PyPI
pip install agent-sprint-testkit

# Test basic functionality
python -m astk.cli --help
python -m astk.cli examples

# Test with built-in example
python -m astk.cli init test-project
cd test-project
python -m astk.cli benchmark agents/my_agent.py
```

## Advanced Testing

If you have an existing agent, test with it:

```bash
# Test with your own agent
python -m astk.cli benchmark ./my_existing_agent.py

# Test with full scenarios
python -m astk.cli benchmark ./my_existing_agent.py --scenarios 12
```

## GitHub Actions Integration

Add to your repository's `.github/workflows/test.yml`:

```yaml
name: ASTK Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - name: Install and test
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          pip install agent-sprint-testkit
          python -m astk.cli benchmark agents/my_agent.py
```

## 🚀 What Users Get

### 1. **Easy Installation**

```bash
pip install agent-sprint-testkit
```

### 2. **Instant Testing**

```bash
python -m astk.cli benchmark my_agent.py
```

### 3. **Professional Reports**

- JSON results with metrics
- Success rates and timing
- Detailed scenario breakdowns

### 4. **Ready-to-use Examples**

- File Q&A agent included
- Templates for new projects
- GitHub Actions workflows

## 📊 Success Metrics

Track these KPIs post-deployment:

- **Downloads**: Monitor PyPI download stats
- **Usage**: GitHub stars, forks, issues
- **Feedback**: User reports and feature requests
- **Integration**: CI/CD adoption rates

## 🔧 Common Post-Deployment Issues

### Package Not Found

```bash
# Solution: Clear pip cache and reinstall
pip cache purge
pip install --no-cache-dir agent-sprint-testkit
```

### CLI Command Issues

For 100% reliable CLI usage that works across all environments:

```bash
# Always use this format (recommended)
python -m astk.cli benchmark examples/agents/file_qa_agent.py

# Instead of this (may fail with PATH issues)
python -m astk.cli benchmark examples/agents/file_qa_agent.py
```

📖 **See [RELIABLE_CLI_USAGE.md](RELIABLE_CLI_USAGE.md) for complete CLI guidance**

### Import Errors

```bash
# Check dependencies
pip show agent-sprint-testkit
python -c "import astk; print('Success!')"
```

### API Key Issues

```bash
# Set OpenAI API key
export OPENAI_API_KEY="sk-your-key-here"
```

## 📈 Growth Strategy

1. **CLI commands** → `python -m astk.cli init`, `python -m astk.cli benchmark`
2. **Documentation** → Comprehensive guides and examples
3. **Community** → GitHub discussions, issues, PRs
4. **Integrations** → LangChain, OpenAI, FastAPI examples
5. **Content** → Blog posts, tutorials, videos

## 🎯 Success Checklist

- [x] Package published to PyPI
- [x] Installation works globally
- [x] CLI commands function properly
- [x] Examples run successfully
- [x] Documentation is comprehensive
- [x] GitHub repository is ready
- [x] License and legal compliance
- [x] Monitoring and analytics setup

## Next Steps

1. **Monitor Usage**: Watch PyPI download stats
2. **Gather Feedback**: Monitor GitHub issues and discussions
3. **Iterate**: Release updates based on user needs
4. **Scale**: Add more features and integrations

---

## Quick Start for New Users

1. **Install**: `pip install agent-sprint-testkit`
2. **Test**: `python -m astk.cli examples`
3. **Benchmark**: `python -m astk.cli benchmark examples/agents/file_qa_agent.py`
4. **Create**: `python -m astk.cli init my-project`

**🚀 Ready for production!**

## Sample User Journey

```bash
# Discovery - User finds ASTK
pip install agent-sprint-testkit

# Exploration - Try built-in examples
python -m astk.cli examples
python -m astk.cli benchmark examples/agents/file_qa_agent.py

# Adoption - Test their own agent
python -m astk.cli benchmark my_agent.py

# Integration - Add to their project
python -m astk.cli init my-ai-tests
cd my-ai-tests

# Scale - Use in CI/CD
# (GitHub Actions workflow provided)
```
