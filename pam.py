import speech_recognition as sr
import pyautogui as keyb
import re

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
    x = re.findall("terminal+", result)
    print(x)
    if(len(x)>0):
        keyb.keyDown('alt')
        keyb.press('enter')
        keyb.keyUp('alt')
    
except:
    pass