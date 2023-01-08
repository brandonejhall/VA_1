import datetime
import pyttsx3
import speech_recognition as sr 
import webbrowser
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import requests, json


def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print('Hello, I am your Virtual Assistant. How Can I Help You Today')
        respond('Hello, I am your Virtual Assistant. How Can I Help You Today')
        audio = r.listen(source)

    data = ''

    try:

        data = r.recognize_google(audio)

        print('You said: ' + data)
        digital_assistant(data)

    except sr.UnknownValueError:

        print('Sorry! Audio was not recognized by Google Speech Recognition.')

    except sr.RequestError as e:

        print(f'Request Failed; {0}'.format(e))

    return data


def respond(audioString):

    print(audioString)

    tts = gTTS(text=audioString, lang="en")

    tts.save("speech.mp3")

    os.system("mpg123 speech.mp3")


def digital_assistant(data):

    listening = False

    if "how are you doing" in data:

        listening = True

        respond("I am well")

 

    if "what time is it exactly" in data:

        listening = True

        respond(ctime())

    if "stop listening" in data:

        listening = False

        print('Sorry! Listening stopped')

        return listening

    return listening


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        respond("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        respond("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        respond("Hello,Good Evening")
        print("Hello,Good Evening")