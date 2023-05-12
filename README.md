# AI speech assistant

[![flake8](https://github.com/yasirfaizahmed/AI_speech_assistant/actions/workflows/flake8.yml/badge.svg)](https://github.com/yasirfaizahmed/AI_speech_assistant/actions/workflows/flake8.yml)

## Overview
This project is a powerful combination of OpenAI's state-of-the-art GPT technology and the advanced Google Cloud Speech API. It enables users to easily convert speech to text and back, all with the click of a customizable key.

## Key Features
- The project leverages OpenAI's highly sophisticated GPT technology, which is capable of generating highly accurate text responses.
- The integration with the Google Cloud Speech API enables users to easily convert their spoken words into text format.
- The project is highly customizable, allowing users to choose the key that initiates speech-to-text conversion.
- Once the spoken words have been converted to text format, the resulting text is automatically sent to the OpenAI API as a user prompt.
- The OpenAI API generates a response based on the user prompt, and the resulting text is converted back to speech format and played for the user.

## Technical Details
This project is built on top of cutting-edge technologies, including:
- OpenAI's GPT-3.5 architecture, which enables highly sophisticated natural language processing and text generation.
- Google Cloud Speech API, which leverages advanced machine learning techniques to accurately convert speech to text.
- A customizable key binding system, which is implemented using advanced keyboard input handling techniques.
- Audio output is generated using high-quality text-to-speech (TTS) libraries and APIs.

## Getting Started
Update the apt
`sudo apt update && cd AI_speech_assistant`

Install the package dependencies
`sudo apt-get install $(cat package.txt)`

Install the pip dependencies
`python3 -m pip install -r requirements.txt`

Make sure the mic is in working condition, set the sensitivity accordingly, by using tool like `pulseaudio`
plug the headphone jack, make sure the headphone has the mic button (button used to hangup call or pause music when pressed)

Set the Openai's GPT key as environmental varaible
`export API_KEY='your-key'`

Download the google-speech-to-text API key .json file and set the path of this file as environmental variable
`export GOOGLE_APPLICATION_CREDENTIALS='/path/to/secret.json'`


## Conclusion
Overall, this project is a powerful tool for anyone who needs to convert speech to text and back with minimal hassle. It leverages cutting-edge technologies to provide a seamless user experience and highly accurate results.
