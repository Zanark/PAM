import speech_recognition as sr
import pyautogui as keyb
import re
import subprocess as sp

#print(sr.__version__)

def PAM_work(r, audio):
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

############################################################------PAM_work() ends

r = sr.Recognizer()
mic = sr.Microphone()
#sr.Microphone.list_microphone_names()

with mic as source:
    r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

# start listening in the background
stop_listening = r.listen_in_background(mic, PAM_work)

# with mic as src:
#     print("\n\nbol")
#     audio = r.listen(src)
#     print("sun liya")

for _ in range(50): time.sleep(0.1)  # we're still listening even though the main thread is doing other things

# calling this function requests that the background listener stop listening
stop_listening(wait_for_stop=False)

# do some more unrelated things
while True: time.sleep(0.1) # we're not listening anymore, even though the background thread might still be running for a second or two while cleaning up and stopping

