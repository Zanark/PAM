import pyttsx3 as tts
import time

engine = tts.init()
voices = engine.getProperty('voices')
print(len(voices))
for voice in voices:
    print(voice)
    if(voice.name != 'english'):
        continue
    engine.setProperty('voice', 'english+f3')
    engine.say('The quick brown fox jumped over the lazy dog.')
    time.sleep(2)
    engine.runAndWait()


