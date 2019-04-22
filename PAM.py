import speech_recognition as sr
from scripts.PAM_work import *
#print(sr.__version__)


r = sr.Recognizer()
mic = sr.Microphone()
#sr.Microphone.list_microphone_names()
r.dynamic_energy_threshold = False
r.energy_threshold = 400

while True:
    with mic as source:
        print("\n\nbol")
        r.adjust_for_ambient_noise(source, duration=0.5) # we only need to calibrate once, before we start listening
        audio = r.listen(source, timeout=3, phrase_time_limit=4)
        tasks(r, audio)
        print("\nsun liya")
