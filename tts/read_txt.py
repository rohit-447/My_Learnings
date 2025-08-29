import pyttsx3
engine=pyttsx3.init()

#reads the txt file and store it in content
with open("tts/resources/readfile.txt", "r", encoding='utf-8') as f:
    content=f.read()

#Speak out content
engine.say(content)
engine.runAndWait()