#!/usr/bin/python

import speech_recognition as src
from gtts import gTTS
from playsound import playsound
import chime
import requests
from llama3 import Llama3Model
import webbrowser
import os
import urllib.request
import re


model = Llama3Model()
chime.theme('zelda')

#os.system("python a.py")

def intro():
    teks = ('Halo nama saya inem, katakan sesuatu setelah bunyi beep')
    bahasa = 'id'
    def speak():
        suara = gTTS(text=teks,lang=bahasa, slow=False)
        suara.save('sound.mp3')
        playsound('sound.mp3')
    speak()
    wakeword()
    
def wakeword():
    mendengar = src.Recognizer()
    with src.Microphone() as source:
        chime.info()
        print('+ Menunggu wakeword ...')
        suara = mendengar.listen(source,phrase_time_limit=2)
        try:
            dengar = mendengar.recognize_google(suara,language='id-ID')
            dengar = str(dengar).lower()
            print('+ Wakeword Diterima...')
            print('+ You: ', dengar)
            
            if('inem' in dengar):
                teks = ('Ya tuan, apa yang bisa saya bantu, silahkan katakan sesuatu setelah bunyi beep')
                bahasa = 'id'
                def speak():
                    suara = gTTS(text=teks,lang=bahasa, slow=False)
                    suara.save('sound.mp3')
                    playsound('sound.mp3')
                speak()
                chat()
            else:
                teks = ('maaf saya tidak mengerti maksud anda, silahkan anda ulangi kembali seteah bunyi beep')
                bahasa = 'id'
                def speak():
                    suara = gTTS(text=teks,lang=bahasa, slow=False)
                    suara.save('sound.mp3')
                    playsound('sound.mp3')
                speak()
                wakeword()
        except:
            pass
            wakeword()
            
def chat():
    chime.info()
    mendengar = src.Recognizer()
    with src.Microphone() as source:
        chime.info()
        print('+ Menunggu Perintah ...')
        suara = mendengar.listen(source,phrase_time_limit=5)
        try:
            dengar = mendengar.recognize_google(suara,language='id-ID')
            dengar = str(dengar).lower()
            print('+ Perintah Diterima...')
            print('+ You: ', dengar)

            if("buka youtube" in dengar ):             
                youtube()
            if('buka terminal'in dengar):
                terminal()
            if('buka browser'in dengar):
               browser()

            response = model.prompt(dengar)
            print("+ Inem:", response)
            teks = (response)
            bahasa = 'id'
            def speak():
                suara = gTTS(text=teks,lang=bahasa, slow=False)
                suara.save('sound.mp3')
                playsound('sound.mp3')
            speak()
            wakeword()
        except:
            pass
            wakeword()


def youtube():
    teks = ("Ucapkan kata kunci pencarian setelah bunyi beep")
    bahasa = 'id'
    def speak():
        suara = gTTS(text=teks,lang=bahasa, slow=False)
        suara.save('sound.mp3')
        playsound('sound.mp3')
    speak()
    chime.info()

    mendengar = src.Recognizer()
    with src.Microphone() as source:
         print('+ Menunggu Kata kunci pencarian ...')
         suara = mendengar.listen(source,phrase_time_limit=5)
         try:
          dengar = mendengar.recognize_google(suara,language='id-ID')
          dengar = str(dengar).lower()
          print('+ Kata kunci pencarian diterima...')           
          print('+ You: ', dengar)

          keyword=(dengar)
          webbrowser.open("https://www.youtube.com/results?search_query="+keyword,new=2)

          teks = ("Membuka youtube dengan kata kunci" + dengar)
          bahasa = 'id'
          def speak():
              suara = gTTS(text=teks,lang=bahasa, slow=False)
              suara.save('sound.mp3')
              playsound('sound.mp3')
          speak()
          wakeword()
         except:
            pass
            wakeword()


def terminal():
    teks = ("Membuka gnome-terminal")
    bahasa = 'id'
    def speak():
        suara = gTTS(text=teks,lang=bahasa, slow=False)
        suara.save('sound.mp3')
        playsound('sound.mp3')
    speak()
    os.system("gnome-terminal")
    wakeword()
    
def browser():
    teks = ("Ucapkan kata kunci pencarian setelah bunyi beep")
    bahasa = 'id'
    def speak():
        suara = gTTS(text=teks,lang=bahasa, slow=False)
        suara.save('sound.mp3')
        playsound('sound.mp3')
    speak()
    chime.info()

    mendengar = src.Recognizer()
    with src.Microphone() as source:
         print('+ Menunggu Kata kunci pencarian ...')
         suara = mendengar.listen(source,phrase_time_limit=5)
         try:
          dengar = mendengar.recognize_google(suara,language='id-ID')
          dengar = str(dengar).lower()
          print('+ Kata kunci pencarian diterima...')           
          print('+ You: ', dengar)

          keyword=(dengar)
          webbrowser.open("https://www.google.com/search?q="+keyword,new=2)

          teks = ("Membuka browser dengan kata kunci" + dengar)
          bahasa = 'id'
          def speak():
              suara = gTTS(text=teks,lang=bahasa, slow=False)
              suara.save('sound.mp3')
              playsound('sound.mp3')
          speak()
          wakeword()
         except:
            pass
            wakeword()
intro()

