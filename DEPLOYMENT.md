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
astk init my-agent-project
cd my-agent-project

# Benchmark their agents
astk benchmark agents/my_agent.py
astk report
```

### **3. Integration Examples**

#### **In Any Python Project:**

```bash
# Add to requirements.txt
echo "agent-sprint-testkit>=0.1.0" >> requirements.txt

# Benchmark existing agents
astk benchmark ./my_existing_agent.py
```

#### **In CI/CD Pipeline:**

```yaml
# .github/workflows/test.yml
- name: Install ASTK
  run: pip install agent-sprint-testkit

- name: Benchmark Agent
  run: astk benchmark agents/my_agent.py
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

ENTRYPOINT ["astk"]
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
astk --help
astk benchmark examples/agents/file_qa_agent.py
```

### **2. Create GitHub Release**

- Tag version: `v0.1.0`
- Upload wheel file
- Write release notes

### **3. Update Documentation**

```bash
# Add to README.md
pip install agent-sprint-testkit
astk init my-project
astk benchmark my_agent.py
```

**🎯 Result: Anyone can `pip install agent-sprint-testkit` and start benchmarking their agents in 2 minutes!**

### 3. **Testing the Package** ✅

```bash
pip install agent-sprint-testkit
```
