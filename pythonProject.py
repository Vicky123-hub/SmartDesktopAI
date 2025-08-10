import pyttsx3
import speech_recognition as sr
from datetime import datetime
import pyjokes
import wikipedia
import webbrowser
import requests
import os

recognizor=sr.Recognizer() 
engine=pyttsx3.init()

with sr.Microphone() as source:
    print("Listening.....")
    engine.say('Hello how can i help you.')
    engine.runAndWait()
    audio=recognizor.listen(source)

try:
    text=recognizor.recognize_google(audio)
    if 'what is the time' in text.lower():
        now=datetime.now()
        current_time=now.strftime('%I: %M %p')
        engine.say(current_time)
        engine.runAndWait()
    elif 'tell me a joke' in text.lower():
        joke=pyjokes.get_joke()
        engine.say(joke)
        engine.runAndWait()
    elif 'google' in text.lower():
        search_query=text.replace('search on google',"").strip()
        engine.say(f'searching on google for {search_query}')
        engine.runAndWait()
        url=f'https://www.google.com/search?q={search_query}'
        webbrowser.open(url)
    elif 'wikipedia' in text.lower():
        search_query=text.replace('search on wikipedia',"")
        engine.say(f'searching on wikipedia for {search_query}')
        engine.runAndWait()
        result = wikipedia.summary(search_query, sentences=2)
        engine.say(result)
        engine.runAndWait()
    else:
        engine.say('sorry i can not hear you.')
        engine.runAndWait()
except sr.UnknownValueError:
    engine.say('Can not hear you')
    engine.runAndWait()
except sr.RequestError:
    engine.say('Check your internet')
    engine.runAndWait()
