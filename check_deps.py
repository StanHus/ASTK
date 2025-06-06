#!/usr/bin/env python3
"""
Simple dependency check script
"""


def check_imports():
    """Check if all required imports work"""
    failed_imports = []

    # Test basic imports
    try:
        import yaml
        print("✓ pyyaml")
    except ImportError as e:
        failed_imports.append(f"pyyaml: {e}")

    try:
        import pydantic
        print("✓ pydantic")
    except ImportError as e:
        failed_imports.append(f"pydantic: {e}")

    try:
        import click
        print("✓ click")
    except ImportError as e:
        failed_imports.append(f"click: {e}")

    try:
        import requests
        print("✓ requests")
    except ImportError as e:
        failed_imports.append(f"requests: {e}")

    try:
        import aiohttp
        print("✓ aiohttp")
    except ImportError as e:
        failed_imports.append(f"aiohttp: {e}")

    try:
        import psutil
        print("✓ psutil")
    except ImportError as e:
        failed_imports.append(f"psutil: {e}")

    # Test ASTK imports
    try:
        import astk
        print(f"✓ astk (version {astk.__version__})")
    except ImportError as e:
        failed_imports.append(f"astk: {e}")

    try:
        from astk.schema import ScenarioConfig
        print("✓ astk.schema")
    except ImportError as e:
        failed_imports.append(f"astk.schema: {e}")

    if failed_imports:
        print("\n❌ Failed imports:")
        for fail in failed_imports:
            print(f"  {fail}")
        return False
    else:
        print("\n✅ All imports successful!")
        return True


if __name__ == "__main__":
    success = check_imports()
    exit(0 if success else 1)
