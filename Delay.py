import time
from Action import Action

class Delay(Action):

    def __init__(self, _time):
        self._time = _time.total_seconds()

    def Perform(self):
        time.sleep(self._time)

    def __str__(self):
        return f"Delay {self._time}"
