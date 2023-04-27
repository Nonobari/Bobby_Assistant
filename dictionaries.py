from datetime import datetime

hi = {
    "journee": ["Bonjour !", "Bonjour, que puis-je faire pour vous ?","Que puis-je faire pour vous ?","Bonjour, comment puis-je vous aider ?"],
    "soir" : ["Bonsoir !", "Bonsoir, que puis-je faire pour vous ?","Que puis-je faire pour vous ?","Bonsoir, comment puis-je vous aider ?"],
    "nuit" : ["Bonsoir !", "Bonsoir, que puis-je faire pour vous ?","Que puis-je faire pour vous ?","Bonsoir, comment puis-je vous aider ?"]
}

bye = {
    "journee": ["Au revoir !", "À bientôt !", "À la prochaine !", "Bonne journée à vous !"],
    "soir": ["Au revoir !", "À bientôt !", "À la prochaine !", "Bonne soirée !"],
    "nuit": ["Au revoir !", "À bientôt !", "À la prochaine !", "Bonne nuit !"]
}

endDiscussion = ["C'était sympathique de discuter","J'ai apprécié cette discussion"]

intents = { 
            "alarm": ["mets une alarme à ", "reveil moi à ","réveil moi à ","reveil moi pour ","réveil moi pour ","mets une alarme pour ", "alarme pour ","reveil pour ","réveil pour ","reveil à ","réveil à ","alarme ","reveil ","réveil","minutes"],
            "break": ["stop","aurevoir","au revoir","break","à plus","à demain","ferme ta gueule"],
            "de rien" : ["Le plaisir est pour moi !", "À votre service !", "De rien"],
            "deezer": ["avec deezer","sur deezer","deezer"],
            "discuss" : ["discutons","discute","parle","conseil-moi","conseille-moi","conseil moi","conseille moi"],
            "pause" : ["pause","stop","break","ferme ta gueule",'chut','silence'],
            "calculator": ["combien font","calcule moi", "calcule","calcul","que vaut","combien fait","résoudre l'équation ", "résoudre l'équation ", "résouds l'équation ", "résout l'équation ", "résous l'équation ", "résouts l'équation ", "résoud l'équation ","résoudre ", "résouds ", "résout ", "résous ", "résouts ", "résoud ", "résoudre ", "resoudre ", "resouds ", "resout ", "resous ", "resouts ", "resoud ","solution de ","solutions de "],
            "lenghtcondition": ["phrase","phrases","quelques mots","quelques phrases"],
            "music": ["joue","fais moi écouter","musique"],
            "search": ["recherche","cherche","trouve moi","trouves moi","cherches"],
            "searchgoogle": ["recherche sur google","sur google"],
            "speedtest": ["speedtest", "speed test", "vitesse de connexion", "vitesse de téléchargement", "vitesse de telechargement", "vitesse internet"],
            "spotify": ["avec spotify","sur spotify","spotify"],
            "randomwikihow": ["apprends moi quelque chose", "apprends moi une nouvelle chose", "apprends moi de nouvelles choses", "découvre moi quelque chose","apprends moi une nouvelle compétence"],
            "resolve": ["résoudre l'équation ", "résoudre l'équation ", "résouds l'équation ", "résout l'équation ", "résous l'équation ", "résouts l'équation ", "résoud l'équation ","résoudre ", "résouds ", "résout ", "résous ", "résouts ", "résoud ", "résoudre ", "resoudre ", "resouds ", "resout ", "resous ", "resouts ", "resoud ","solution de ","solutions de "],
            "thanks" : ["merci","je te remercie","thanks"],
            "youtube": ["avec youtube","sur youtube","youtube"],
            "youtubedownloader":["telecharges ", "telecharge ", "télécharges ","télécharger ","télécharge ","telecharger "],
            "wikihow" : ["comment", "apprends moi à"],
            "wikipedia" : ["recherche sur wikipédia ","cherche sur wikipédia ","qui est ","qu'est-ce que c'est que ","qu'est-ce que","c'est quoi ","qu'est-ce qu'"],
            "wolframalphaoutput": ["Result","Results","Decimal form","Decimal forms","Exact result","Exact results","Complex solution","Complex solutions","Real solution","Real solutions","Solution","Solutions","General solution","General solutions","Numerical solution","Numerical solutions","Integer solution","Integer solutions","Definite integral","Definite integrals"]
            }

ignoredWords = ["speedtest"]


def testTime():
    """Retourne le moment de la journée (journee, soir, nuit)"""
    now = datetime.now()
    if now.hour >= 6 and now.hour < 18:
        return "journee"
    elif now.hour >= 18 and now.hour < 23:
        return "soir"
    else:
        return "nuit"