import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import webbrowser

user = "" #enter your name
assistant_name = "" #enter your assistant name

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id) #0 for male 1 for female
    engine.say(audio)
    engine.runAndWait()


def takeVoice():
    Hello()

    while(True):
        query = takeCommand().lower()

        #enter commands here
        if "open google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")
        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")
        elif "what is the time" in query:
            speak(datetime.datetime.now().strftime("%H:%M:%S"))
        elif "what is the date" in query:
            speak(datetime.datetime.now().strftime("%d/%m/%Y"))
        elif "bye" in query:
            speak("Bye " + user)
            exit()
        elif "wikipedia" in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif "what is your name" in query:
            speak("My name is " + assistant_name)

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-us') #language
            print(f"User said: {query}\n")
        
        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"

        return query

def Hello():
    speak("Hello " + user)
    speak("How can I help you?")

if __name__ == "__main__":
    takeVoice()