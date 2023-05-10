"""
File: speesh.py
Author: yaseer faiz ahmed
Date: May 6, 2023
Description: SPEECH is an assistant powered by google-cloud, OpenAI APIs.
"""


from log_handler import InitilizeLogger
import logging


class Base():
  """ Base class for all the classes"""
  def __init__(self):
    self.logger = InitilizeLogger(handler=logging.FileHandler, level=10)()
    self._import_config()

  def _import_config(self):
    _class_name = type(self).__name__
    _config_module = __import__('configs')
    _config_class = getattr(_config_module, _class_name)
    self.__dict__.update(_config_class.__dict__)


class Config(Base):
  def __init__(self):
    self.a = 1
    super().__init__()
