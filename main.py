import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime
import pyautogui
import pyautogui as pg

def alexis_code():
    r = sr.Recognizer()

    def record_audio(ask = False):
        with sr.Microphone() as source:
            if ask:
                alexis_speak(ask)
            audio = r.listen(source)
            voice_data = ''
            try:
                voice_data = r.recognize_google(audio)
            except sr.UnknownValueError:
                alexis_speak("Sorry, Please Try Again")
            except sr.RequestError:
                alexis_speak('Sorry My Services are Down')
            return voice_data

    def alexis_speak(audio_string):
        tts = gTTS(text=audio_string, lang='en')
        r = random.randint(1, 10000000)
        audio_file = 'audio-' + str(r) + '.mp3'
        tts.save(audio_file)
        playsound.playsound(audio_file)
        print(audio_string)
        os.remove(audio_file)

    def respond(voice_data):
        alexis_speak('How May I Help?')
        voice_data = record_audio()
        time.sleep(1)
        if 'what is your name' in voice_data:
            alexis_speak('My Name is Alexis')
        elif 'hey' in voice_data:
            alexis_speak('here')
            url = 'https://www.youtube.com/watch?v=gNhN6lT-y5U'
            webbrowser.get().open(url)
        elif 'what time is it' in voice_data:
            alexis_speak(ctime())
        elif 'search' in voice_data:
            search = record_audio('What Do You Want To Search For?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            alexis_speak('Here is what I found for ' + search)
        elif 'find location' in voice_data:
            location = record_audio('Where do you want to go?')
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.get().open(url)
            alexis_speak('Have a nice time in ' + location)
        elif 'turn off' in voice_data:
            alexis_speak('Goodbye')
            exit()
        elif 'who created you' in voice_data:
            alexis_speak('Some asshole created me instead of doing schoolwork')
        elif 'who is Public Enemy number one' in voice_data:
            alexis_speak('Joe the little shit')
        elif 'thank you' in voice_data:
            alexis_speak('No Problem')
        elif 'cheers' in voice_data:
            alexis_speak('No Baw')
        elif 'what do you think of Siri' in voice_data:
            alexis_speak('tramp')
        elif 'what do you think of Google' in voice_data:
            alexis_speak('I cant say anything bad about google because my Text to Speech comes from them')
        elif 'what do you think of Cortana' in voice_data:
            alexis_speak('garbage')
        elif 'pause' in voice_data:
            alexis_speak('Pausing Now')
            pyautogui.press('playpause')
        elif 'play' in voice_data:
            alexis_speak('Continuing Now')
            pyautogui.press('playpause')
        elif 'YouTube' in voice_data:
            search = record_audio('What Do You Want To Search Youtube For?')
            url ='https://www.youtube.com/results?search_query=' + search
            alexis_speak('Here is what I found for ' + search)
            webbrowser.get().open(url)
            pg.moveTo(500, 500, 0.1)
            time.sleep(3)
            pg.leftClick(500, 500, 5)
        elif 'Spotify' in voice_data:
            alexis_speak('opening spotify')
            os.startfile('spotify.exe')
            pg.moveTo(470, 21, 0.1)
            alexis_speak('What Would You Like Me To Play?')
            songname = record_audio()
            pg.tripleClick(470, 21)
            time.sleep(1)
            pg.press('delete')
            time.sleep(2)
            pg.leftClick(470, 21,2)
            pg.write(songname)
            print(songname)
            time.sleep(2)
            pg.moveTo(420, 187, 0.1)
            pg.leftClick(420, 187, 1)
        elif 'f*** you' in voice_data:
            playsound.playsound("C:\\Users\\Sam\\PycharmProjects\\AI\\MP3s\\heyman.mp3")
        elif "I don't like you" in voice_data:
            playsound.playsound("C:\\Users\\Sam\\PycharmProjects\\AI\\MP3s\\ThenYouShallDie.mp3")
        elif 'Who You Gonna Call' in voice_data:
            playsound.playsound("C:\\Users\\Sam\\PycharmProjects\\AI\\MP3s\\WeAreReadyToBelieveYou.mp3")
        elif "we're on a mission from god" in voice_data:
            playsound.playsound("C:\\Users\\Sam\\PycharmProjects\\AI\\MP3s\\106Miles.mp3")
        elif 'scream' in voice_data:
            playsound.playsound("C:\\Users\\Sam\\PycharmProjects\\AI\\MP3s\\Scream.mp3")
        elif 'I shall stab you' in voice_data:
            playsound.playsound("C:\\Users\\Sam\\PycharmProjects\\AI\\MP3s\\TisButAScratch.mp3")

    voice_data = record_audio()

    if 'Alexis' in voice_data:
        alexis_speak('Hello')
        respond(voice_data)

    else:
        print('No Wake Word Detected')

while True:
    alexis_code()

