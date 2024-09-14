from .base_agent import BaseAgent
import os
from langchain_openai import ChatOpenAI
from ..prompts.nagivation_agent.prompts import Prompt
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from .vector_agent import VectorAgent

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class NavigationAgent(BaseAgent):
    def __init__(self, model_name="gpt-3.5-turbo"):
        super().__init__()

        self.model = ChatOpenAI(model_name=model_name, api_key=OPENAI_API_KEY)
        self.parser = StrOutputParser()

        self.vector_agent = VectorAgent()

    def perform_task(self, message):
        agent_name = self.choose_agent(message)

        match agent_name:
            case "VectorAgent":
                return self.vector_agent.perform_task(message)
            case _:
                return f"Agent {agent_name} is not supported"
    
    def choose_agent(self, message) -> str:
        
        system_template = Prompt.get_prompt_for_navigate()

        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", system_template)
            ]
        )
        
        chain = prompt_template | self.model | self.parser
        return chain.invoke({"message": message})

        
    