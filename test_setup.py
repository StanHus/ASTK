#!/usr/bin/env python3
"""
ASTK Setup Test Script
======================

Quick verification that ASTK environment is properly configured.
"""

import sys
import subprocess
from pathlib import Path


def test_python_version():
    """Test Python version"""
    print("🐍 Testing Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 11:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(
            f"❌ Python {version.major}.{version.minor}.{version.micro} - Need Python 3.11+")
        return False


def test_dependencies():
    """Test required dependencies"""
    print("\n📦 Testing dependencies...")

    packages = [
        "langchain",
        "langchain_openai",
        "langchain_core",
        "pydantic",
        "click"
    ]

    success = True
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package} - OK")
        except ImportError:
            print(f"❌ {package} - MISSING")
            success = False

    return success


def test_openai_key():
    """Test OpenAI API key"""
    print("\n🔑 Testing OpenAI API key...")
    import os

    key = os.getenv("OPENAI_API_KEY")
    if key and key.startswith("sk-"):
        print("✅ OPENAI_API_KEY - OK")
        return True
    else:
        print("❌ OPENAI_API_KEY - Missing or invalid")
        print("   Set with: export OPENAI_API_KEY='your-key-here'")
        return False


def test_file_structure():
    """Test file structure"""
    print("\n📁 Testing file structure...")

    required_files = [
        "examples/agents/file_qa_agent.py",
        "scripts/simple_benchmark.py",
        "scripts/simple_run.py",
        "astk/__init__.py"
    ]

    success = True
    for file_path in required_files:
        if Path(file_path).exists():
            print(f"✅ {file_path} - OK")
        else:
            print(f"❌ {file_path} - MISSING")
            success = False

    return success


def test_agent():
    """Test the example agent"""
    print("\n🤖 Testing File Q&A Agent...")

    try:
        result = subprocess.run([
            sys.executable,
            "examples/agents/file_qa_agent.py",
            "test"
        ], capture_output=True, text=True, timeout=30)

        if result.returncode == 0:
            print("✅ File Q&A Agent - OK")
            return True
        else:
            print("❌ File Q&A Agent - ERROR")
            print(f"   Error: {result.stderr}")
            return False

    except Exception as e:
        print(f"❌ File Q&A Agent - ERROR: {e}")
        return False


def main():
    """Run all tests"""
    print("🚀 ASTK Setup Test")
    print("=" * 50)

    tests = [
        test_python_version,
        test_dependencies,
        test_openai_key,
        test_file_structure,
        test_agent
    ]

    results = []
    for test in tests:
        results.append(test())

    print("\n" + "=" * 50)
    print("📊 Test Summary")
    print("=" * 50)

    passed = sum(results)
    total = len(results)

    if passed == total:
        print("🎉 ALL TESTS PASSED!")
        print("\n🚀 Ready to run benchmarks:")
        print("   python scripts/simple_benchmark.py examples/agents/file_qa_agent.py")
    else:
        print(f"⚠️  {passed}/{total} tests passed")
        print("\n🔧 Fix the issues above and run again.")

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
