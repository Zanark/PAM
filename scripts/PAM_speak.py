from gtts import gTTS
import os

def speak(sentence):
    tts = gTTS(sentence, lang="hi")
    tts.save('PAM_auOP.mp3')
    os.system('mpg123 PAM_auOP.mp3')
