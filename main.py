#-*- coding:UTF-8 -*-
import speech_recognition as sr
import os
import sys
import webbrowser
# import urllib

def talk(words):
    print(words)
    os.system("say " + words)
talk("Голосовой поиск по Youtube")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talk("Что нужно найти?")
        print("Говорите")
        # r.pause_threshold = 0.8
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        komanda = str(r.recognize_google(audio, language="ru_RU").lower())
        print("Ваша команда: " + komanda)
        talk("Идет поиск")

        url = str('https://www.youtube.com/results?search_query='+komanda).replace(' ', '+')
        os.system("open \"\"" + url)
        sys.exit()

        # webbrowser.open(url)

    except sr.UnknownValueError:
        # talk("Я Вас не поняла")
        komanda = command()

    return komanda

def makeSomething(komanda):
    if 'найди в instagram мою жену'.lower() in komanda:
        talk("Идет поиск")
        url = ("https://www.youtube.com/results?search_query=" + komanda)
        webbrowser.open(url.decode('utf-8'))
    elif 'стоп' in komanda:
        talk("ОК, без проблем")
        sys.exit()
while True:
    makeSomething(command())

