from translate import Translator

# Ask the user for input
text = input("Enter the text you want to translate: ")
source_lang = input("Enter the source language (e.g. 'en' for English): ")
target_lang = input("Enter the target language (e.g. 'fr' for French): ")

# Create a translator object and translate the text
translator = Translator(from_lang=source_lang, to_lang=target_lang)
translation = translator.translate(text)

# Print the translated text
print("Translation: ", translation)
