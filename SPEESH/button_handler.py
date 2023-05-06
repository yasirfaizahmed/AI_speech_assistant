"""
File: speesh.py
Author: yaseer faiz ahmedpatterns
Date: May 6, 2023
Description: SPEECH is an assistant powered by google-cloud, OpenAI APIs.
"""

import evdev
import os
import time
from threading import Thread

from pattern import Singleton


class Watcher(metaclass=Singleton):
  MIN_DELAY = 5
  event_timestamp = 0.0

  def __init__(self, device_path: str):
    if os.path.exists(device_path) is False:
      return
    self.device = evdev.InputDevice(device_path)
    self.device_path = device_path

  def _watcher_thread_target(self):
    for event in self.device.read_loop():
      if event.type == evdev.ecodes.EV_KEY:
        if (time.time() - Watcher.event_timestamp) > Watcher.MIN_DELAY:
          print("pressed")
        Watcher.event_timestamp = time.time()

  def start_watcher(self):
    watcher_thread = Thread(target=self._watcher_thread_target)
    watcher_thread.start()
    watcher_thread.join()


if __name__ == '__main__':
  watcher = Watcher(device_path='/dev/input/event15').start_watcher()
