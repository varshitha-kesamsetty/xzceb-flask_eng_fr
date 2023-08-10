"""
start program
"""
import json
import os
from deep_translator import MyMemoryTranslator

#function to convert english to french
def english_to_french(english_text):
    french_text = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(english_text)
    print(french_text)
    return french_text
#function to convert french to english
def french_to_english(french_text):
    english_text=MyMemoryTranslator(source='fr-FR',target='en-GB').translate(french_text)
    print(english_text)
    return english_text
