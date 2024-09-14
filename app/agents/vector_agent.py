from .base_agent import BaseAgent
import os
from langchain_openai import ChatOpenAI
from ..prompts.vector_agent.prompts import Prompt
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class VectorAgent(BaseAgent):
    def __init__(self, model_name="gpt-3.5-turbo"):
        super().__init__()

        self.model = ChatOpenAI(model_name=model_name, api_key=OPENAI_API_KEY)

        self.parser = StrOutputParser()

    def perform_task(self, message) -> str:
        function_name = self.choose_function(message)

        # Dynamically call the function if it exists
        func = getattr(self, function_name, None)
        
        if callable(func):
            return func()  # Execute the function and return its result
        else:
            return f"Error: {function_name} is not a valid function."

     

    def choose_function(self, message) -> str:
        system_template = Prompt.get_prompt_for_choosing_function()

        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", system_template)
            ]
        )
        
        chain = prompt_template | self.model | self.parser
        return chain.invoke({"message": message})

    def move_forward(self):
        return "Moving forward"
    
    def move_backward(self):
        return "Moving backward"

    def turn_left(self):
        return "Turning left"
    
    def turn_right(self):
        return "Turning right"