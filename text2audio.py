
from gtts import gTTS
from playsound import playsound

audio = 'speach.mp3'
language = 'en'
sp = gTTS(text= "Sounak is fat", lang= language,slow=False)

sp.save(audio)
playsound(audio)