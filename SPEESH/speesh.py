"""
File: speesh.py
Author: yaseer faiz ahmed
Date: May 6, 2023
Description: SPEECH is an assistant powered by google-cloud, OpenAI APIs.
"""

from button_handler import Watcher


class Speesh():
  def __init__(self):
    self.watcher = Watcher(device_path='/dev/input/event15')


if __name__ == '__main__':
  Speesh()
