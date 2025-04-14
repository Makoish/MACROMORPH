from Action import Action
from pynput.mouse import Button
from Mouse import Mouse
from ControllerSingleton import ControllerSingleton
from datetime import datetime

class MouseMove(Action, Mouse):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mouse = ControllerSingleton().get_controller()
        self.start_time = datetime.now()

    def move(self, x, y):
        self.x = x
        self.y = y

    def Perform(self):
        self.mouse.position = (self.x, self.y)

    def __str__(self):
        return f"Mouse moved to pos {self.x}, {self.y}"
        
        
