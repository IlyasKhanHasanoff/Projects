import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Ask the user for input
text = input("Enter the text you want to convert to speech: ")

# Convert the text to speech
engine.say(text)
engine.runAndWait()
