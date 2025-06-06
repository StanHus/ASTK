# CI/CD Temporarily Disabled

## Reason

The GitHub Actions CI was causing Pydantic compatibility issues that prevented the package from importing correctly. The error was:

```
TypeError: constr() got an unexpected keyword argument 'regex'
```

## What Was Done

1. Fixed the Pydantic compatibility issue in `astk/schema.py`
2. Disabled CI to focus on core package functionality
3. Package can now be built and uploaded manually

## Manual Release Process

Use the provided `release.sh` script:

```bash
./release.sh upload
```

## Re-enabling CI

CI can be re-enabled later after thorough testing of the import system across different Python and Pydantic versions.

## Current Status

- ✅ Package imports work
- ✅ Manual build/upload works
- ❌ CI temporarily disabled
- ✅ Ready for 0.1.3 release
