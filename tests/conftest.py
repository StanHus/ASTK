"""
Pytest configuration and shared fixtures
"""

import pytest
from pathlib import Path
import yaml

from astk.schema import ScenarioConfig


@pytest.fixture
def sample_scenario_file(tmp_path):
    """Create a sample scenario file for testing"""
    scenario = {
        "task": "file_qna",
        "persona": {
            "archetype": "impatient_mobile_user",
            "temperature": 0.9
        },
        "protocol": "A2A",
        "success": {
            "regex": "(?i)here's"
        },
        "budgets": {
            "latency_ms": 3000
        },
        "chaos": [
            "drop_tool:search",
            "inject_latency:1500"
        ]
    }

    file_path = tmp_path / "scenario.yaml"
    with open(file_path, "w") as f:
        yaml.dump(scenario, f)

    return file_path


@pytest.fixture
def sample_scenario_config():
    """Create a sample scenario config for testing"""
    return ScenarioConfig(
        task="file_qna",
        persona={
            "archetype": "impatient_mobile_user",
            "temperature": 0.9
        },
        protocol="A2A",
        success={
            "regex": "(?i)here's"
        },
        budgets={
            "latency_ms": 3000
        },
        chaos=[
            "drop_tool:search",
            "inject_latency:1500"
        ]
    )


@pytest.fixture
def sample_agent_file(tmp_path):
    """Create a sample agent file for testing"""
    agent_code = '''
def main():
    """Sample agent entry point"""
    return "Hello from test agent"

if __name__ == "__main__":
    main()
'''

    file_path = tmp_path / "agent.py"
    file_path.write_text(agent_code)

    return file_path
