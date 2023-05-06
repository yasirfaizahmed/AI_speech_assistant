# Import the Google Cloud client library
from google.cloud import speech_v1p1beta1 as speech

# Create a SpeechClient instance
client = speech.SpeechClient()

# Audio file
audio_file = open('test2.flac', 'rb')

# Configure the audio source
audio = speech.RecognitionAudio(content=audio_file.read())
# Configure the audio settings
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=44100,
    language_code="en-IN",
    audio_channel_count=2
)

# Call the Speech-to-Text API
response = client.recognize(config=config, audio=audio)

# Print the transcript
for result in response.results:
    print(result.alternatives[0].transcript)
