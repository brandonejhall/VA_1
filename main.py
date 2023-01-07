import pyttsx3
import speech_recognition as sr 
import webbrowser
import speech_recognition as sr
from time import ctime
import time
import os
#from gtts import gTTS
import requests, json


def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print('Hello, I am your Virtual Assistant. How Can I Help You Today')

        audio = r.listen(source)

    data = ''

    try:

        data = r.recognize_google(audio)

        print('You said: ' + data)

    except sr.UnknownValueError:

        print('Sorry! Audio was not recognized by Google Speech Recognition.')

    except sr.RequestError as e:

        print(f'Request Failed; {0}'.format(e))

    return data