import pyautogui as keyb
import re
import subprocess as sp
import time
import sys
import os

FILE_LOC = os.path.dirname(os.path.realpath(__file__))
#print(FILE_LOC)

def tasks(r, audio):
    try:
        result = r.recognize_google(audio)
        print("\n\nRecognized o/p: "+result)
        sp.run(["notify-send", "--expire-time=1500", "--icon="+FILE_LOC+"/../assets/rem.svg", "PAM", "You said:  "+result])

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
            sp.run(["notify-send", "--expire-time=2000", "--icon="+FILE_LOC+"/../rem.svg", "PAM", "ITER ka maa ka bhosda"])

        #-------------------IF PAM IS ASKED TO STOP
        x = re.findall("stop listening|stop+|terminate+", result, re.IGNORECASE)
        print(x)
        if(len(x)>0):
            sp.run(["notify-send", "--expire-time=1500", "--icon="+FILE_LOC+"/../rem.svg", "PAM", "Goodbye, Zanark"])
            sys.exit("Goobye Zanark")
    
    except sr.UnknownValueError:
        print("\n\nGoogle Speech Recognition could not understand audio")
        sp.run(["notify-send", "--expire-time=1500", "--icon="+FILE_LOC+"/../rem.svg", "PAM", "Google Speech Recognition could not understand audio"])
    except sr.RequestError as e:
        print("\n\nCould not request results from Google Speech Recognition service; {0}".format(e))
        sp.run(["notify-send", "--expire-time=1500", "--icon="+FILE_LOC+"/../rem.svg", "PAM", "Could not request results from Google Speech Recognition service; {0}".format(e)])

############################################################------PAM_work() ends
