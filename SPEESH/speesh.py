"""
File: speesh.py
Author: yaseer faiz ahmed
Date: May 6, 2023
Description: SPEECH is an assistant powered by google-cloud, OpenAI APIs.
"""

from handler import Watcher
from configs import Config


class Speesh(Config):
  def __init__(self):
    self.watcher = Watcher(device_path=self.EVENT_FILE).start_watcher()


if __name__ == '__main__':
  Speesh()
