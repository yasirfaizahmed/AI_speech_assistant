# flake8: noqa
# # Import the Google Cloud client library
# from google.cloud import speech_v1p1beta1 as speech

# # Create a SpeechClient instance
# client = speech.SpeechClient()

# # Audio file
# audio_file = open('test2.flac', 'rb')

# # Configure the audio source
# audio = speech.RecognitionAudio(content=audio_file.read())
# # Configure the audio settings
# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
#     sample_rate_hertz=44100,
#     language_code="en-IN",
#     audio_channel_count=2
# )

# # Call the Speech-to-Text API
# response = client.recognize(config=config, audio=audio)

# # Print the transcript
# for result in response.results:
#     print(result.alternatives[0].transcript)


# from record import Record
# import subprocess

# p = subprocess.Popen(["/home/xd/Documents/python_codes/AI_speesh_assistant/bin/python3", "/home/xd/Documents/python_codes/AI_speesh_assistant/SPEESH/record.py"], env=)


import os
import sys
import pyaudio
def fun():
    print("heelloo")
    raise FileNotFoundError

class SuppressOutput:
  """
  A context manager to temporarily suppress stderr output.
  """
  def __enter__(self):
    sys.stderr = open(os.devnull, 'w')

  def __exit__(self, exc_type, exc_val, exc_tb):
    sys.stderr.close()
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
AUDIO_DIR = '_AUDIOs'

with SuppressOutput() as s:
    fun()
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

