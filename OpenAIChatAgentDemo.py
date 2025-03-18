import asyncio
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.identity import DefaultAzureCredential
import autogen

class OpenAIChatAgentDemo:
    def __init__(self, llmConfig: list[dict[str, any]]):
        self.llmConfig = llmConfig

    def runUserGoal(self, goal:str):
        chatAgent = autogen.AssistantAgent(
            name="AI_Agent",
            system_message= "You are an assistant agent that helps users to achieve their goals.",
            llm_config= 
            {
                "config_list": self.llmConfig
            }
        )
        response = chatAgent.generate_reply(
            messages= [{"role": "user", "content": goal}],
        )
        return response
    
        