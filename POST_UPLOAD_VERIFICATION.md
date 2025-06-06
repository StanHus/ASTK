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
astk --help
astk examples
```

### **3. Test Project Creation**

```bash
# Test project initialization
astk init test-agent-project
cd test-agent-project

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
astk benchmark agents/my_agent.py
# Should show help/error about missing OPENAI_API_KEY

# With API key:
export OPENAI_API_KEY="your-key-here"
astk benchmark agents/my_agent.py --scenarios 3
```

### **5. Verify GitHub Workflow**

```bash
# Check generated workflow
cat .github/workflows/astk.yml
# Should contain proper GitHub Actions syntax
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
astk init my-ai-agent
cd my-ai-agent
```

### Benchmark Your Agent

```bash
export OPENAI_API_KEY="your-key"
astk benchmark agents/my_agent.py
```

### View Results

```bash
astk report
```

```

---

## **🔧 Troubleshooting**

### **Import Errors**
If you see import errors, check:
1. Package was uploaded with all dependencies
2. `scripts/simple_benchmark.py` is included in package
3. All astk submodules exist

### **CLI Not Found**
If `astk` command not found:
1. Check entry points in setup.py
2. Reinstall: `pip uninstall agent-sprint-testkit && pip install agent-sprint-testkit`
3. Verify with: `python -c "import astk.cli; print('OK')"`

### **Permission Errors**
If upload failed:
1. Verify PyPI token has correct permissions
2. Check package name not already taken
3. Try: `python -m twine upload --verbose dist/*`

---

## **🎉 Next Steps After Verification**

1. **📝 Update main README** with installation instructions
2. **🏷️ Create GitHub release** (tag v0.1.0)
3. **📢 Announce** to potential users
4. **📊 Monitor** download statistics on PyPI
5. **🐛 Fix** any issues reported by early users

### **If Package Installation Fails:**

1. **Check PyPI status**: Verify package uploaded correctly
2. Reinstall: `pip uninstall agent-sprint-testkit && pip install agent-sprint-testkit`
3. **Clear pip cache**: `pip cache purge`
4. **Try specific version**: `pip install agent-sprint-testkit==0.1.1`
```
