#!/usr/bin/env python3

"""Speech to Text Python3 code to generate output file from what you said base on selected language.
The code is written By Babak Emadi Nikoo"""

import speech_recognition as sr


r = sr.Recognizer()

print('''Select your speaking language: 
1) English
2) Persian
3) Dutch ''')
lang = input()

if lang == '1':
    with sr.Microphone() as source:
        print("Please tell your text...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language= 'en-US')
        print("You said: ", text)
        
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(text)
            print("Output saved to output.txt file.")
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

elif lang == '2':
    with sr.Microphone() as source:
        print(":لطفا متن خود را بخوانید")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language='fa-IR')
        print("آنچه شما گفتید: ", text)
        
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(text)
            print("متن شما در فایل output.txt ذخیره شده است.")
    except sr.UnknownValueError:
        print("صدای شما قابل تشخیص نمی باشد.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

else:
    with sr.Microphone() as source:
        print("Sprechen Sie jetzt...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio, language= 'de-DE')
        print("Sie haben gesagt: ", text)
        
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(text)
            print("Ausgabe wurde in output.txt Datei gespeichert.")
    except sr.UnknownValueError:
        print("Konnte Sprache nicht verstehen")
    except sr.RequestError as e:
        print("Konnte keine Ergebnisse von Google Speech Recognition Service abrufen; {0}".format(e))
