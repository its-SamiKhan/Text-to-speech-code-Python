import pyttsx3

engine = pyttsx3.init()

Text=input("Enter the text:")

engine.say(Text)
engine.runAndWait()
engine.stop()
