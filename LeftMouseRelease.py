from Action import Action
from pynput.mouse import Button
from Mouse import Mouse
from MouseControllerSingleton import MouseControllerSingleton

class LeftMouseRelease(Action, Mouse):
    def __init__(self):
        self.mouse = MouseControllerSingleton().get_controller()

    def Perform(self):
        self.mouse.release(Button.left)
        