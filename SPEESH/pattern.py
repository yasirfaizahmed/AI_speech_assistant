"""
File: speesh.py
Author: yaseer faiz ahmed
Date: May 6, 2023
Description: SPEECH is an assistant powered by google-cloud, OpenAI APIs.
"""


class Singleton(type):
  instances = {}

  def __call__(cls, *args, **kwargs):
    if cls not in cls.instances:
      cls.instances[cls] = cls.__new__(cls, *args, **kwargs)    # obj = cls.__new__(cls, *args, **kwargs)
      if isinstance(cls.instances[cls], cls):
        cls.instances[cls].__init__(*args, **kwargs)
    elif kwargs.get('_run_init', None) is not None:
      if isinstance(cls.instances[cls], cls):
        del kwargs['_run_init']
        cls.instances[cls].__init__(*args, **kwargs)

    return cls.instances[cls]
