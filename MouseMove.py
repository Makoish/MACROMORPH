from Action import Action
from pynput.mouse import Button
from Mouse import Mouse
from ControllerSingleton import ControllerSingleton

class MouseMove(Action, Mouse):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mouse = ControllerSingleton().get_controller()

    def move(self, x, y):
        self.x = x
        self.y = y

    def Perform(self):
        self.mouse.position = (self.x, self.y)
        
        
