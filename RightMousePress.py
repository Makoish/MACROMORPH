from Action import Action
from pynput.mouse import Button
from Mouse import Mouse
from datetime import datetime
from ControllerSingleton import ControllerSingleton

class RightMousePress(Action, Mouse):
    def __init__(self):
        self.mouse = ControllerSingleton().get_controller()
        self.start_time = datetime.now()

    def Perform(self):
        self.mouse.press(Button.right)
        


    def __str__(self):
        return "RMB Pressed" 

