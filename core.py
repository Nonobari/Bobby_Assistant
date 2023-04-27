from assistantClass import Assistant
from dictionaries import *
import random as rd

def truncateWords(query,intent):
    for word in intents[intent]:
        query=query.replace(word,"")
        query = query.strip('?').strip('.').strip('!').strip(' ')
    return query

    
def mainLoop(assistant:Assistant ,query:str):
    if query == None:
        return
    #YoutubeMusicPlayer
    elif any(word in query for word in intents["music"]) and any(word in query for word in intents["youtube"]):
            query = truncateWords(query,"music")
            query = truncateWords(query,"youtube")
            assistant.youtubeSearch(query)
    #SpotifyMusicPlayer
    elif any(word in query for word in intents["music"]) and any(word in query for word in intents["spotify"]):
            query = truncateWords(query,"music")
            query = truncateWords(query,"spotify")
            assistant.spotifySearch(query)
    #DeezerMusicPlayer
    elif any(word in query for word in intents["music"]) and any(word in query for word in intents["deezer"]):
            query = truncateWords(query,"music")
            query = truncateWords(query,"deezer")
            assistant.deezerSearch(query)

    #MusicPlayer
    elif any(word in query for word in intents["music"]):
        query = truncateWords(query,"music")
        assistant.musicPlayer(query)

    #Recherche sur wikipédia
    elif any(word in query for word in intents["wikipedia"]):
        lenght = 1
        query = truncateWords(query,"wikipedia")
        if any(word in query for word in intents["lenghtcondition"]):
            
            if 'en deux phrases' in query:
                lenght = 2
                query = query.replace('en deux phrases' ,"")
            if 'en trois phrases' in query:
                lenght = 3
                query = query.replace('en trois phrases' ,"")
        assistant.wikiSearch(query,lenght)
    

    # Recherche sur wikihow
    elif any(word in query for word in intents["wikihow"]):
        query = truncateWords(query,'wikihow')
        assistant.wikiHowSearch(query)

    #Recherche aléatoire Wikihow
    elif any(word in query for word in intents["randomwikihow"]):
        query = truncateWords(query,'randomwikihow')
        assistant.randomHowTo()

    #Alarme
    # elif any(word in query for word in intents["alarm"]):
    #     pid = subprocess.Popen([sys.executable, "alarm.py"],creationflags=subprocess.CREATE_NEW_CONSOLE) # Call subprocess
    
    #YoutubeDownloader
    elif any(word in query for word in intents["youtubedownloader"]):
        query = truncateWords(query, 'youtubedownloader')
        assistant.youtubeDownload(query)

    #Speedtest
    elif any(word in query for word in intents["speedtest"]):
        query = truncateWords(query, 'speedtest')
        assistant.speedTest()

    #Calculator WolframAlpha
    elif any(word in query for word in intents["calculator"]):
        query = truncateWords(query,'calculator')
        assistant.wolframAlphaEquationSolver(query)

    #Thanks
    elif any(word in query for word in intents["thanks"]):
        assistant.stopSpeaking()
        assistant.output(rd.choice(intents["de rien"]))
        
    #Arrêt de l'assistant
    elif any(word in query for word in intents["break"]):
        assistant.breakAssistant()

    #Silence
    elif any(word in query for word in intents["pause"]):
        assistant.stopSpeaking()

