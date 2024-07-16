#!/usr/bin/python

import speech_recognition as src
from gtts import gTTS
from playsound import playsound
import chime
import requests

chime.theme('zelda')

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
            if('nyalakan pompa' in dengar ):
              res = requests.get('http://192.168.0.155/cm?cmnd=POWER+TOGGLE')
              teks = ('Pompa sudah dinyalakan')
              bahasa = 'id'         
              def reading():
                  suara = gTTS(text=teks, lang=bahasa, slow=False)
                  suara.save('sound.mp3')
                  playsound('sound.mp3')
              reading()
              
            elif ('matikan pompa' in dengar):
              res = requests.get('http://192.168.0.155/cm?cmnd=POWER+TOGGLE')
              teks = ('Pompa sudah dimatikan')
              bahasa = 'id'   
              def reading():
                  suara = gTTS(text=teks, lang=bahasa, slow=False)
                  suara.save('sound.mp3')
                  playsound('sound.mp3')
              reading()

            elif ('nyalakan lampu gudang' in dengar):
              res = requests.get('http://192.168.0.151/cm?cmnd=POWER+TOGGLE')
              teks = ('Lampu gudang sudah dinyalakan')
              bahasa = 'id'   
              def reading():
                  suara = gTTS(text=teks, lang=bahasa, slow=False)
                  suara.save('sound.mp3')
                  playsound('sound.mp3')
              reading()

            elif ('matikan lampu gudang' in dengar):
              res = requests.get('http://192.168.0.151/cm?cmnd=POWER+TOGGLE')
              teks = ('Lampu gudang sudah dimatikan')
              bahasa = 'id'   
              def reading():
                  suara = gTTS(text=teks, lang=bahasa, slow=False)
                  suara.save('sound.mp3')
                  playsound('sound.mp3')
              reading()
            wakeword()
        except:
            pass
            wakeword()

intro()
