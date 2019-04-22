import speech_recognition as sr
import PAM_work
#print(sr.__version__)


r = sr.Recognizer()
mic = sr.Microphone()
#sr.Microphone.list_microphone_names()
r.dynamic_energy_threshold = False
r.energy_threshold = 350

while True:
    with mic as source:
        print("\n\nbol")
        r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening
        audio = r.listen(source, timeout=5, phrase_time_limit=7)
        tasks(r, audio)
        print("\nsun liya")
