#!pip install SpeechRecpgnition
#!pip install pyaudio

#takes the input from microphone and convert into text
import speech_recognition as sr

#create instance 
reconizer=sr.Recognizer()


with sr.Microphone() as source:
    print("Start Speaking")
    audio=reconizer.listen(source)  #listen until scilence

#convert speech into txt
try:
    text=reconizer.recognize_google(audio)
    print(f"You said, {text}")
except sr.UnknownValueError:
    print("Not clear voice")
except sr.RequestError:
    print("Internet or API issue")