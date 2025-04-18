from Action import Action
from pynput.mouse import Button
from datetime import datetime
from ControllerSingleton import ControllerSingleton

class LeftMouseRelease(Action):
    def __init__(self):
        self.start_time = datetime.now()

    def Perform(self):
        self.mouse = ControllerSingleton().get_controller()
        self.mouse.release(Button.left)
        self.mouse = None
        
    def __str__(self):
        return "LMB Released"