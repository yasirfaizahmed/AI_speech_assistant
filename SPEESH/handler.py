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
from audio_util import AudioUtil
from request_util import Request
from base import Base


class Watcher(Base, metaclass=Singleton):
  MIN_DELAY = 6
  event_timestamp = 0.0

  def __init__(self, device_path: str):
    super().__init__()
    if os.path.exists(device_path) is False:
      return
    self.device = evdev.InputDevice(device_path)
    self.device_path = device_path

    # Request instance for google, openai client requests
    self.request = Request()

  def _start_processing(self):
    audio_util = AudioUtil()
    record_response = audio_util.start_record()
    if record_response is True:
      transcript, confidence = self.request.speech_to_text(audio_file=audio_util.audio_input_file)
      self.logger.info("Confidence: {} Transcript: {}".format(confidence, transcript))
      if confidence > self.CONFIDENCE_THRESHOLD:
        ai_response: str = self.request.ask_openai(user_prompt=transcript)
        self.logger.info("AI_RESPONSE: {}".format(ai_response))
        mp3_ouput_file = self.request.text_to_speech(ai_response)
        audio_util.play_audio(audio_file=mp3_ouput_file)
    self.logger.info("Watcher Started")

  def _watcher_thread_target(self):
    for event in self.device.read_loop():
      if event.type == evdev.ecodes.EV_KEY:
        if (time.time() - Watcher.event_timestamp) > Watcher.MIN_DELAY:
          self.logger.info("Listening...")
          self._start_processing()
        Watcher.event_timestamp = time.time()

  def start_watcher(self):
    watcher_thread = Thread(target=self._watcher_thread_target)
    watcher_thread.start()
    self.logger.info("Watcher Started")
    watcher_thread.join()


if __name__ == '__main__':
  # Record()
  watcher = Watcher(device_path='/dev/input/event15').start_watcher()
