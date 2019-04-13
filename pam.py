import speech_recognition as sr
import pyautogui as keyb
import re
import subprocess as sp

#print(sr.__version__)

r = sr.Recognizer()
mic = sr.Microphone()
#sr.Microphone.list_microphone_names()

with mic as src:
    print("\n\nbol")
    audio = r.listen(src)
    print("sun liya")

try:
    result = r.recognize_google(audio)
    print("\n\nRecognized o/p: "+result)

    #terminal check
    x = re.findall("terminal+|command line|commandline", result)
    print(x)
    if(len(x)>0):
        keyb.keyDown('alt')
        keyb.press('enter')
        keyb.keyUp('alt')
    
    #watch anime
    x = re.findall("anime+", result)
    print(x)
    if(len(x)>0):
        sp.run(["firefox", "-new-tab", "http://kissanime.ru"])
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))