"""
File: speesh.py
Author: yaseer faiz ahmed
Date: May 6, 2023
Description: SPEECH is an assistant powered by google-cloud, OpenAI APIs.
"""

import evdev
import os
import time
from threading import Thread

from pattern import Singleton
from audio_util import Record, play_audio
from request_util import Request

CONFIDENCE_THRESHOLD = 0.5


class Watcher(metaclass=Singleton):
  MIN_DELAY = 6
  event_timestamp = 0.0

  def __init__(self, device_path: str):
    if os.path.exists(device_path) is False:
      return
    self.device = evdev.InputDevice(device_path)
    self.device_path = device_path

    # Request instance for google, openai client requests
    self.request = Request()

  def _start_processing(self):
    record_response = Record(_run_init=True)
    if record_response.result is True:
      transcript, confidence = self.request.speech_to_text(audio_file=record_response.audio_input_file)
      if confidence > CONFIDENCE_THRESHOLD:
        ai_response: str = self.request.ask_openai(user_prompt=transcript)
        print('################   ', ai_response)
        mp3_ouput_file = self.request.text_to_speech(ai_response)
        play_audio(audio_file=mp3_ouput_file)

  def _watcher_thread_target(self):
    for event in self.device.read_loop():
      if event.type == evdev.ecodes.EV_KEY:
        if (time.time() - Watcher.event_timestamp) > Watcher.MIN_DELAY:
          print("################   Pressed")
          self._start_processing()
        Watcher.event_timestamp = time.time()

  def start_watcher(self):
    watcher_thread = Thread(target=self._watcher_thread_target)
    watcher_thread.start()
    print("################   Watcher started")
    watcher_thread.join()


if __name__ == '__main__':
  # Record()
  watcher = Watcher(device_path='/dev/input/event15').start_watcher()
