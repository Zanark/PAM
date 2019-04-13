import speech_recognition as sr
import pyautogui as keyb
import re
import subprocess as sp
import time

#print(sr.__version__)

def PAM_work(r, audio):
    try:
        result = r.recognize_google(audio)
        print("\n\nRecognized o/p: "+result)

        #-------------------terminal check
        x = re.findall("terminal+|command line|commandline", result)
        print(x)
        if(len(x)>0):
            keyb.keyDown('alt')
            keyb.press('enter')
            keyb.keyUp('alt')
        
        #-------------------watch anime
        x = re.findall("anime+", result)
        print(x)
        if(len(x)>0):
            sp.run(["firefox", "-new-tab", "http://kissanime.ru"])
    
    except sr.UnknownValueError:
        print("\n\nGoogle Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("\n\nCould not request results from Google Speech Recognition service; {0}".format(e))

############################################################------PAM_work() ends

r = sr.Recognizer()
mic = sr.Microphone()
#sr.Microphone.list_microphone_names()
r.dynamic_energy_threshold = False
r.energy_threshold = 350

with mic as source:
    print("\n\nbol")
    r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening
    audio = r.listen(source, timeout=1, phrase_time_limit=7)
    PAM_work(r, audio)
    print("\nsun liya")
