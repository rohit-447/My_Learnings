import pyttsx3

#instance of module
engine=pyttsx3.init()

#.say is used to conver the text into speech 
engine.say("Hello World")

#getting the properties 
voices=engine.getProperty('voice')  #This returns the list of voices present in the devices returns as object
#print(voices)

#This print all the voices which are present in the device
# for voices in voices:
#     print(voices)

#change of any property [Currently having some error]
# engine.setProperty('voices', voices[1].id)


#change of volume 0 -> min 1-> max
#engine.setProperty('volume', 0.0)
#engine.say("Hello World")

#change of rate
# engine.setProperty('rate',200)
# engine.say("Hello World I am speaking much slower now than the default speed. This should be easy to notice if I keep talking for longer")
engine.runAndWait()