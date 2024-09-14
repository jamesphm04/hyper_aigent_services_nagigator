from abc import ABC, abstractmethod

class BaseAgent(ABC):

    @abstractmethod
    def perform_task(self, task_name):
        pass