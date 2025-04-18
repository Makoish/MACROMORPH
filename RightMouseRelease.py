from Action import Action
from pynput.mouse import Button
from ControllerSingleton import ControllerSingleton
from datetime import datetime

class RightMouseRelease(Action):
    def __init__(self):
        
        self.start_time = datetime.now()

    def Perform(self):
        self.mouse = ControllerSingleton().get_controller()
        self.mouse.release(Button.right)
        self.mouse = None
        

    def __str__(self):
        return "RMB Released"