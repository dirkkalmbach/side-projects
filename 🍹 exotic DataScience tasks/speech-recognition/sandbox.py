#%%
import speech_recognition as sr
import pyttsx3
#%%
# TEXT-TO-SPEAK ✅
# initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

SpeakText("Hey, Dirk. Have a nice day!")

#%%
# SPEEK-TO-TEXT

with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2, duration=0.2)

    audio2 = r.listen(source2)

    #MyText = r.recognize_google(audio2)
    #MyText = MyText.lower()

    #print("Did you say " + MyText)
    #SpeakText(MyText)
# %%
audio2
# %%


# %%
