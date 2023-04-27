import os
import pyttsx3

path = f"assets/output.txt"

engine = pyttsx3.init(driverName='sapi5')
with open(path, 'r',encoding='utf-8') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

engine.say(lines)
engine.runAndWait()

lines = ['']
with open(path, 'w',encoding='utf-8') as f:
    f.write('')

