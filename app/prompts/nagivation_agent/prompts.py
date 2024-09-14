class Prompt:
    def __init__(self):
        pass
    
    @staticmethod
    def get_prompt_for_navigate():
        return """
        You are a navigation agent. Given a message, you should decide which agent to use to perform the task.
        Here is the message: "{message}"

        Here is the list of the name of agent you can choose from:
            1. VectorAgent
                - name: "VectorAgent"
                - description: "This agent can perform tasks related to a Raspberry Pi base robot called Vector."
                - possible actions as function name: ["move_forward", "move_backward", "turn_left", "turn_right"]

        You should return a string as this format: "<name_of_agent>"
        """