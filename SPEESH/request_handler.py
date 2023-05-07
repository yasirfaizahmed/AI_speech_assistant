import os
from google.cloud import speech_v1p1beta1 as speech
import openai as ai

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


if __name__ == '__main__':
  speech_to_text(audio_file='/home/xd/Documents/python_codes/AI_speesh_assistant/_AUDIOs/May-07-2023_15-18-51.flac')
  print(ask_openai(user_prompt="hello there.."))
