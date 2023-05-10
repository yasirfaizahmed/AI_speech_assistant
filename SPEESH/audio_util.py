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
import sys
from pydub import AudioSegment

from pattern import Singleton, SuppressOutput
from base import Base


RECORD_SECONDS = 5


class AudioUtil(Base, metaclass=Singleton):
  def __init__(self, **kwargs):
    super().__init__()

  def start_record(self, duration: int = RECORD_SECONDS):
    self.audio_input_file = self._prepare_audio_archive()
    frames = []

    # start Recording
    with SuppressOutput() as _:
      sys.stderr = open(os.devnull, 'w')
      audio = pyaudio.PyAudio()
      sys.stderr.close()
      stream = audio.open(format=self.FORMAT, channels=self.CHANNELS,
                          rate=self.RATE, input=True,
                          frames_per_buffer=self.CHUNK)

    for _ in range(0, int(self.RATE / self.CHUNK * duration)):
      data = stream.read(self.CHUNK, exception_on_overflow=False)
      frames.append(data)

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the file
    waveFile = wave.open(self.audio_input_file, 'wb')
    waveFile.setnchannels(self.CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(self.FORMAT))
    waveFile.setframerate(self.RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    return True

  def _prepare_audio_archive(self) -> str:
    # handling the archive dir
    _audio_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '../{}'.format(self.AUDIO_DIR)))
    if os.path.exists(_audio_dir) is False:
      os.mkdir(_audio_dir)
      os.mkdir(os.path.join(_audio_dir, self.AUDIO_IN_DIR))
      os.mkdir(os.path.join(_audio_dir, self.AUDIO_OUT_DIR))

    return self._calibrate_audio_file_path(mode='in', format='flac')

  def _calibrate_audio_file_path(self, mode: str, format: str):
    _current_time = time.strftime("%H-%M-%S", time.localtime())
    _current_date = date.today().strftime("%B-%d-%Y")
    if mode == 'in':
      return '{}/{}/{}_{}.{}'.format(self.AUDIO_DIR, self.AUDIO_IN_DIR, _current_date, _current_time, format)
    elif mode == 'out':
      return '{}/{}/{}_{}.{}'.format(self.AUDIO_DIR, self.AUDIO_OUT_DIR, _current_date, _current_time, format)

  def play_audio(self, audio_file: str):
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


if __name__ == '__main__':
  recorder = AudioUtil()
