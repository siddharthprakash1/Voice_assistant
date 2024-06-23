# AI Voice Assistant with Webcam

This project implements an AI voice assistant that uses speech recognition, text-to-speech, and a webcam feed. It's powered by the Llama 3 language model through Ollama.

## Features

- Speech recognition using Google Speech Recognition
- Text-to-speech response using pyttsx3
- Webcam feed display
- AI-powered responses using Llama 3 model via Ollama
- Conversation history management with LangChain

## Requirements

- Python 3.x
- OpenCV (cv2)
- pyttsx3
- SpeechRecognition
- LangChain
- Ollama
- python-dotenv

## Installation

1. Clone this repository:->git clone https://github.com/yourusername/ai-voice-assistant.git
                         ->cd ai-voice-assistant
2. Install the required packages: from the requirnment.txt file
 Package                  Version
------------------------ -----------
aiohttp                  3.9.5
aiosignal                1.3.1
annotated-types          0.7.0
asttokens                2.4.1
async-timeout            4.0.3
attrs                    23.2.0
beautifulsoup4           4.12.3
certifi                  2024.6.2
charset-normalizer       3.3.2
colorama                 0.4.6
comm                     0.2.2
comtypes                 1.4.4
dataclasses-json         0.6.7
debugpy                  1.8.1
decorator                5.1.1
docopt                   0.6.2
exceptiongroup           1.2.0
executing                2.0.1
frozenlist               1.4.1
greenlet                 3.0.3
idna                     3.7
ipykernel                6.29.4
ipython                  8.23.0
jedi                     0.19.1
Js2Py                    0.74
jsonpatch                1.33
jsonpointer              3.0.0
jupyter_client           8.6.1
jupyter_core             5.7.2
langchain                0.2.5
langchain-community      0.2.5
langchain-core           0.2.9
langchain-text-splitters 0.2.1
langsmith                0.1.81
marshmallow              3.21.3
matplotlib-inline        0.1.6
multidict                6.0.5
mypy-extensions          1.0.0
nest-asyncio             1.6.0
numpy                    1.26.4
opencv-python            4.10.0.84
orjson                   3.10.5
packaging                24.1
parso                    0.8.4
pip                      24.0
pipwin                   0.5.2
platformdirs             4.2.0
prompt-toolkit           3.0.43
psutil                   5.9.8
pure-eval                0.2.2
PyAudio                  0.2.11
pydantic                 2.7.4
pydantic_core            2.18.4
Pygments                 2.17.2
pyjsparser               2.7.1
pypiwin32                223
PyPrind                  2.11.3
pySmartDL                1.3.4
python-dateutil          2.9.0.post0
python-dotenv            1.0.1
pyttsx3                  2.90
pywin32                  306
PyYAML                   6.0.1
pyzmq                    25.1.2
requests                 2.32.3
setuptools               69.5.1
six                      1.16.0
soupsieve                2.5
SpeechRecognition        3.10.4
SQLAlchemy               2.0.31
stack-data               0.6.3
tenacity                 8.4.1
tornado                  6.4
traitlets                5.14.2
typing_extensions        4.11.0
typing-inspect           0.9.0
tzdata                   2024.1
tzlocal                  5.2
urllib3                  2.2.2
wcwidth                  0.2.13
wheel                    0.43.0
yarl                     1.9.4  
3. Make sure you have Ollama installed and the Llama 3 model downloaded:
4.then run the script


2. The webcam feed will open, and the voice assistant will start listening.

3. Speak into your microphone to interact with the AI assistant.

4. Press 'q' or 'Esc' to exit the program.

## How it works

1. The program initializes a webcam stream and speech recognition.
2. It uses Google Speech Recognition to convert speech to text.
3. The text is sent to the Llama 3 model via Ollama for processing.
4. The AI generates a response, which is then converted to speech using pyttsx3.
5. The conversation history is managed using LangChain.

## Customization

You can modify the `SYSTEM_PROMPT` in the `Assistant` class to change the AI's behavior and personality.

## Future Improvements

We are planning to enhance this project with the following features:

1. **Search Engine Integration**: This will allow the AI assistant to access and provide information from the internet, greatly expanding its knowledge base and capabilities.

2. **Video Input Processing**: We aim to implement webcam tracking and computer vision algorithms to enable the assistant to take input from video data. This will allow for features such as gesture recognition, object detection, and visual question answering.

These improvements will make the assistant more versatile and capable of handling a wider range of inputs and tasks.

## License

[MIT License](LICENSE)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer

This project uses Google Speech Recognition, which may have usage limits or require an API key for extended use. Make sure to comply with their terms of service.
