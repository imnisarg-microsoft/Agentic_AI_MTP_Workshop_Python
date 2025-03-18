import autogen
import os
from azure.identity import AzureCliCredential
from OpenAIChatAgentDemo import OpenAIChatAgentDemo
from OpenAIAgentWithUserProxy import OpenAIAgentWithUserProxy
from AssistantAgentWithConversationHistory import AssistantAgentWithConversationHistory
from MiddlewareAgentDemo import MiddlewareAgentDemo
from AgentWithFunctionCall import AgentWithFunctionCall

# Get the Azure OpenAI token using Managed Identity
credential = AzureCliCredential()
token = credential.get_token("https://cognitiveservices.azure.com/.default").token

# Azure OpenAI Configuration
AZURE_OPENAI_ENDPOINT = "https://agentic-ai-workshop-openai.openai.azure.com"
DEPLOYMENT_NAME = "gpt-4o"  # Your Azure OpenAI deployment name

# Define the AI Agent using AutoGen
config_list = [
    {
        "model": DEPLOYMENT_NAME,
        "api_key": token,  # Set to None when using token-based auth
        "base_url": f"{AZURE_OPENAI_ENDPOINT}",
        "api_type": "azure",
        "api_version": "2024-02-01",
    }
]

# response = OpenAIChatAgentDemo(config_list).runUserGoal("What is the capital of India?")
# response = OpenAIAgentWithUserProxy(config_list).runUserGoal("What is Autogen?")
# response = MiddlewareAgentDemo(config_list).runUserGoal("What is threat hunting?")
response = AgentWithFunctionCall(config_list).runUserGoal()
print(response)


