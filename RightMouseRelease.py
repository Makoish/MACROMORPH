from Action import Action
from pynput.mouse import Button
from Mouse import Mouse
from ControllerSingleton import ControllerSingleton

class RightMouseRelease(Action, Mouse):
    def __init__(self):
        self.mouse = ControllerSingleton().get_controller()

    def Perform(self):
        self.mouse.release(Button.right)
        