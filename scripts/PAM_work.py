import speech_recognition as sr
import pyautogui as keyb
import re
import subprocess as sp
import time
import sys
from gtts import gTTS
import os

from pydub import AudioSegment as AS

FILE_LOC = os.path.dirname(os.path.realpath(__file__))
#print(FILE_LOC)

def speak(sentence, lng):
    tts = gTTS(sentence, lang=lng)      #gTTS at work
    tts.save('auOP.mp3')                #saving as mp3
    tts_op = AS.from_mp3('auOP.mp3')
    tts_op.export('auOP.wav', format="wav") #making a wav file with same audio
    
    sound = AS.from_file('auOP.wav', format="wav")  #using the wav file for increasing pitch and frame rate
    new_sample_rate = int(sound.frame_rate * 1.4)
    
    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    hipitch_sound = hipitch_sound.set_frame_rate(44100)
    hipitch_sound.export("auOP-hp.wav", format="wav")
    
    os.system('aplay ./auOP-hp.wav')
    os.system('rm auOP.wav auOP.mp3')

def tasks(r, audio):
    try:
        result = r.recognize_google(audio)
        print("\n\nRecognized o/p: "+result)
        sp.run(["notify-send", "--expire-time=1800", "--icon="+FILE_LOC+"/../assets/rem.svg", "PAM", "You said:  "+result])
        #speak("You said:  "+result)

        #-------------------open a terminal
        x = re.findall("terminal+|command line|commandline", result, re.IGNORECASE)
        print(x)
        if(len(x)>0):
            keyb.keyDown('alt')
            keyb.press('enter')
            keyb.keyUp('alt')
        
        #-------------------Lets watch anime!
        x = re.findall("anime+", result, re.IGNORECASE)
        print(x)
        if(len(x)>0):
            sp.run(["firefox", "-new-tab", "http://kissanime.ru"])

        #-------------------lock my screen
        x = re.findall("lock+|gotta go|need to go|susu|pee", result, re.IGNORECASE)
        print(x)
        if(len(x)>0):
            keyb.keyDown('winleft')
            keyb.press('v')
            keyb.keyUp('winleft')

        #-------------------reddit/popular
        x = re.findall("reddit+", result, re.IGNORECASE)
        print(x)
        if(len(x)>0):
            sp.run(["firefox", "-new-tab", "https://www.reddit.com/r/popular"])

        #-------------------reddit/r/unixporn
        x = re.findall("unix+|porn+|unix porn|nix|ricing subreddit|ricing thread", result, re.IGNORECASE)
        print(x)
        if(len(x)>0):
            sp.run(["firefox", "-new-tab", "https://www.reddit.com/r/unixporn"])

        #-------------------Lets Play Minecraft!
        x = re.findall("minecraft+", result, re.IGNORECASE)
        print(x)
        if(len(x)>0):
            keyb.keyDown('winleft')
            keyb.press('m')
            keyb.keyUp('winleft')

        #-------------------PAM on ITER
        x = re.findall("i t e r|iter|[iter][iter][iter][iter]|college", result, re.IGNORECASE)
        print(x)
        if(len(x)>0):
            sp.run(["notify-send", "--expire-time=2000", "--icon="+FILE_LOC+"/../assets/rem.svg", "PAM", "ITER ka maa ka bhosda"])
            speak("I T E R ka maa ka bhosda", "hi")

        #-------------------IF PAM IS ASKED TO STOP
        x = re.findall("stop listening|stop+|terminate+", result, re.IGNORECASE)
        print(x)
        if(len(x)>0):
            sp.run(["notify-send", "--expire-time=1500", "--icon="+FILE_LOC+"/../assets/rem.svg", "PAM", "Goodbye, Zanark"])
            speak("Sayonara Zaanark!", "ja")
            sys.exit("Goobye Zanark")
    
    except sr.UnknownValueError:
        print("\n\nGoogle Speech Recognition could not understand audio")
        sp.run(["notify-send", "--expire-time=1500", "--icon="+FILE_LOC+"/../assets/rem.svg", "PAM", "Google Speech Recognition could not understand audio"])

    except sr.RequestError as e:
        print("\n\nCould not request results from Google Speech Recognition service; {0}".format(e))
        sp.run(["notify-send", "--expire-time=1500", "--icon="+FILE_LOC+"/../assets/rem.svg", "PAM", "Could not request results from Google Speech Recognition service; {0}".format(e)])

############################################################------PAM_work() ends
