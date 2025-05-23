from Action import Action
from pynput.mouse import Button
from datetime import datetime
from KeyboardControllerSingleton import KeyboardControllerSingleton

class KeyboardRelease(Action):
    def __init__(self, key):
        
        self.start_time = datetime.now()
        self.key = key
    def Perform(self):
        self.keyboard = KeyboardControllerSingleton().get_controller()
        self.keyboard.release(self.key)
        


    def __str__(self):
        return f"{self.key} released" 

