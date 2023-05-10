import pyaudio


class AudioUtil:
  # Audio configs
  AUDIO_DIR = '_AUDIOs'
  AUDIO_DIR_ABS = ''
  AUDIO_IN_DIR = '_IN'
  AUDIO_OUT_DIR = '_OUT'
  # Audio recording parameters
  FORMAT = pyaudio.paInt16
  CHANNELS = 2
  RATE = 44100
  CHUNK = 1024

  # Speech/Text configs

  # Openai configs


class Watcher:
  # General configs
  EVENT_FILE = '/dev/input/event15'
  CONFIDENCE_THRESHOLD = 0.5
