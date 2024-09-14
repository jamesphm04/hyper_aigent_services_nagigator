class Prompt:
    def __init__(self):
        pass
    
    @staticmethod
    def get_prompt_for_choosing_function():
        return """
        You are an agent controlling a robot named Vector.
        You have to choose a function to perform a task on Vector base on a message.
        Here is the message: "{message}"

        Here is the list of the name of function you can choose from:
            1. move_forward
                - description: "Move the robot forward"
            2. move_backward
                - description: "Move the robot backward"
            3. turn_left
                - description: "Turn the robot left"
            4. turn_right
                - description: "Turn the robot right"

        You should return a string as this format: "<name_of_function>"
        """