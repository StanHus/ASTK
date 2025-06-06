# ASTK Release Instructions - Version 0.1.3

## Summary of Changes

Version 0.1.3 includes critical fixes for CI/CD pipeline, enhanced testing infrastructure, and updated contact information.

### Key Improvements:

- ✅ Fixed all CI test failures
- ✅ Added missing `pyyaml` dependency
- ✅ Expanded Python support to 3.9+
- ✅ Enhanced test suite with better error handling
- ✅ Updated contact emails to `admin@blackbox-dev.com`
- ✅ Synchronized versions across all files

## Pre-Release Checklist

- [x] Updated version to 0.1.3 in:

  - [x] `setup.py`
  - [x] `astk/__init__.py`
  - [x] `astk/cli.py`
  - [x] `tests/test_imports.py`

- [x] Updated contact information:

  - [x] `setup.py` - author_email
  - [x] `LICENSE` - contact email

- [x] Updated documentation:

  - [x] `CHANGELOG.md` - added 0.1.3 release notes

- [x] Code quality checks:
  - [x] All tests passing locally
  - [x] Dependencies properly specified
  - [x] Import errors handled gracefully

## Build and Release Steps

### 1. Clean Previous Builds

```bash
rm -rf dist/ build/ *.egg-info/
```

### 2. Install Build Dependencies

```bash
pip install --upgrade build twine
```

### 3. Build the Package

```bash
python -m build
```

This will create:

- `dist/agent_sprint_testkit-0.1.3-py3-none-any.whl`
- `dist/agent-sprint-testkit-0.1.3.tar.gz`

### 4. Verify the Build

```bash
# Check that files were created
ls -la dist/

# Test install from wheel
pip install dist/agent_sprint_testkit-0.1.3-py3-none-any.whl --force-reinstall

# Verify installation
python -c "import astk; print(f'ASTK version: {astk.__version__}')"
astk --help
```

### 5. Upload to PyPI

```bash
# Upload to PyPI (you'll be prompted for credentials)
twine upload dist/*
```

### 6. Verify PyPI Upload

After upload, verify at: https://pypi.org/project/agent-sprint-testkit/

Test installation from PyPI:

```bash
pip uninstall agent-sprint-testkit -y
pip install agent-sprint-testkit==0.1.3
python -c "import astk; print(f'ASTK version: {astk.__version__}')"
```

## Post-Release Steps

### 1. Tag the Release

```bash
git add .
git commit -m "Release version 0.1.3 - CI fixes and enhancements"
git tag v0.1.3
git push origin main
git push origin v0.1.3
```

### 2. Create GitHub Release

1. Go to https://github.com/stanhus/ASTK/releases
2. Click "Create a new release"
3. Tag: `v0.1.3`
4. Title: `ASTK v0.1.3 - CI Fixes and Enhanced Testing`
5. Description:

```markdown
## 🚀 ASTK v0.1.3 - CI Fixes and Enhanced Testing

This release resolves critical CI/CD pipeline issues and enhances the testing infrastructure.

### 🔧 Fixed

- Resolved all GitHub Actions test failures
- Added missing `pyyaml` dependency
- Fixed Python version compatibility (now supports 3.9+)
- Synchronized package versions across all files
- Enhanced import error handling

### ✨ Added

- New comprehensive test suite with better diagnostics
- Dependency validation script (`check_deps.py`)
- Enhanced CI pipeline with better error reporting
- Improved test infrastructure with pytest fixtures

### 📧 Changed

- Updated contact emails to `admin@blackbox-dev.com`
- Improved CI robustness with proper fallbacks

### 🐛 Technical Improvements

- Enhanced import error handling with try/catch blocks
- Added comprehensive dependency validation
- Better CI diagnostics and troubleshooting
- More resilient test infrastructure

**Full Changelog**: https://github.com/stanhus/ASTK/compare/v0.1.2...v0.1.3
```

### 3. Update Documentation

Ensure all documentation references the new version and the updated contact information.

## Rollback Plan

If issues are discovered:

1. **Quick Fix**: Upload a patch version (0.1.4) with fixes
2. **Major Issues**: Yank the release from PyPI:
   ```bash
   # Contact PyPI support or use web interface to yank
   ```

## Testing the Release

After release, test the installation process:

```bash
# Test in clean environment
python -m venv test_env
source test_env/bin/activate  # or test_env\Scripts\activate on Windows
pip install agent-sprint-testkit==0.1.3
python -c "import astk; print('✅ ASTK installed successfully')"
astk --help
deactivate
rm -rf test_env
```

## Notes

- **License**: Package uses Creative Commons BY-NC-ND 4.0
- **PyPI Name**: `agent-sprint-testkit`
- **Import Name**: `astk`
- **Contact**: `admin@blackbox-dev.com`
- **Repository**: https://github.com/stanhus/ASTK
