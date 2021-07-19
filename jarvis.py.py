# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 09:25:24 2021

@author: ajit
"""

import pyttsx3
import speech_recognition as e
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
 #print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
     
    else:
        speak("Good Evening!")
        
    speak("Hello AJ i am jarvis. please tell me how can i help you")

def takeCommand():
    
    r = e.Recognizer()
    with e.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize.google(audio, Language='en-uk')
        print(f"User said:{query}\n")
        
    except Exception as e:
        
        print("Say that again please...")
        return"none"
    return query

if __name__ == "__main__":
    wishMe()
    takeCommand()
        
        
    
        
        
 