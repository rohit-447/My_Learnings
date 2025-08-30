#Reading the audio file and convert this into text
import speech_recognition as sr
recognizer=sr.Recognizer()

try: 
 with sr.AudioFile("Speech_Recognation/resource/audiofile.mp3") as source:
    audio =recognizer.record(source)

except Exception as e:
    print(e)

text=recognizer.recognize_google(audio)
print(f"Audio file Says, {text}")
