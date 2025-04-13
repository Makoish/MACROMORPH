from pynput.mouse import Controller

class MouseControllerSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new MouseControllerSingleton instance...")
            cls._instance = super(MouseControllerSingleton, cls).__new__(cls)
            cls._instance.controller = Controller()
        
        return cls._instance

    def get_controller(self):
        return self.controller
