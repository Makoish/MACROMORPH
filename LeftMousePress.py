from Action import Action
from pynput.mouse import Button
from Mouse import Mouse
from datetime import datetime
from ControllerSingleton import ControllerSingleton

class LeftMousePress(Action, Mouse):
    def __init__(self):
        self.mouse = ControllerSingleton().get_controller()
        self.start_time = datetime.now()
        self.x = self.mouse.position[0]
        self.y = self.mouse.position[1]
        self.mouse = None
        

    def Perform(self):
        self.mouse = ControllerSingleton().get_controller()
        self.mouse.press(Button.left)
        self.mouse = None

    def __str__(self):
        return "LMB Pressed"
        
        
