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


from record import Record
import subprocess

p = subprocess.Popen(["/home/xd/Documents/python_codes/AI_speesh_assistant/bin/python3", "/home/xd/Documents/python_codes/AI_speesh_assistant/SPEESH/record.py"], env=)