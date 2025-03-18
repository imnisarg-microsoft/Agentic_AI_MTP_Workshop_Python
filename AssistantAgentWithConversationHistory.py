import autogen

class AssistantAgentWithConversationHistory:
    def __init__(self, llmConfig: list[dict[str, any]]):
        self.llmConfig = llmConfig
        self.messages = []  # Store conversation history

    def runUserGoal(self, user_message):
        assistant_agent = autogen.AssistantAgent(
            name="assistant",
            system_message="You remember user details like their name.",
            llm_config={"config_list": self.llmConfig},
        )

        user_proxy = autogen.UserProxyAgent(
            name="User",
            human_input_mode="NEVER",
            code_execution_config={"use_docker": False},
        )

        for message in self.messages:
            # Send the history to the assistant
            user_proxy.send(message['content'], assistant_agent)
        # Append user's new message
        self.messages.append({"role": "user", "content": user_message})
 
        # Call the assistant with full conversation history
        reply = user_proxy.initiate_chat(
            assistant_agent,
            message=user_message,
            max_turns=1,
            chat_history=self.messages  # ✅ Pass entire history
        )


        return reply

