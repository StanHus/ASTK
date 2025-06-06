#!/usr/bin/env python3

import os
import sys
import traceback
from astk.evals_integration import OpenAIEvalsAdapter
from astk.schema import ScenarioConfig, SuccessCriteria, OpenAIEvaluationConfig, PersonaConfig


def test_evaluation():
    print("🔍 Debug: Testing evaluation system...")

    # Create test scenario
    scenario = ScenarioConfig(
        name="debug_test",
        task="simple_test",
        persona=PersonaConfig(archetype="test", temperature=0.5, traits=[]),
        protocol="A2A",
        input_prompt="What is 2+2?",
        success=SuccessCriteria(
            regex="4",
            semantic_score=0.8,
            openai_evaluations=[
                OpenAIEvaluationConfig(
                    evaluator="gpt-3.5-turbo",
                    prompt="Evaluate this response. Score 1-10 and return JSON with 'overall_score' field.",
                    pass_threshold=7.0
                )
            ]
        )
    )

    # Test response
    test_response = "2 + 2 = 4. This is basic addition where we combine two quantities of 2 to get 4."

    print(f"📝 Test response: {test_response}")
    print()

    try:
        # Initialize adapter
        adapter = OpenAIEvalsAdapter()
        print("✅ OpenAI adapter initialized")

        # Test basic criteria first
        print("🧪 Testing basic criteria...")
        basic_score = adapter._evaluate_basic_criteria(
            test_response, scenario.success)
        print(f"   Basic score: {basic_score:.1f}")

        # Test semantic similarity
        print("🧪 Testing semantic similarity...")
        semantic_score = adapter._calculate_semantic_similarity(
            test_response, scenario.success)
        print(f"   Semantic score: {semantic_score:.1f}")

        # Test OpenAI evaluation directly
        print("🧪 Testing OpenAI evaluation...")
        eval_config = scenario.success.openai_evaluations[0]

        try:
            score, feedback = adapter._perform_openai_evaluation(
                test_response,
                eval_config.prompt,
                eval_config.evaluator,
                scenario
            )
            print(f"   ✅ OpenAI evaluation successful: {score:.1f}")
            print(f"   📋 Feedback preview: {feedback[:200]}...")

        except Exception as e:
            print(f"   ❌ OpenAI evaluation failed: {str(e)}")
            print(f"   🔍 Full traceback:")
            traceback.print_exc()

        # Test full multi-layer evaluation
        print("🧪 Testing full multi-layer evaluation...")
        result = adapter.evaluate_response_multilayer(test_response, scenario)

        print(f"   Overall score: {result.overall_score:.1f}")
        print(f"   Passed: {result.passed}")
        print("   Layer breakdown:")
        for layer_name, layer_data in result.layer_results.items():
            score = layer_data.get('score', 0)
            evaluator = layer_data.get('evaluator', 'unknown')
            print(f"     └ {layer_name} ({evaluator}): {score:.1f}")

    except Exception as e:
        print(f"❌ Test failed: {str(e)}")
        traceback.print_exc()


if __name__ == "__main__":
    test_evaluation()
