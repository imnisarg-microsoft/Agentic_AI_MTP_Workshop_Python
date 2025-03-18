import autogen

class MiddlewareAgentDemo:
    def __init__(self, llmConfig: list[dict[str, any]]):
        self.llmConfig = llmConfig

    def runUserGoal(self, goal: str):
        agent = autogen.AssistantAgent(
            name="AI_Agent",
            system_message="You are an assistant agent that helps users to achieve their goals.",
            llm_config={"config_list": self.llmConfig},
        )

        class CustomMiddlewareAgent(autogen.ConversableAgent):
            def __init__(self, name, llm_config):
                super().__init__(name=name, llm_config=llm_config)

            def generate_reply(self, messages, sender):
                """Intercepts the user input, modifies it, and forwards it to the assistant agent."""
                modified_messages = messages[:]  # Copy message history

                if modified_messages and "content" in modified_messages[-1]:
                    modified_messages[-1]["content"] = f"[Filtered]: {modified_messages[-1]['content']}"

                return agent.generate_reply(messages=modified_messages, sender=self)

        # Instantiate middleware agent
        middleware_agent = CustomMiddlewareAgent(
            name="Middleware",
            llm_config={"config_list": self.llmConfig}
        )

        # User Proxy Agent
        user_proxy = autogen.UserProxyAgent(
            name="User",
            human_input_mode="NEVER",
            code_execution_config={"use_docker": False},  # Disable Docker
        )

        # Run Chat
        response = user_proxy.initiate_chat(middleware_agent, message=goal, max_turns=1)
        return response
