# PyPI Authentication Setup

## Issue

You're getting a "403 Forbidden" error when uploading to PyPI, which means your API token is invalid or expired.

## Solution

### Step 1: Get a New PyPI API Token

1. Go to https://pypi.org/manage/account/token/
2. Log in to your PyPI account
3. Click **"Add API token"**
4. Name: `ASTK-Upload-Token`
5. Scope: **"Entire account"** (or limit to `agent-sprint-testkit` project)
6. Click **"Add token"**
7. **COPY THE TOKEN** (it starts with `pypi-` and you won't see it again!)

### Step 2: Configure Authentication

**Option A: Using .pypirc file (Recommended)**

Edit or create `~/.pypirc`:

```ini
[distutils]
index-servers = pypi

[pypi]
username = __token__
password = pypi-YOUR_ACTUAL_TOKEN_HERE
```

**Option B: Environment Variables**

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-YOUR_ACTUAL_TOKEN_HERE
```

### Step 3: Test Authentication

```bash
# Test with a dry run
twine check dist/*

# If that works, upload
twine upload dist/*
```

## Quick Release Commands

```bash
# Make release script executable
chmod +x release.sh

# Build package only
./release.sh

# Build and upload
./release.sh upload
```

## Troubleshooting

### 403 Forbidden

- Token is invalid/expired → Generate new token
- Token has wrong scope → Make sure it covers your package
- Username/password format wrong → Use `__token__` as username

### 400 Bad Request

- Version already exists → Bump version number
- Package name conflict → Check package name

### Network Issues

- Try again later
- Check firewall/proxy settings

## Security Notes

- **Never commit** your API token to Git
- Add `~/.pypirc` to your global `.gitignore`
- Use project-scoped tokens when possible
- Regenerate tokens periodically
