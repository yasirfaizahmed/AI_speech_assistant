import pyaudio
import wave
import time
from datetime import date
import os

from pattern import Singleton


FORMAT = pyaudio.paInt16
CHANNELS = 1
# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms
RECORD_SECONDS = 5


class Record(metaclass=Singleton):
  def __init__(self, duration: int = RECORD_SECONDS):
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
    self.audio_file = self._prepare_audio_archive()
    waveFile = wave.open(self.audio_file, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

  def _prepare_audio_archive(self) -> str:
    # handling the archive dir
    _audio_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), '../_AUDIOs'))
    if os.path.exists(_audio_dir) is False:
      os.mkdir(_audio_dir)
    _current_time = time.strftime("%H-%M-%S", time.localtime())
    _current_date = date.today().strftime("%B-%d-%Y")
    return '_AUDIOs/{}_{}.wav'.format(_current_date, _current_time)


if __name__ == '__main__':
  recorder = Record()
