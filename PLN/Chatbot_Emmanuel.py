# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:03:00 2022

@author: ProBook
"""

import random

interrogativos=[
    "quién",
    "qué",
    "cuál",
    "cómo",
    "dónde",
    "cuándo",
    "cuánto",
    "por",
    "qué"
    ]

articlos_def_indef=[
    "el",
    "la",
    "los",
    "las",
    ######
    "un",
    "una",
    "unos",
    "unas"
    ]

preposiciones=[
    "a",
    "ante",
    "bajo",
    "cabe",
    "con",
    "contra",
    "de",
    "desde",
    "durante",
    "en",
    "entre",
    "hacia",
    "hasta",
    "mediante",
    "para",
    "por",
    "según",
    "sin",
    "so",
    "sobre",
    "tras",
    "versus",
    "vía"
    ]

complemento=[
    "unity",
    "programación",
    "diseño",
    "animación",
    "programar"
    ]

sujetos=[
    "ellos",
    "el",
    "ella",
    "yo"
     ]


verbos=[
        "ser",
        "estar",
        "poder",
        "estudiar",
        "aprender",
        "empezar",
        "comprender",
        "comenzar",
        "saber",
        "tener",
        "necesitar",
        ]


verbos_yo=[
    "soy",
    "puedo",
    "debo",
    "aprendo",
    "comprendo",
    "estudio",
    "empiezo",
    "soy",
    "necesito"
    ]

verbos_tercera=[
    "es",
    "eres",
    "puede",
    "aprender",
    "comprender",
    "estudiar",
    "necesitar"
    ]
print("\nBot: Hola que tal!, soy el bot para que puedas saber más sobre unity, ¿como te llamas?")
name = input("Yo: ");

nombre= ("Emmanuel");

print("\nBot: Que tal ",nombre,", ¿En que puedo ayudarte?")
salir =0


while (salir == 0):
    texto = input("Yo: ");
    #Econtramos los simbolos dentro del texto
    res = texto.find("¿");
    res1 = texto.find("?");
    #hacemos chico el texto y luego lo dividimos
    texto = texto.lower();
    texts = texto.split();





    if(res > -1 and res1 > -1):
        #Es una pregunta
        res = res+1;
        pregunta=texto[res:res1]
        pregunta=pregunta.split()
        longitud=len(pregunta);
        
        #print(pregunta);
        ###########################################################################################
        ###########################################################################################
        ###########################################################################################
        #Estas esttructuras son para presente simple------------------------------------------
        ###########################################################################################
        ###########################################################################################
        ###########################################################################################
        
        
        #Esta es una pregunta simple =====  interrogativo + verbo posesivo + verbo en infinitivo + preposicion + comlemento + preposicion + complemento
        #                                   ¿Qué necesito saber para programar en unity?
        if (pregunta[0] in interrogativos  and pregunta[1] in verbos_yo and pregunta[2] in verbos and pregunta[3] in preposiciones and pregunta[4] in complemento and pregunta[5] in preposiciones and pregunta[6] in complemento):
            print("8")
            
        
        
        
        
        #Esta es una pregunta simple =====  interrigativo + verbo posesivo + verbo infinitivo + preposicion + complemento
        #                                   ¿Qué puedo aprender en unity?
        elif(pregunta[0] in interrogativos  and pregunta[1] in verbos_yo and pregunta[2] in verbos and pregunta[3] in preposiciones and pregunta[4] in complemento):
            print("Es una pregunta chida")
        #Esta es una pregunta simple =====  interrigativo + verbo en tercera + complemento
        #                                   ¿Qué es unity?
        elif (pregunta[0] in interrogativos  and pregunta[1] in verbos_tercera and pregunta[2] in complemento):
            print("esta es la segunda")
          #Esta es una pregunta simple =====  interrigativo + verbo posesivo + preposicion + complemento
          #                                   ¿Qué aprendo en unity?
        elif (pregunta[0] in interrogativos  and pregunta[1] in verbos_yo and pregunta[2] in preposiciones and pregunta[3] in complemento):
            print("este es el 3o")
            
        #Esta es una pregunta simple =====  interrigativo + verbo posesivo + complemento
        #                                   ¿Dónde puedo programar?
        elif (pregunta[0] in interrogativos  and pregunta[1] in verbos_yo and pregunta[2] in complemento):
            print("este es el 4o")
            
            
        elif(longitud>5):
            
            #Esta es una pregunta simple =====  interrigativo + verbo tercera + articulos + compleneto + preposicion + complemento
            #                                   ¿Cómo es la programación en unity?
            
           
            if(pregunta[0] in interrogativos  and pregunta[1] in verbos_tercera and pregunta[2] in articlos_def_indef and pregunta[3] in complemento and pregunta[4] in preposiciones and pregunta[5] in complemento):
                print("6")
            
        
        
        #Esta es una pregunta simple =====  interrigativo + verbo tercera + articulos + preposicion + complemento
        #                                   ¿Qué es la programación?
        elif(pregunta[0] in interrogativos  and pregunta[1] in verbos_tercera and pregunta[2] in articlos_def_indef and pregunta[3] in complemento):
            print("7")
        
        
        #Esto es la respuesta si no esta bien la misma
        else:
            print("\nBot : No entidno tu lenguaje: ")
       
    else:
        if(res > -1 or res1 > -1):
            #Existe una pregunta pero no esta conclusa
            num = random.randint(0,3);
            if(num == 0):
                print("\nBot :Creo que estas haciendo una pregunta, pero le faltan los signos de interrogación");   
            if(num == 1):
                print("\nBot : Oh! vaya, creo has olvidado poder un signo de interrogación, no logro comprender lo que quieres preguntar")
            if(num == 2):
                print("\nBot : Hermano, carezco de inteligencia, no puedo comprender tu pregunta si no estan los dos simbolos de interrogación")
                
            if(num == 3):
                print("\nBot : A mi programador le hace hace falta dotarme de inteligencia sobre el lenguaje natural, por favor, podrías usar los '¿?', así podré comprenderte mejor")
                    
        
            
        else:
            #esta es una frase
            print("\nBot :Esta diciendo algo");
    
    


            
   


