from Action import Action
from pynput.mouse import Button
from Mouse import Mouse
from ControllerSingleton import ControllerSingleton
from datetime import datetime

class RightMouseRelease(Action, Mouse):
    def __init__(self):
        self.mouse = ControllerSingleton().get_controller()
        self.start_time = datetime.now()

    def Perform(self):
        self.mouse.release(Button.right)
        

    def __str__(self):
        return "RMB Released"