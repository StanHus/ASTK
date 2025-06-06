#!/usr/bin/env python3
"""
Example: Using ASTK with OpenAI Evals API

This example demonstrates how to use ASTK's new OpenAI Evals integration
to create professional-grade agent evaluations.

Requirements:
    pip install agent-sprint-testkit[evals]
    
Environment:
    export OPENAI_API_KEY=your_api_key_here
"""

import asyncio
import os
from typing import List

from astk.evals_integration import OpenAIEvalsAdapter, GRADER_PROMPTS
from astk.schema import ScenarioConfig, PersonaConfig, SuccessCriteria


class ExampleCodeQAAgent:
    """Example agent that answers code-related questions"""

    def __init__(self):
        self.knowledge_base = {
            "python": "Python is a high-level programming language known for its simplicity and readability.",
            "functions": "Functions are reusable blocks of code that perform specific tasks.",
            "classes": "Classes are blueprints for creating objects with attributes and methods.",
        }

    async def process_query(self, query: str) -> str:
        """Process a code-related query and return a response"""
        query_lower = query.lower()

        for topic, explanation in self.knowledge_base.items():
            if topic in query_lower:
                return f"Here's what I know about {topic}: {explanation}"

        return "I can help you with Python programming concepts. Ask me about functions, classes, or Python basics!"


async def demo_evals_integration():
    """Demonstrate ASTK + OpenAI Evals integration"""

    print("🚀 ASTK + OpenAI Evals Integration Demo")
    print("=" * 50)

    # Check if OpenAI API key is available
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Please set OPENAI_API_KEY environment variable")
        print("💡 Get your API key from: https://platform.openai.com/api-keys")
        return

    try:
        # Initialize the Evals adapter
        print("🔧 Initializing OpenAI Evals adapter...")
        adapter = OpenAIEvalsAdapter()

        # Create sample scenarios for code QA evaluation
        print("📝 Creating test scenarios...")
        scenarios = create_code_qa_scenarios()

        print(f"✅ Created {len(scenarios)} test scenarios:")
        for i, scenario in enumerate(scenarios[:3], 1):
            print(f"   {i}. {scenario.task}")

        # Create an evaluation
        print("\n🎯 Creating OpenAI Eval...")
        eval_id = adapter.create_eval_from_scenarios(
            scenarios=scenarios,
            eval_name="ASTK Code QA Demo",
            grader_model="gpt-4"
        )

        print(f"✅ Eval created successfully!")
        print(f"📋 Eval ID: {eval_id}")

        # Show the grader prompt being used
        print("\n📊 Grader Prompt Preview:")
        print("-" * 30)
        code_qa_prompt = GRADER_PROMPTS["code_qa"]
        print(code_qa_prompt[:200] +
              "..." if len(code_qa_prompt) > 200 else code_qa_prompt)

        # Demonstrate agent response generation
        print("\n🤖 Example Agent Responses:")
        print("-" * 30)
        agent = ExampleCodeQAAgent()

        sample_queries = [
            "What are Python functions?",
            "Explain classes in Python",
            "How does Python work?"
        ]

        for query in sample_queries:
            response = await agent.process_query(query)
            print(f"Q: {query}")
            print(f"A: {response}\n")

        # Show next steps
        print("🚀 Next Steps:")
        print("1. Generate agent responses using OpenAI Responses API")
        print("2. Run evaluation using the CLI:")
        print(f"   astk evals run {eval_id}")
        print("3. View results in OpenAI dashboard")
        print("4. Compare with different models using:")
        print(f"   astk evals compare {eval_id} gpt-4-mini gpt-4-turbo")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("💡 Make sure you have the latest OpenAI package:")
        print("   pip install openai>=1.50.0")


def create_code_qa_scenarios() -> List[ScenarioConfig]:
    """Create sample scenarios for code QA evaluation"""

    scenarios = [
        ScenarioConfig(
            task="explain_function",
            persona=PersonaConfig(
                archetype="software_developer",
                temperature=0.7
            ),
            protocol="A2A",
            success=SuccessCriteria(
                semantic_score=0.8,
                task_specific={
                    "requires_code_explanation": True,
                    "technical_accuracy": True
                }
            )
        ),
        ScenarioConfig(
            task="debug_assistance",
            persona=PersonaConfig(
                archetype="junior_developer",
                temperature=0.5
            ),
            protocol="A2A",
            success=SuccessCriteria(
                semantic_score=0.7,
                task_specific={
                    "provides_solution": True,
                    "explains_reasoning": True
                }
            )
        ),
        ScenarioConfig(
            task="best_practices",
            persona=PersonaConfig(
                archetype="senior_engineer",
                temperature=0.3
            ),
            protocol="A2A",
            success=SuccessCriteria(
                semantic_score=0.9,
                task_specific={
                    "actionable_advice": True,
                    "industry_standards": True
                }
            )
        ),
        ScenarioConfig(
            task="code_review",
            persona=PersonaConfig(
                archetype="tech_lead",
                temperature=0.4
            ),
            protocol="A2A",
            success=SuccessCriteria(
                semantic_score=0.8,
                task_specific={
                    "identifies_issues": True,
                    "suggests_improvements": True
                }
            )
        ),
        ScenarioConfig(
            task="architecture_advice",
            persona=PersonaConfig(
                archetype="solutions_architect",
                temperature=0.6
            ),
            protocol="A2A",
            success=SuccessCriteria(
                semantic_score=0.8,
                task_specific={
                    "scalability_considerations": True,
                    "design_patterns": True
                }
            )
        )
    ]

    return scenarios


def cli_usage_examples():
    """Show CLI usage examples"""
    print("\n🛠️ CLI Usage Examples:")
    print("=" * 30)

    examples = [
        ("Create eval for code QA agent",
         "python -m astk.cli evals create my_agent.py --eval-type code_qa --grader gpt-4"),
        ("Run evaluation", "python -m astk.cli evals run eval_12345"),
        ("Compare two models",
         "python -m astk.cli evals compare eval_12345 gpt-4-mini gpt-4-turbo"),
        ("Install with evals support",
         "pip install agent-sprint-testkit[evals]"),
    ]

    for description, command in examples:
        print(f"📋 {description}:")
        print(f"   {command}\n")


if __name__ == "__main__":
    # Run the demo
    asyncio.run(demo_evals_integration())

    # Show CLI examples
    cli_usage_examples()

    print("\n🎉 Ready to revolutionize your agent testing with OpenAI Evals!")
    print("📖 Full documentation: https://github.com/stanhus/ASTK/blob/main/OPENAI_EVALS_INTEGRATION.md")
