import speech_recognition as sr
import pyautogui as keyb

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
    keyb.keyDown('alt')
    keyb.press('enter')
    keyb.keyUp('alt')
    
except:
    pass