import pyassistant
import speech_recognition as sr
from gtts import gTTS
import os
# all the basic  libraries inserted.

sr.Microphone(device_index=1)

r=sr.Recognizer()
r.energy_threshold=5000
with sr.Microphone() as source:
        with sr.Microphone() as source:
            print("speak!")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            app_id = "THGUP6-HL5RVQK8KW"
            # unique wolfram ID
            client = pyassistant.Client(app_id)
            res = client.query(text)
            answer = next(res.results).text
            print("You asked : {}".format(text))
            print(answer)
            mytext = answer
            language = 'HI'
            # Hindi language is here. You can change it "EN" for english.
            myobj = gTTS(text=mytext, la  ng=language)
            myobj.save("welcome.mp3")
            os.system("welcome.mp3")
        except:
            print("Sorry I don't know, Will work harder next time ")
            mytext = 'Sorry I dont know, Will work harder next time'
            language = 'HI'
            myobj = gTTS(text=mytext, lang=language)
            myobj.save("welcome.mp3")
            os.system("welcome.mp3")
