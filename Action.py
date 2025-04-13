from abc import ABC, abstractmethod


class Action(ABC):
    @abstractmethod
    def Perform(self):
        pass