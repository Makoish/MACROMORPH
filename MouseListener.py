from pynput.mouse import Listener, Button
from ListAction import ListAction
from LeftMousePress import LeftMousePress
from RightMousePress import RightMousePress
from LeftMouseRelease import LeftMouseRelease
from RightMouseRelease import RightMouseRelease
from KeyboardPress import KeyboardPress
from KeyboardRelease import KeyboardRelease
import threading
from Delay import Delay
from MouseMove import MouseMove
from ControllerSingleton import ControllerSingleton
from KeyboardControllerSingleton import KeyboardControllerSingleton
import ctypes
from datetime import datetime
from pynput.keyboard import Listener as KeyboardListener, Key
PROCESS_PER_MONITOR_DPI_AWARE=2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)

class eventListener:
    def __init__(self):

        self.listAction = ListAction()
        self.controller = ControllerSingleton().get_controller()
        start_pos = self.controller.position
        self.listAction.append(MouseMove(start_pos[0], start_pos[1]))
        self.listener = Listener(
            on_click=self.on_click,
            on_move=self.on_move,
            on_scroll=self.on_scroll
        )

        self.keyboard_listener = KeyboardListener(
            on_press=self.on_key_press
        )
        self.keyboard_listener.start()

    def on_click(self, x, y, button, pressed):


        if pressed:
            if button == Button.left:
                self.listAction.append(LeftMousePress())
            if button == Button.right:
                self.listAction.append(RightMousePress())
        else:
            if button == Button.left:
                self.listAction.append(LeftMouseRelease())
            if button == Button.right:
                self.listAction.append(RightMouseRelease())


    def on_key_press(self, key):
        if key == Key.f12:
            print("F12 pressed. Stopping listeners")
            self.running = False
            self.listener.stop()
            self.keyboard_listener.stop()
            return False  # This stops the keyboard listener

        last_start_time = self.listAction.tail.data.start_time
        _delay = datetime.now() - last_start_time
        self.listAction.append(Delay(_delay))
        self.listAction.append(KeyboardPress(key))
        
        
    

    def on_release(key):
        last_start_time = self.listAction.tail.data.start_time
        _delay = datetime.now() - last_start_time
        self.listAction.append(Delay(_delay))
        self.listAction.append(KeyboardRelease(key))


    
    def on_move(self, x, y):
        last_start_time = self.listAction.tail.data.start_time
        _delay = datetime.now() - last_start_time
        self.listAction.append(Delay(_delay))
        self.listAction.append(MouseMove(x, y))

    def on_scroll(self, x, y, dx, dy):
        print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")

    def after_listener_stops(self):
        self.listAction.traverse()

    def start(self):
        self.listener.start()  # non-blocking
        self.listener.join()   # blocking
        self.after_listener_stops()  # This is called after the listener stops

# Usage
if __name__ == "__main__":
    _eventListener = eventListener()
    _eventListener.start()
