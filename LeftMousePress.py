from Action import Action
from pynput.mouse import Button
from Mouse import Mouse
from datetime import datetime
from ControllerSingleton import ControllerSingleton

class LeftMousePress(Action, Mouse):
    def __init__(self):
        self.mouse = ControllerSingleton().get_controller()
        self.start_time = datetime.now()

    def Perform(self):
        self.mouse.press(Button.left)

    def __str__(self):
        return "LMB Pressed"
        
        
