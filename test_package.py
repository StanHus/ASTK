#!/usr/bin/env python3
"""
Quick test script to verify ASTK package functionality
"""


def test_imports():
    """Test that all modules can be imported"""
    try:
        import astk
        print("✅ astk package imported successfully")

        from astk.cli import cli
        print("✅ CLI module imported successfully")

        from astk import runner, schema, metrics
        print("✅ Core modules imported successfully")

        # Test CLI help
        import click.testing
        runner = click.testing.CliRunner()
        result = runner.invoke(cli, ['--help'])

        if result.exit_code == 0:
            print("✅ CLI help works")
            print(f"CLI Output preview:\n{result.output[:200]}...")
        else:
            print(f"❌ CLI failed: {result.output}")

        return True

    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False


def test_package_structure():
    """Test package structure"""
    import os
    from pathlib import Path

    required_files = [
        'astk/__init__.py',
        'astk/cli.py',
        'astk/runner.py',
        'astk/schema.py',
        'astk/metrics.py',
        'scripts/simple_benchmark.py',
        'setup.py',
        'requirements.txt',
        'README.md'
    ]

    missing = []
    for file in required_files:
        if not Path(file).exists():
            missing.append(file)

    if missing:
        print(f"❌ Missing files: {missing}")
        return False
    else:
        print("✅ All required files present")
        return True


if __name__ == "__main__":
    print("🧪 Testing ASTK Package...")
    print()

    structure_ok = test_package_structure()
    imports_ok = test_imports()

    print()
    if structure_ok and imports_ok:
        print("🎉 ASTK package is ready!")
        print()
        print("Next steps:")
        print("1. Verify PyPI upload completed")
        print("2. Test: pip install agent-sprint-testkit (in fresh environment)")
        print("3. Test: astk --help")
        print("4. Test: astk init test-project")
    else:
        print("❌ Package has issues - check errors above")
