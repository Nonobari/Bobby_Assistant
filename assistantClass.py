import autocorrect
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import pywhatkit
import pywikihow
import os
from requests.utils import unquote
import pytube
import speedtest
import wolframalpha
from pytube.cli import on_progress
from dictionaries import *
import random as rd
import sys
import subprocess


now = datetime.now()
spell = autocorrect.Speller(lang='fr')

class Assistant:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
        self.discussionMode = False
        self.engine = pyttsx3.init(driverName='sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voices',self.voices[1].id)
        self.engine.setProperty('rate',200)
        self.path = f"{os.getcwd()}\\assets\\output.txt"
        self.output(rd.choice(hi[testTime()]),overWrite=False)
        
    def __repr__(self) -> str:
        return f"Assistant({self.name},{self.age})"

    def __str__(self) -> str:
        return f"{self.name} a {self.age} ans"

    def speak(self,audio,overWrite = False):
        if overWrite:
            with open("assets\\output.txt","w",encoding='utf-8') as f:
                f.write(audio)
        else:
            with open('assets\\output.txt','a',encoding='utf-8') as f:
                f.write(f"{audio}\n")
        global pid
        pid = subprocess.Popen([sys.executable, "speaking.py"]) # Call subprocess

    def listening(self):
        global pidListening
        pidListening = subprocess.Popen([sys.executable, "listening.py"]) # Call subprocess
    
    
    def write(self,text,affichageAssistantName = True):
        if affichageAssistantName:
            print(f"{self.name} : {text}")
        else: print(text)
    
    def output(self,audio ,text = None, affichageAssistantName = True,overWrite = True):
        if text == None:
            text = audio
        Assistant.speak(self,audio,overWrite)
        Assistant.write(self,text,affichageAssistantName)

    def inputAssistant(self):
        pass
 
    def reading(self,correction = True):
        query = input("User : ")
        # print(f"Your command : {query.lower()}\n")
        co = open('assets\\command.txt','a')
        co.write(f"{now} | {query}\n")
        co.close()
        if correction:
            if not any(word in ignoredWords for word in query.split(" ")):
                query = spell(query)
        return query.lower()

    def youtubeSearch(self,term):
        # result = "https://www.youtube.com/results?search_query=" + term
        self.output(f"Voici ce que j'ai trouvé sur YouTube")
        pywhatkit.playonyt(term)

    def spotifySearch(self,term):
        self.output(f"Cette fonctionnalité n'est pas encore au point, lancement de {term} sur YouTube")
        pywhatkit.playonyt(term)

    def deezerSearch(self,term):
        self.output(f"Cette fonctionnalité n'est pas encore au point, lancement de {term} sur YouTube")
        pywhatkit.playonyt(term)


    def musicPlayer(self,query):
        self.output(f"Sur quelle platforme voulez vous écouter {query} ?")
        reponse = self.reading(correction=False)
        if "spotify" in reponse:
            Assistant.spotifySearch(self,query)
        elif "deezer" in reponse:
            Assistant.deezerSearch(self,query)
        elif "youtube" in reponse:
            Assistant.youtubeSearch(self,query)

    def wikiSearch(self,term,lenght = 1):
        wikipedia.set_lang("fr")
        try:
            pageTitles = wikipedia.search(term)
            result = wikipedia.summary(pageTitles[0],sentences=lenght,auto_suggest=False)
            self.output(result)
        except wikipedia.exceptions.PageError or wikipedia.exceptions.DisambiguationError:
            self.output(f"Je n'ai pas trouvé de page nommée {term}, voulez-vous que je cherche sur Google?")
            result = self.reading()
            if result == "oui" or result == "je veux bien":
                pywhatkit.search(term)
                self.output("J'ai ouvert une page internet")
            else:
                self.output("D'accord")

    def wikiHowSearch(self,term):
        search_function = pywikihow.search_wikihow(term,1,'fr')
        reponse = unquote(search_function[0].summary)
        self.output(f"Je vais vous apprendre à {reponse}")


    def randomHowTo(self):
        reponse = unquote(pywikihow.RandomHowTo('fr').summary)
        self.output(f"Je vais vous apprendre à {reponse}")

    def youtubeDownload(self, term):
        dirMusic = "music\\Youtube"
        url = pywhatkit.playonyt(term,open_video=False)
        video = pytube.YouTube(str(url),on_progress_callback=on_progress).streams.get_audio_only()
        self.output("Début du téléchargement","Downloading...\n")
        file = video.download(dirMusic)
        base, reste = os.path.splitext(file)
        os.rename(file,base+'.mp3')
        self.output("La musique a été téléchargée dans ce dossier","\n Téléchargement terminé",overWrite = False)
        os.system(f"start {os.path.realpath(dirMusic)}")
        return file

    def speedTest(self):
        s = speedtest.Speedtest()
        self.output("J'effectue le test de connexion","Test en cours...")
        download_result = s.download()/1024**2
        upload_result = s.upload()/1024**2
        ping_result = s.results.ping
        
        self.output(f"Votre ping est de {ping_result:.1f} millisecondes".replace('.',','),f"Ping : {ping_result:.3f} ms",overWrite = False)
        self.output(f"Votre vitesse de téléchargement est de {download_result:.1f} mégabites par secondes".replace('.',','),f"Download Speed : {download_result:.2f} MBits/s",overWrite = False)
        self.output(f"Votre vitesse de téléversement est de {upload_result:.1f} mégabites par secondes".replace('.',','),f"Upload Speed : {upload_result:.2f} MBits/s",overWrite = False)


    def wolframAlphaEquationSolver(self,query):
        api_key = "E56J82-A232J3KT4G"
        requester = wolframalpha.Client(api_key)
        requested = requester.query(query)
        try :
            solutions = {}
            for i in range(len(requested['pod'])):
                if requested["pod"][i]["@title"] in intents["wolframalphaoutput"]:
                    if type(requested["pod"][i]['subpod'])==list:
                        solutions[f"{requested['pod'][i]['@title']}"] = [f"{requested['pod'][i]['subpod'][j]['plaintext']}" for j in range(len(requested["pod"][i]['subpod']))]
                    else:
                        solutions[f"{requested['pod'][i]['@title']}"]=f"{requested['pod'][i]['subpod']['plaintext']}"
            
            # reponses = [f"{translator.translate(elt,'fr').text} : {solutions[elt]}" for elt in solutions]
            reponses = [f"{elt} : {solutions[elt]}" for elt in solutions]

            if reponses == []:
                raise
            else: 
                self.speak("J'ai affiché les solutions")
                for elt in reponses:
                    self.write(elt,False)
                    
        except:
            self.output("Aucune réponse","Désolé, je n'ai rien trouvé")


    def breakAssistant(self):
        Assistant.stopSpeaking(self)
        Assistant.stopListening(self)
        self.output(rd.choice(bye[testTime()]),overWrite=True)
        sys.exit()

    def stopSpeaking(self):
        if pid.poll()==None:
            pid.kill()
    
    def stopListening(self):
        try:
            if pidListening.poll()==None:
                pidListening.kill()
        except:
            pass