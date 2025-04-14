from Action import Action
from pynput.mouse import Button
from Mouse import Mouse
from ControllerSingleton import ControllerSingleton

class LeftMousePress(Action, Mouse):
    def __init__(self):
        self.mouse = ControllerSingleton().get_controller()

    def Perform(self):
        self.mouse.position = (self.x, self.y)
        self.mouse.press(Button.left)
        
        
