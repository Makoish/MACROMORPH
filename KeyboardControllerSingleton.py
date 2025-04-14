from pynput.keyboard import Controller

class KeyboardControllerSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new ControllerSingleton instance...")
            cls._instance = super(KeyboardControllerSingleton, cls).__new__(cls)
            cls._instance.controller = Controller()
        
        return cls._instance

    def get_controller(self):
        return self.controller
