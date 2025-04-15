from Action import Action
from pynput.mouse import Button
from datetime import datetime
from ControllerSingleton import ControllerSingleton

class MouseScroll(Action):
    def __init__(self, x, y):
        self.mouse = ControllerSingleton().get_controller()
        self.start_time = datetime.now()
        self.x = x
        self.y = y
    def Perform(self):
        self.mouse.scroll(self.x, self.y)
        

    def __str__(self):
        return f"Scrolled to {self.x}, {self.y}" 

