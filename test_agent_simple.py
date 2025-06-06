#!/usr/bin/env python3
"""
Simple test agent for verifying ASTK evaluation system
"""


def respond_to_query(query: str) -> str:
    """Simple agent that provides basic responses"""

    query_lower = query.lower()

    # Math questions
    if "2 + 2" in query_lower or "2+2" in query_lower:
        return "2 + 2 = 4. This is basic addition where we combine two quantities of 2 to get a sum of 4."

    # General responses
    if "microservices" in query_lower and "monolithic" in query_lower:
        return """
        Microservices and monolithic architectures represent two different approaches to system design:
        
        **Monolithic Architecture:**
        - Single deployable unit with all components tightly coupled
        - Easier to develop and test initially
        - Simpler deployment and monitoring
        - Good for small to medium applications
        
        **Microservices Architecture:**
        - Multiple small, independent services
        - Better scalability and technology diversity
        - More complex deployment and monitoring
        - Better for large, complex applications
        
        **When to use each:**
        - Monolithic: Small teams, simple applications, rapid prototyping
        - Microservices: Large teams, complex domains, need for independent scaling
        
        **Data consistency challenges:**
        - Use event sourcing and saga patterns
        - Implement eventual consistency where appropriate
        - Consider distributed transaction patterns like Two-Phase Commit when necessary
        """

    # Default response
    return f"I understand you're asking about: {query}. Let me provide a thoughtful analysis based on the key concepts involved."


if __name__ == "__main__":
    # Test the agent
    test_queries = [
        "What is 2 + 2?",
        "Explain microservices vs monolithic architecture"
    ]

    for query in test_queries:
        print(f"Query: {query}")
        print(f"Response: {respond_to_query(query)}")
        print("-" * 50)
