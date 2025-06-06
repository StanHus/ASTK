#!/bin/bash
# ASTK Release Script - Version 0.1.3

set -e  # Exit on any error

echo "🚀 ASTK Release Script v0.1.3"
echo "=============================="

# Check if we're in the right directory
if [ ! -f "setup.py" ]; then
    echo "❌ Error: setup.py not found. Are you in the ASTK directory?"
    exit 1
fi

# Get version from setup.py
VERSION=$(python -c "import re; print(re.search(r'version=[\"\']([^\"\']+)[\"\']', open('setup.py').read()).group(1))")

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info/

# Install/upgrade build tools
echo "📦 Installing build dependencies..."
pip install --upgrade build twine

# Build the package
echo "🔨 Building package..."
python -m build

# Check if build was successful
if [ ! -d "dist/" ]; then
    echo "❌ Error: Build failed - dist/ directory not created"
    exit 1
fi

echo "✅ Build successful!"
echo "📁 Created files:"
ls -la dist/

# Verify the package can be imported
echo "🔍 Testing package import..."
pip install "dist/agent_sprint_testkit-${VERSION}-py3-none-any.whl" --force-reinstall --quiet

if python -c "import astk; print(f'✅ ASTK version: {astk.__version__}')"; then
    echo "✅ Package import test passed"
else
    echo "❌ Package import test failed"
    exit 1
fi

echo ""
echo "🎉 Package ready for upload!"
echo ""
echo "Next steps:"
echo "1. Make sure your PyPI token is configured in ~/.pypirc"
echo "2. Run: twine upload dist/*"
echo "3. Or run this script with 'upload' argument: ./release.sh upload"

# If 'upload' argument provided, attempt upload
if [ "$1" = "upload" ]; then
    echo ""
    echo "🚀 Uploading to PyPI..."
    twine upload dist/*
    
    if [ $? -eq 0 ]; then
        echo "✅ Upload successful!"
        echo "🌐 Package available at: https://pypi.org/project/agent-sprint-testkit/"
    else
        echo "❌ Upload failed. Check your PyPI credentials."
        exit 1
    fi
fi 