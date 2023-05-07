import os
from google.cloud import speech_v1p1beta1 as speech
import openai as ai
from google.cloud import texttospeech
import time
from datetime import date
import io
from pydub import AudioSegment
import pyaudio

# Audio recording parameters
CHANNELS = 2
RATE = 44100


def speech_to_text(audio_file: str):
  # Create a SpeechClient instance
  client = speech.SpeechClient()

  if os.path.exists(audio_file) is False:
    return False
  # Audio file
  audio_file = open(audio_file, 'rb')

  audio = speech.RecognitionAudio(content=audio_file.read())
  # Configure the audio settings
  config = speech.RecognitionConfig(
      encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
      sample_rate_hertz=RATE,
      language_code="en-IN",
      audio_channel_count=CHANNELS
  )

  # Call the Speech-to-Text API
  response = client.recognize(config=config, audio=audio)

  # Print the transcript
  transcript = ""
  confidence = None
  for result in response.results:
    transcript = result.alternatives[0].transcript
    confidence = result.alternatives[0].confidence

  return transcript, confidence


def ask_openai(user_prompt: str,
               engine='text-davinci-003',
               temperature=0.5,
               max_tokens=50) -> str:
  # secret key
  secret = os.environ['API_KEY']
  ai.api_key = secret

  completions = ai.Completion.create(engine=engine,            # Determines the quality, speed, and cost.
                                     temperature=temperature,  # Level of creativity in the response
                                     prompt=user_prompt,       # What the user typed in
                                     max_tokens=max_tokens,    # Maximum tokens in the prompt AND response
                                     n=1,                      # The number of completions to generate
                                     stop=None)
  return completions.choices[0].text.strip()


def text_to_speech(text: str):
  # Instantiates a client
  client = texttospeech.TextToSpeechClient()

  # Set the text input to be synthesized
  synthesis_input = texttospeech.SynthesisInput(text=text)

  # Build the voice request, select the language code ("en-US") and the ssml
  # voice gender ("neutral")
  voice = texttospeech.VoiceSelectionParams(
      language_code="en-IN", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
  )

  # Select the type of audio file you want returned
  audio_config = texttospeech.AudioConfig(
      audio_encoding=texttospeech.AudioEncoding.MP3
  )

  # Perform the text-to-speech request on the text input with the selected
  # voice parameters and audio file type
  response = client.synthesize_speech(
      input=synthesis_input, voice=voice, audio_config=audio_config
  )

  _current_time = time.strftime("%H-%M-%S", time.localtime())
  _current_date = date.today().strftime("%B-%d-%Y")
  audio_file = '_AUDIOs/{}_{}.mp3'.format(_current_date, _current_time)

  # The response's audio_content is binary.
  with open(audio_file, "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)

  return audio_file


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


if __name__ == '__main__':
  # speech_to_text(audio_file='/home/xd/Documents/python_codes/AI_speesh_assistant/_AUDIOs/May-07-2023_15-18-51.flac')
  # print(ask_openai(user_prompt="hello there.."))
  # text_to_speech(text="hello there")
  play_audio(audio_file='/home/xd/Documents/python_codes/AI_speesh_assistant/_AUDIOs/May-07-2023_17-56-20.mp3')
