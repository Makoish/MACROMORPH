import time
from Action import Action

class Delay(Action):

    def __init__(self, _time):
        self._time = _time

    def Perform(self):
        time.sleep(self._time.total_seconds())
