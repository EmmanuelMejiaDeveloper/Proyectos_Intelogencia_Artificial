# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:49:37 2022

@author: armma
"""

from nltk.chat.util import  Chat, reflections

refleciones = {
    "ir":"fui",
    "hola":"hey!"
    
    
    }
pares = [
    
    
        [
            r"mi nombre es (.*)",
            ["Hola %1, como estas?",]
            
        ],
        [
            r"(.*) una red ipv4?",
            ["Si , son reedees con un protocolo ",]
            
        ],
    
    ]
def chatear():
    print("Hola")
    chat= Chat(pares,refleciones)
    chat.converse()

if __name__ == "__main__":
    chatear()
chatear()