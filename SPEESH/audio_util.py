"""
File: speesh.py
Author: yaseer faiz ahmed
Date: May 6, 2023
Description: SPEECH is an assistant powered by google-cloud, OpenAI APIs.
"""


import pyaudio
import wave
import time
from datetime import date
import os
import logging
from pydub import AudioSegment

from pattern import Singleton
from configs import Config


# Audio recording parameters
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
AUDIO_DIR = '_AUDIOs'

logging.basicConfig(level=logging.INFO)


def calibrate_audio_file_path(mode: str, format: str):
  _current_time = time.strftime("%H-%M-%S", time.localtime())
  _current_date = date.today().strftime("%B-%d-%Y")
  if mode == 'in':
    return '{}/{}/{}_{}.{}'.format(Config.AUDIO_DIR, Config.AUDIO_IN_DIR, _current_date, _current_time, format)
  elif mode == 'out':
    return '{}/{}/{}_{}.{}'.format(Config.AUDIO_DIR, Config.AUDIO_OUT_DIR, _current_date, _current_time, format)


def play_audio(audio_file: str):
  # Set up PyAudio
  p = pyaudio.PyAudio()

  # Load the MP3 file using pydub
  mp3_file = audio_file
  audio = AudioSegment.from_file(mp3_file, format="mp3")

  # Convert the audio to raw PCM data
  raw_data = audio.raw_data

  # Open a stream to play the audio
  stream = p.open(format=p.get_format_from_width(audio.sample_width),
                  channels=audio.channels,
                  rate=audio.frame_rate,
                  output=True)

  # Write the PCM data to the stream
  stream.write(raw_data)

  # Close the stream and PyAudio
  stream.stop_stream()
  stream.close()
  p.terminate()


class Record(Config, metaclass=Singleton):
  def __init__(self, duration: int = RECORD_SECONDS, **kwargs):
    self.result = False
    self.audio_input_file = self._prepare_audio_archive()

    self.start_record(self.audio_input_file, duration)

  def start_record(self, audio_input_file: str, duration: int):
    audio = pyaudio.PyAudio()
    frames = []

    # start Recording
    print("Recording")
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    for _ in range(0, int(RATE / CHUNK * duration)):
      data = stream.read(CHUNK, exception_on_overflow=False)
      frames.append(data)

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the file
    waveFile = wave.open(audio_input_file, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    self.result = True

  def _prepare_audio_archive(self) -> str:
    # handling the archive dir
    _audio_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '../{}'.format(AUDIO_DIR)))
    Config.AUDIO_DIR_ABS = _audio_dir
    if os.path.exists(_audio_dir) is False:
      os.mkdir(_audio_dir)
      os.mkdir(os.path.join(_audio_dir, Config.AUDIO_IN_DIR))
      os.mkdir(os.path.join(_audio_dir, Config.AUDIO_OUT_DIR))

    return calibrate_audio_file_path(mode='in', format='flac')


if __name__ == '__main__':
  recorder = Record()
