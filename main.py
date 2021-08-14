import pyttsx3
import speech_recognition as sr
import wikipedia
import pyjokes
import random
import requests
import datetime
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'barry' in command:
                command = command.replace('barry', '')
                print(command)
    except:
        pass
    return command


def start_barry():
    command = take_command()
    query = command().lower()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'news' in query:
        def trndnews():
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=59ff055b7c754a10a1f8afb4583ef1ab"
            page = requests.get(url).json()
            article = page["articles"]
            results = []
            for ar in article:
                results.append(ar["title"])
            for i in range(len(results)):
                print(i + 1, results[i])
            speak("here are the top trending news reports..")
            speak("Would you like me to read them?")
            reply = command().lower()
            reply = str(reply)
            if reply == "yes":
                speak(results)
            else:
                speak('Okay')
                pass
        trndnews()

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The Current time is ' + time)
    elif 'Hey Barry, who is' in command:
        person = command.replace('Hey Barry, who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'Are you still looking for love Barry?' in command:
        talk('I am in a relationship with wifi')

    elif 'Tell me a joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    start_barry()
