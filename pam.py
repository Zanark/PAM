import speech_recognition as sr

#print(sr.__version__)

r = sr.Recognizer()
mic = sr.Microphone()
#sr.Microphone.list_microphone_names()

with mic as src:
    print("\n\nbol")
    audio = r.listen(src)
    print("sun liya")

try:
    print("\n\nRecognized o/p: "+r.recognize_google(audio))
except:
    pass