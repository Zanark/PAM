import speech_recognition as sr

#print(sr.__version__)

r = sr.Recognizer()

with sr.Microphone() as src:
    audio = r.listen(src)
    print("sun liya")

try:
    print("Recognized o/p: "+r.recognize_google(audio))
except:
    pass