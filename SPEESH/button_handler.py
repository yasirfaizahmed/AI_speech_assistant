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
import subprocess

from pattern import Singleton
# from record import Record


class Watcher(metaclass=Singleton):
  MIN_DELAY = 6
  event_timestamp = 0.0

  def __init__(self, device_path: str):
    if os.path.exists(device_path) is False:
      return
    self.device = evdev.InputDevice(device_path)
    self.device_path = device_path

  def _start_recording(self):
    # Record()
    subprocess.Popen(["/home/xd/Documents/python_codes/AI_speesh_assistant/bin/python3", "/home/xd/Documents/python_codes/AI_speesh_assistant/SPEESH/record.py"], user='xd')

  def _watcher_thread_target(self):
    for event in self.device.read_loop():
      if event.type == evdev.ecodes.EV_KEY:
        if (time.time() - Watcher.event_timestamp) > Watcher.MIN_DELAY:
          print("Pressed")
          self._start_recording()
        Watcher.event_timestamp = time.time()

  def start_watcher(self):
    watcher_thread = Thread(target=self._watcher_thread_target)
    watcher_thread.start()
    watcher_thread.join()


if __name__ == '__main__':
  # Record()
  watcher = Watcher(device_path='/dev/input/event15').start_watcher()
