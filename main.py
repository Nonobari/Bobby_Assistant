from assistantClass import Assistant
from core import *
bobby = Assistant("Bobby", 20)


if __name__== "__main__":
    while True:
        query = bobby.reading(correction=False)
        mainLoop(bobby,query)
    
