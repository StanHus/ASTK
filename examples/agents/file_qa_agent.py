#!/usr/bin/env python3
"""
Simple File Q&A Agent using LangChain
"""

import os
import sys
from typing import List, Optional
# from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from langchain.agents import tool
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel, Field

# Load environment variables
# load_dotenv()


class FileQAAgent:
    """Agent that can answer questions about files in a directory"""

    def __init__(self, model_name: str = "gpt-3.5-turbo"):
        """Initialize the agent with OpenAI model"""
        self.llm = ChatOpenAI(
            model_name=model_name,
            temperature=0.7,
            api_key=os.getenv("OPENAI_API_KEY")
        )

        # Create agent with tools
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI assistant that answers questions about files. "
             "Use the available tools to read files and provide accurate answers."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])

        self.agent = create_openai_tools_agent(
            self.llm, self.get_tools(), prompt)
        self.agent_executor = AgentExecutor(
            agent=self.agent, tools=self.get_tools())
        self.chat_history: List[HumanMessage | AIMessage] = []

    @tool
    def read_file(file_path: str) -> str:
        """Read the contents of a file at the given path"""
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"

    @tool
    def list_files(directory: str = ".") -> str:
        """List files in the specified directory"""
        try:
            files = os.listdir(directory)
            return "\n".join(files)
        except Exception as e:
            return f"Error listing directory: {str(e)}"

    def get_tools(self):
        """Get the list of available tools"""
        return [self.read_file, self.list_files]

    async def chat(self, message: str) -> str:
        """Process a chat message and return the response"""
        # Add user message to history
        self.chat_history.append(HumanMessage(content=message))

        # Get response from agent
        response = await self.agent_executor.ainvoke({
            "input": message,
            "chat_history": self.chat_history
        })

        # Add agent response to history
        self.chat_history.append(AIMessage(content=response["output"]))

        return response["output"]


async def main():
    # Create agent
    agent = FileQAAgent()

    # Get query from command line arguments or use default queries
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        response = await agent.chat(query)
        print(f"Agent: {response}")
    else:
        # Example interactions
        response = await agent.chat("What files are in the examples/data directory?")
        print(f"Agent: {response}\n")

        response = await agent.chat("Can you read and summarize the contents of examples/data/sample.txt?")
        print(f"Agent: {response}")


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
