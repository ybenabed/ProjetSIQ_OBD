import os
import threading
import time
from obd_scripts.requests import get_speeds, get_distance
from obd_scripts.files import read_values
import wifi_connection.prog as wi_fi

class StoppableThread(threading.Thread):
    """To customize the thread and make it stoppable"""
    def __init__(self,  *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()


delay = 5
speed_thread = StoppableThread(target=get_speeds, args=(delay,))
wifi_thread = threading.Thread(target=wi_fi)
speed_thread.start()
wifi_thread.start()
while(wifi_thread.is_alive()):
    pass
speed_thread.stop()
speeds = read_values()
distance = get_distance()