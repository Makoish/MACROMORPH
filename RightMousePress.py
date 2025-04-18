from Action import Action
from pynput.mouse import Button
from datetime import datetime
from ControllerSingleton import ControllerSingleton

class RightMousePress(Action):
    def __init__(self):
        self.start_time = datetime.now()
        self.mouse = ControllerSingleton().get_controller()
        self.x = self.mouse.position[0]
        self.y = self.mouse.position[1]
        self.mouse = None

    def Perform(self):
        self.mouse = ControllerSingleton().get_controller()
        self.mouse.press(Button.right)
        self.mouse = None
        


    def __str__(self):
        return "RMB Pressed" 

