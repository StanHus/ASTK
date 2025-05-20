from setuptools import setup, find_packages

setup(
    name="astk",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
        "pyyaml>=6.0.0",
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "plotly>=5.0.0",
        "matplotlib>=3.4.0",
        "tabulate>=0.8.0",
        "opentelemetry-api>=1.0.0",
        "opentelemetry-sdk>=1.0.0",
        "opentelemetry-exporter-otlp>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "astk=scripts.astk:cli",
        ],
    },
    python_requires=">=3.9",
    author="Trilogy AI CoE",
    description="AgentSprint TestKit - Benchmark your AI agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/trilogy-ai/astk",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
