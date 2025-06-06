# 🧪 Post-Upload Verification Guide

## **After PyPI Upload - Complete These Tests**

### **1. Verify Package is Live**

```bash
# Check package exists on PyPI
curl -s https://pypi.org/pypi/astk/json | jq .info.version

# Should return: "0.1.0"
```

### **2. Test Fresh Installation**

```bash
# Create fresh environment
cd /tmp
python3 -m venv test_astk_install
source test_astk_install/bin/activate

# Install from PyPI
pip install agent-sprint-testkit

# Test CLI
python -m astk.cli --help
python -m astk.cli --version
```

### **3. Test Project Creation**

```bash
# Test project initialization
python -m astk.cli init test-project
cd test-project

# Verify structure created
ls -la
# Should see: agents/ tests/ .github/ README.md requirements.txt

# Test the generated agent
python agents/my_agent.py "Hello world"
# Should output: Agent: Agent response to: Hello world
```

### **4. Test Benchmarking**

```bash
# Test benchmark command (will fail without OpenAI key, but should show proper error)
python -m astk.cli benchmark agents/my_agent.py
# Should show help/error about missing OPENAI_API_KEY

# With API key:
export OPENAI_API_KEY="your-key-here"
python -m astk.cli benchmark agents/my_agent.py --scenarios 3
```

### **5. Verify GitHub Workflow**

```bash
# Check generated workflow
cat .github/workflows/astk.yml
# Should contain proper GitHub Actions syntax
```

### View Results

```bash
python -m astk.cli report
```

---

## **🎯 Success Criteria**

✅ **Package installs globally**: `pip install agent-sprint-testkit` works  
✅ **Scripts work**: All entry points function correctly  
✅ **Dependencies resolve**: No conflicts during installation  
✅ **CLI available globally**: Commands work from any directory  
✅ **Documentation accurate**: README matches actual behavior

---

## **🚀 User Documentation (README Update)**

Once verified, add this to your main README.md:

````markdown
## 🚀 Quick Start

### Install ASTK

```bash
pip install agent-sprint-testkit
```
````

### Create Your First Agent Project

```bash
python -m astk.cli init my-ai-agent
cd my-ai-agent
```

### Benchmark Your Agent

```bash
export OPENAI_API_KEY="your-key"
python -m astk.cli benchmark agents/my_agent.py
```

### View Results

```bash
python -m astk.cli report
```
