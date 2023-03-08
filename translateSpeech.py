from translate import Translator
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Ask the user for input
text = input("Enter the text you want to translate and convert to speech: ")
source_lang = input("Enter the source language (e.g. 'en' for English): ")
target_lang = input("Enter the target language (e.g. 'fr' for French): ")

# Translate the text to the target language
translator = Translator(from_lang=source_lang, to_lang=target_lang)
translation = translator.translate(text)

# Print the translation
print("Translation: ", translation)

# Convert the translated text to speech
engine.say(translation)
engine.runAndWait()
