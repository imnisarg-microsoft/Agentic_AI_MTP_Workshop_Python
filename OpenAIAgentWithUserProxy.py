import asyncio
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.identity import DefaultAzureCredential
import autogen

class OpenAIAgentWithUserProxy:
    def __init__(self, llmConfig: list[dict[str, any]]):
        self.llmConfig = llmConfig

    def runUserGoal(self, goal:str):
        agent = autogen.AssistantAgent(
        name="AI_Agent",
        system_message = "You are an assistant agent that helps users to achieve their goals.",
        llm_config=
            {
                "config_list": self.llmConfig,
            }
        )
        user_proxy = autogen.UserProxyAgent(
        name="User",
        human_input_mode="NEVER",
        code_execution_config={"use_docker": False},  # Disable Docker
        )

        response = user_proxy.initiate_chat(agent, message=goal, max_turns=1)
        return response
    
        