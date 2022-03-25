# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:03:00 2022

@author: ProBook
"""

import random

off=[
    "salir",
    "apagar",
    ]

interrogativos=[
    "quién",
    "qué",
    "cuál",
    "cómo",
    "dónde",
    "cuándo",
    "cuánto",
    "por",
    ]

interro_nega=[
    "Quién",
    "Qué",
    "Cuál",
    "Cómo",
    "Dónde",
    "Cuándo",
    "Cuánto",
    "Por",
    ]

articlos_def_indef=[
    "el",
    "la",
    "los",
    "las",
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
    "tras",
    "versus",
    "vía"
    ]

complemento=[
    "unity",
    "programación",
    "diseño",
    "animación",
    "programar",
    "animar"
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
        "hacer",
        "programar" 
        ]
verbos_necesitar=[
    "tener",
    "saber",
    "necesitar",
    "comenzar",
    "hacer"  
    ]

verbos_estudiar=[
        "estudiar",
        "aprender",
        "empezar",
        "saber",
        "hacer",
        "aprender",
        "programar'"
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
    "necesito",
    "programo",
    ]

verbos_tercera=[
    "es",
    "eres",
    "puede",
    "aprende",
    "comprende",
    "estudia",
    "necesita"
    ]

verbos_puedo=[
        "puedo",
        "debo",
        "aprendo",
        "comprendo",
        "necesito",
        ]
print("\nBot: Hola que tal!, soy el bot para que puedas saber más sobre unity, ¿como te llamas?")
name = input("Yo: ");

nombre= str(name);

print("\nBot: Que tal ",nombre,", ¿En que puedo ayudarte?")
salir =0

pregunta_error=0;
res=0

error=False;
while (salir == 0):
    texto = input("Yo: ");
    salir1= texto;
    
    
    salir2=salir1.lower();
    salir3=salir2.split();
    
    
    
    texto_ques =texto;
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
        pregu=pregunta;
        
        texto_ques= texto_ques[res:res1];
        texto_ques= texto_ques.split();
        
        interro=pregunta.split();
        if(texto_ques[0] in interro_nega):
            
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
            
            
            if(longitud==7):
                #Esta es una pregunta simple =====  interrogativo + verbo posesivo + verbo en infinitivo + preposicion + comlemento + preposicion + complemento
                #                                   ¿Qué necesito saber para programar en unity?
                #                                   ¿Qué puedo estudiar para programar en unity?
                #                                   ¿Qué debo aprender para hacer una animación?
                
                
                #                                   ¿Qué puedo estudiar para programar en animación?
               
                
                
                if (pregunta[0] in interrogativos  and pregunta[1] in verbos_yo and pregunta[2] in verbos and pregunta[3] in preposiciones and pregunta[4] in complemento and pregunta[5] in preposiciones and pregunta[6] in complemento):
                    
                    #print(pregunta)
                    if(pregunta[0] == "qué" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar and pregunta[6] == "unity"):
                        print("\nBot: Puedes aprender divcersas cosas en unity, como programar, animar, diseñar, pero para ello debes tener un conocimiento básico o avanzado en programación si quieres que sea sencillo")
                        error=False;
                        
                    elif(pregunta[0] == "qué" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar  and pregunta[6] == "programación"):
                        print("\nBot: Puedes aprende diversas cosas en programación, es fundamental para la resolución de problemas, puedes hacer lo que tu quieras, todo lo que puedas imaginar")
                        error=False;
                        
                    elif(pregunta[0] == "qué" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar and pregunta[6] == "diseño"):
                        print("\nBot: Puedes aprender sobre el diseño, aunque muy basico, existen herramientas externas a unity para el diseño, por ello puedes buscar herramientas externas a ello")
                        error=False;
                    
                    elif(pregunta[0] == "qué" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar and pregunta[6] == "animación"):
                        print("\nBot: La animación puedes aprenderla aqui, para animar los personajes, por ello ")
                        error=False;
                    ###########################Que """""""""""""""""""""""
                    
                    
                    #                                   
                    #                                   .
                    #                                  
                    
                    
                    #                                  
                    
                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar and pregunta[6] == "unity"):
                        print("\nBot: En unity no puedes aprender a programar, aunque si puedes hacer algúnos ejercicios para acomplarte al programa, y para programar lo hace por medio de scripts, que estos son los que le dan vida al juego o al entorno mismo, pero programar requiere de saber sobre programación orientada a objetos")
                        error=False;
                        
                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar  and pregunta[6] == "programación"):
                        print("\nBot: Bueno, puedes aprender sobre aprender a programar, viendo videos o tomando un curso respecto a esto")
                        error=False;
                        
                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar and pregunta[6] == "diseño"):
                        print("\nBot: El diseño es un arte gráfico del cual , la única forma de aprenderlo es hacieno diseños o dibujos coloreados, es un proceso bonito y largo")
                        error=False;
                    
                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar and pregunta[6] == "animación"):
                        print("\nBot: La animación de puede hacer por Unity con su interfaz que ofrece, mediante frames, se puede hacer la animación más rapida o más lenta, eso lo aprender en videos en youtube o en la documentacion de unity")
                        error=False;
                    
                    ###########################Cómo """""""""""""""""""""""
                    
                    
                    #                                   
                    #                                   
                    #                                  
                    
                    
                    #   
                    
                    
                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar and pregunta[6] == "unity"):
                        print("\nBot: En unity no tiene un programa integrtado para programar, sin embargo al momento de instalar unity, te pide que intalse Visula Studio para poder programar, el mimso es muy intuitivo para unity")
                        error=False;
                        
                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar  and pregunta[6] == "programación"):
                        print("\nBot: La programación la puedes aprender en tutoriales o en cursos, aunque los lemguajes cambian, el razonamiento lógico y aprender un lenguaje es mas que suficiente para entender los demás lenguajes")
                        error=False;
                        
                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar and pregunta[6] == "diseño"):
                        print("\nBot: El diseño lo puedes aprender en programas externos a unity, ya que en unity es muy simple el que tiene unity, puedes aprender más en Youtube")
                        error=False;
                    
                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[2] in verbos_estudiar and pregunta[6] == "animación"):
                        print("\nBot: La animación la encuentras en una pestaña llamada 'animation', en donde tiene dos opciones para el diseño y otras para como va a mover la animación el script, puedes encontrar en la documentacion como puede animar y como hacerlo correctamente.")
                        error=False;
                        
                    ###########################Donde """""""""""""""""""""""
                   
                    else:
                        error=True;
                else:  
                      error=True;
                   
            else:
                if(longitud ==6):
                    #Esta es una pregunta simple =====  interrigativo + verbo tercera + articulos + compleneto + preposicion + complemento
                    #                                   ¿Cómo es la programación en unity?
                    
                   
                    if(pregunta[0] in interrogativos  and pregunta[1] in verbos_tercera and pregunta[2] in articlos_def_indef and pregunta[3] in complemento and pregunta[4] in preposiciones and pregunta[5] in complemento):
                        
                        
                        
                        if(pregunta[0] == "qué" and pregunta[1] in verbos_puedo  and pregunta[5] == "unity"):
                            print("\nBot: Puedes aprender divcersas cosas en unity, como programar, animar, diseñar, pero para ello debes tener un conocimiento básico o avanzado en programación si quieres que sea sencillo")
                            error=False;
                            
                        elif(pregunta[0] == "qué" and pregunta[1] in verbos_puedo and pregunta[5] == "programación"):
                            print("\nBot: Puedes aprende diversas cosas en programación, es fundamental para la resolución de problemas, puedes hacer lo que tu quieras, todo lo que puedas imaginar")
                            error=False;
                            
                        elif(pregunta[0] == "qué" and pregunta[1] in verbos_puedo and pregunta[5] == "diseño"):
                            print("\nBot: Puedes aprender sobre el diseño, aunque muy basico, existen herramientas externas a unity para el diseño, por ello puedes buscar herramientas externas a ello")
                            error=False;
                        
                        elif(pregunta[0] == "qué" and pregunta[1] in verbos_puedo and pregunta[5] == "animación"):
                            print("\nBot: La animación puedes aprenderla aqui, para animar los personajes, por ello ")
                            error=False;
                        ###########################Que """""""""""""""""""""""
                        
                        
                        #                                   
                        #                                   
                        #                                  
                        
                        
                        #                                  
                        
                        elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo and pregunta[5] == "unity"):
                            print("\nBot: En unity no puedes aprender a programar, aunque si puedes hacer algúnos ejercicios para acomplarte al programa, y para programar lo hace por medio de scripts, que estos son los que le dan vida al juego o al entorno mismo, pero programar requiere de saber sobre programación orientada a objetos")
                            error=False;
                            
                        elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo and pregunta[5] == "programación"):
                            print("\nBot: Bueno, puedes aprender sobre aprender a programar, viendo videos o tomando un curso respecto a esto")
                            error=False;
                            
                        elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo and pregunta[5] == "diseño"):
                            print("\nBot: El diseño es un arte gráfico del cual , la única forma de aprenderlo es hacieno diseños o dibujos coloreados, es un proceso bonito y largo")
                            error=False;
                        
                        elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo  and pregunta[5] == "animación"):
                            print("\nBot: La animación de puede hacer por Unity con su interfaz que ofrece, mediante frames, se puede hacer la animación más rapida o más lenta, eso lo aprender en videos en youtube o en la documentacion de unity")
                            error=False;
                        
                        ###########################Cómo """""""""""""""""""""""
                        
                        
                        #                                   
                        #                                   
                        #                                  
                        
                        
                        #   
                        
                        
                        elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[5] == "unity"):
                            print("\nBot: En unity no tiene un programa integrtado para programar, sin embargo al momento de instalar unity, te pide que intalse Visula Studio para poder programar, el mimso es muy intuitivo para unity")
                            error=False;
                            
                        elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[5] == "programación"):
                            print("\nBot: La programación la puedes aprender en tutoriales o en cursos, aunque los lemguajes cambian, el razonamiento lógico y aprender un lenguaje es mas que suficiente para entender los demás lenguajes")
                            error=False;
                            
                        elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[5] == "diseño"):
                            print("\nBot: El diseño lo puedes aprender en programas externos a unity, ya que en unity es muy simple el que tiene unity, puedes aprender más en Youtube")
                            error=False;
                        
                        elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[5] == "animación"):
                            print("\nBot: La animación la encuentras en una pestaña llamada 'animation', en donde tiene dos opciones para el diseño y otras para como va a mover la animación el script, puedes encontrar en la documentacion como puede animar y como hacerlo correctamente.")
                            error=False;
                            
                        ###########################Donde """""""""""""""""""""""
                       
                        else:
                            error=True;
                        
                        
                        
                        #print("6")
                        #res =6;
                        
                        #666666666666666666666666
                        
                        
                    else:
                        error=True;
                
                else:
                    if(longitud ==5):
                        #Esta es una pregunta simple =====  interrigativo + verbo posesivo + verbo infinitivo + preposicion + complemento
                        #                                   ¿Qué puedo aprender en unity?
                        #print(pregunta)
                        if(pregunta[0] in interrogativos  and pregunta[1] in verbos_yo and pregunta[2] in verbos and pregunta[3] in preposiciones and pregunta[4] in complemento):
                            ####################
                            #print(pregunta)
                            if(pregunta[0] == "qué" and pregunta[1] in verbos_puedo and pregunta[2] in verbos and pregunta[4] == "unity"):
                                print("\nBot: Puedes aprender divcersas cosas en unity, como programar, animar, diseñar, pero para ello debes tener un conocimiento básico o avanzado en programación si quieres que sea sencillo")
                                error=False;
                                
                            elif(pregunta[0] == "qué" and pregunta[1] in verbos_puedo and pregunta[2] in verbos  and pregunta[4] == "programación"):
                                print("\nBot: Puedes aprende diversas cosas en programación, es fundamental para la resolución de problemas, puedes hacer lo que tu quieras, todo lo que puedas imaginar")
                                error=False;
                                
                            elif(pregunta[0] == "qué" and pregunta[1] in verbos_puedo and pregunta[2] in verbos and pregunta[4] == "diseño"):
                                print("\nBot: Puedes aprender sobre el diseño, aunque muy basico, existen herramientas externas a unity para el diseño, por ello puedes buscar herramientas externas a ello")
                                error=False;
                            
                            elif(pregunta[0] == "qué" and pregunta[1] in verbos_puedo and pregunta[2] in verbos and pregunta[4] == "animación"):
                                print("\nBot: La animación puedes aprenderla aqui, para animar los personajes, por ello ")
                                error=False;
                            ###########################Que """""""""""""""""""""""
                            
                            
                            
                            elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo and pregunta[2] in verbos and pregunta[4] == "unity"):
                                print("\nBot: En unity no puedes aprender a programar, aunque si puedes hacer algúnos ejercicios para acomplarte al programa, y para programar lo hace por medio de scripts, que estos son los que le dan vida al juego o al entorno mismo, pero programar requiere de saber sobre programación orientada a objetos")
                                error=False;
                                
                            elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo and pregunta[2] in verbos and pregunta[4] == "programación"):
                                print("\nBot: Bueno, puedes aprender sobre aprender a programar, viendo videos o tomando un curso respecto a esto")
                                error=False;
                                
                            elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo and pregunta[2] in verbos and pregunta[4] == "diseño"):
                                print("\nBot: El diseño es un arte gráfico del cual , la única forma de aprenderlo es hacieno diseños o dibujos coloreados, es un proceso bonito y largo")
                                error=False;
                            
                            elif(pregunta[0] == "cómo" and pregunta[1] in verbos_puedo and pregunta[2] in verbos and pregunta[4] == "animación"):
                                print("\nBot: La animación de puede hacer por Unity con su interfaz que ofrece, mediante frames, se puede hacer la animación más rapida o más lenta, eso lo aprender en videos en youtube o en la documentacion de unity")
                                error=False;
                            
                            ###########################Cómo """""""""""""""""""""""
                            
                            
                            #                                   
                            #                                   
                            #                                  
                            
                            
                            #   
                            
                            
                            elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[2] in verbos and pregunta[4] == "unity"):
                                print("\nBot: En unity no tiene un programa integrtado para programar, sin embargo al momento de instalar unity, te pide que intalse Visula Studio para poder programar, el mimso es muy intuitivo para unity")
                                error=False;
                                
                            elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[2] in verbos and pregunta[4] == "programación"):
                                print("\nBot: La programación la puedes aprender en tutoriales o en cursos, aunque los lemguajes cambian, el razonamiento lógico y aprender un lenguaje es mas que suficiente para entender los demás lenguajes")
                                error=False;
                                
                            elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[2] in verbos and pregunta[4] == "diseño"):
                                print("\nBot: El diseño lo puedes aprender en programas externos a unity, ya que en unity es muy simple el que tiene unity, puedes aprender más en Youtube")
                                error=False;
                            
                            elif(pregunta[0] == "dónde" and pregunta[1] in verbos_puedo and pregunta[2] in verbos and pregunta[4] == "animación"):
                                print("\nBot: La animación la encuentras en una pestaña llamada 'animation', en donde tiene dos opciones para el diseño y otras para como va a mover la animación el script, puedes encontrar en la documentacion como puede animar y como hacerlo correctamente.")
                                error=False;
                                
                            ###########################Donde """""""""""""""""""""""
                            else:
                                error=True;
                            
                            
                            
                            
                            
                            
                            
                            
                            
                            
                        
                        #Esta es una pregunta simple =====  interrigativo + verbo tercera + articulos + complemento
                        #                                   ¿Qué es la programación?
                        
                        else:
                            error=True;
                        
                       
                    else:
                        if(longitud ==4):
                            #Esta es una pregunta simple =====  interrigativo + verbo posesivo + preposicion + complemento
                            #                                   ¿Qué aprendo en unity?
                          if (pregunta[0] in interrogativos  and pregunta[1] in verbos_yo and pregunta[2] in preposiciones and pregunta[3] in complemento):
                              #print("este es el 3o")
                              #res =4;
                              
                              #-----------------------------------------------------------------------------------
                              #-----------------------------------------------------------------------------------
                              #print(pregunta)
                              if(pregunta[0] == "qué" and pregunta[1] in verbos_yo and pregunta[3] == "unity"):
                                  print("\nBot: Puedes aprender divcersas cosas en unity, como programar, animar, diseñar, pero para ello debes tener un conocimiento básico o avanzado en programación si quieres que sea sencillo")
                                  error=False;
                                  
                              elif(pregunta[0] == "qué" and pregunta[1] in verbos_yo and pregunta[3] == "programación"):
                                  print("\nBot: Puedes aprende diversas cosas en programación, es fundamental para la resolución de problemas, puedes hacer lo que tu quieras, todo lo que puedas imaginar")
                                  error=False;
                                  
                              elif(pregunta[0] == "qué" and pregunta[1] in verbos_yo and pregunta[3] == "diseño"):
                                  print("\nBot: Puedes aprender sobre el diseño, aunque muy basico, existen herramientas externas a unity para el diseño, por ello puedes buscar herramientas externas a ello")
                                  error=False;
                              
                              elif(pregunta[0] == "qué" and pregunta[1] in verbos_yo and pregunta[3] == "animación"):
                                  print("\nBot: La animación puedes aprenderla aqui, para animar los personajes, por ello ")
                                  error=False;
                              ###########################Que """""""""""""""""""""""
                              
                              
                              
                              elif(pregunta[0] == "cómo" and pregunta[1] in verbos_yo and pregunta[3] == "unity"):
                                  print("\nBot: En unity no puedes aprender a programar, aunque si puedes hacer algúnos ejercicios para acomplarte al programa, y para programar lo hace por medio de scripts, que estos son los que le dan vida al juego o al entorno mismo, pero programar requiere de saber sobre programación orientada a objetos")
                                  error=False;
                                  
                              elif(pregunta[0] == "cómo" and pregunta[1] in verbos_yo and pregunta[3] == "programación"):
                                  print("\nBot: Bueno, puedes aprender sobre aprender a programar, viendo videos o tomando un curso respecto a esto")
                                  error=False;
                                  
                              elif(pregunta[0] == "cómo" and pregunta[1] in verbos_yo and pregunta[3] == "diseño"):
                                  print("\nBot: El diseño es un arte gráfico del cual , la única forma de aprenderlo es hacieno diseños o dibujos coloreados, es un proceso bonito y largo")
                                  error=False;
                              
                              elif(pregunta[0] == "cómo" and pregunta[1] in verbos_yo and pregunta[3] == "animación"):
                                  print("\nBot: La animación de puede hacer por Unity con su interfaz que ofrece, mediante frames, se puede hacer la animación más rapida o más lenta, eso lo aprender en videos en youtube o en la documentacion de unity")
                                  error=False;
                              
                              ###########################Cómo """""""""""""""""""""""
                              
                              
                              #                                   
                              #                                   
                              #                                  
                              
                              
                              #   
                              
                              
                              elif(pregunta[0] == "dónde" and pregunta[1] in verbos_yo and pregunta[3] == "unity"):
                                  print("\nBot: En unity no tiene un programa integrtado para programar, sin embargo al momento de instalar unity, te pide que intalse Visula Studio para poder programar, el mimso es muy intuitivo para unity")
                                  error=False;
                                  
                              elif(pregunta[0] == "dónde" and pregunta[1] in verbos_yo and pregunta[3] == "programación"):
                                  print("\nBot: La programación la puedes aprender en tutoriales o en cursos, aunque los lemguajes cambian, el razonamiento lógico y aprender un lenguaje es mas que suficiente para entender los demás lenguajes")
                                  error=False;
                                  
                              elif(pregunta[0] == "dónde" and pregunta[1] in verbos_yo and pregunta[3] == "diseño"):
                                  print("\nBot: El diseño lo puedes aprender en programas externos a unity, ya que en unity es muy simple el que tiene unity, puedes aprender más en Youtube")
                                  error=False;
                              
                              elif(pregunta[0] == "dónde" and pregunta[1] in verbos_yo and pregunta[3] == "animación"):
                                  print("\nBot: La animación la encuentras en una pestaña llamada 'animation', en donde tiene dos opciones para el diseño y otras para como va a mover la animación el script, puedes encontrar en la documentacion como puede animar y como hacerlo correctamente.")
                                  error=False;
                                  #----------------------------------------
                              
                          elif(pregunta[0] in interrogativos  and pregunta[1] in verbos_tercera and pregunta[2] in articlos_def_indef and pregunta[3] in complemento):
                              #-----------------------------------------------------------------------------------
                              #-----------------------------------------------------------------------------------
                              #print(pregunta)
                              if(pregunta[0] == "qué" and pregunta[1] in verbos_tercera and pregunta[3] == "unity"):
                                  print("\nBot: Puedes aprender divcersas cosas en unity, como programar, animar, diseñar, pero para ello debes tener un conocimiento básico o avanzado en programación si quieres que sea sencillo")
                                  error=False;
                                  
                              elif(pregunta[0] == "qué" and pregunta[1] in verbos_tercera and pregunta[3] == "programación"):
                                  print("\nBot: Puedes aprende diversas cosas en programación, es fundamental para la resolución de problemas, puedes hacer lo que tu quieras, todo lo que puedas imaginar")
                                  error=False;
                                  
                              elif(pregunta[0] == "qué" and pregunta[1] in verbos_tercera and pregunta[3] == "diseño"):
                                  print("\nBot: Puedes aprender sobre el diseño, aunque muy basico, existen herramientas externas a unity para el diseño, por ello puedes buscar herramientas externas a ello")
                                  error=False;
                              
                              elif(pregunta[0] == "qué" and pregunta[1] in verbos_tercera and pregunta[3] == "animación"):
                                  print("\nBot: La animación puedes aprenderla aqui, para animar los personajes, por ello ")
                                  error=False;
                              ###########################Que """""""""""""""""""""""
                              
                              
                              
                              elif(pregunta[0] == "cómo" and pregunta[1] in verbos_tercera and pregunta[3] == "unity"):
                                  print("\nBot: En unity no puedes aprender a programar, aunque si puedes hacer algúnos ejercicios para acomplarte al programa, y para programar lo hace por medio de scripts, que estos son los que le dan vida al juego o al entorno mismo, pero programar requiere de saber sobre programación orientada a objetos")
                                  error=False;
                                  
                              elif(pregunta[0] == "cómo" and pregunta[1] in verbos_tercera and pregunta[3] == "programación"):
                                  print("\nBot: Bueno, puedes aprender sobre aprender a programar, viendo videos o tomando un curso respecto a esto")
                                  error=False;
                                  
                              elif(pregunta[0] == "cómo" and pregunta[1] in verbos_tercera and pregunta[3] == "diseño"):
                                  print("\nBot: El diseño es un arte gráfico del cual , la única forma de aprenderlo es hacieno diseños o dibujos coloreados, es un proceso bonito y largo")
                                  error=False;
                              
                              elif(pregunta[0] == "cómo" and pregunta[1] in verbos_tercera and pregunta[3] == "animación"):
                                  print("\nBot: La animación de puede hacer por Unity con su interfaz que ofrece, mediante frames, se puede hacer la animación más rapida o más lenta, eso lo aprender en videos en youtube o en la documentacion de unity")
                                  error=False;
                              
                              ###########################Cómo """""""""""""""""""""""
                              
                              
                              #                                   
                              #                                   
                              #                                  
                              
                              
                              #   
                              
                              
                              elif(pregunta[0] == "dónde" and pregunta[1] in verbos_tercera and pregunta[3] == "unity"):
                                  print("\nBot: En unity no tiene un programa integrtado para programar, sin embargo al momento de instalar unity, te pide que intalse Visula Studio para poder programar, el mimso es muy intuitivo para unity")
                                  error=False;
                                  
                              elif(pregunta[0] == "dónde" and pregunta[1] in verbos_tercera and pregunta[3] == "programación"):
                                  print("\nBot: La programación la puedes aprender en tutoriales o en cursos, aunque los lemguajes cambian, el razonamiento lógico y aprender un lenguaje es mas que suficiente para entender los demás lenguajes")
                                  error=False;
                                  
                              elif(pregunta[0] == "dónde" and pregunta[1] in verbos_tercera and pregunta[3] == "diseño"):
                                  print("\nBot: El diseño lo puedes aprender en programas externos a unity, ya que en unity es muy simple el que tiene unity, puedes aprender más en Youtube")
                                  error=False;
                              
                              elif(pregunta[0] == "dónde" and pregunta[1] in verbos_tercera and pregunta[3] == "animación"):
                                  print("\nBot: La animación la encuentras en una pestaña llamada 'animation', en donde tiene dos opciones para el diseño y otras para como va a mover la animación el script, puedes encontrar en la documentacion como puede animar y como hacerlo correctamente.")
                                  error=False;
                                  
                              ###########################Donde """""""""""""""""""""""
                              else:
                                  error=True;
                              
                              
                              
                              #777777777777777777777777777777
                              
                          else:
                              error=True;
                              #44444444444444444444444444
                              
                             
                        else:
                            if(longitud ==3):
                                #Esta es una pregunta simple =====  interrigativo + verbo en tercera + complemento
                                #                                   ¿Qué es unity?
                                if (pregunta[0] in interrogativos  and pregunta[1] in verbos_tercera and pregunta[2] in complemento):
                                    
                                    #print("esta es la segunda")
                                    #salir=1;
                                    
                                    #res =3;
                                    #333333333333333333333333
                                    
                                    
                                    #-----------------------------------------------------------------------------------
                                    #-----------------------------------------------------------------------------------
                                    #print(pregunta)
                                    if(pregunta[0] == "qué" and pregunta[1] in verbos_tercera and pregunta[2] == "unity"):
                                        print("\nBot: Puedes aprender divcersas cosas en unity, como programar, animar, diseñar, pero para ello debes tener un conocimiento básico o avanzado en programación si quieres que sea sencillo")
                                        error=False;
                                        
                                    elif(pregunta[0] == "qué" and pregunta[1] in verbos_tercera and pregunta[2] == "programación"):
                                        print("\nBot: Puedes aprende diversas cosas en programación, es fundamental para la resolución de problemas, puedes hacer lo que tu quieras, todo lo que puedas imaginar")
                                        error=False;
                                        
                                    elif(pregunta[0] == "qué" and pregunta[1] in verbos_tercera and pregunta[2] == "diseño"):
                                        print("\nBot: Puedes aprender sobre el diseño, aunque muy basico, existen herramientas externas a unity para el diseño, por ello puedes buscar herramientas externas a ello")
                                        error=False;
                                    
                                    elif(pregunta[0] == "qué" and pregunta[1] in verbos_tercera and pregunta[2] == "animación"):
                                        print("\nBot: La animación puedes aprenderla aqui, para animar los personajes, por ello ")
                                        error=False;
                                    ###########################Que """""""""""""""""""""""
                                    
                                    
                                    
                                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_tercera and pregunta[2] == "unity"):
                                        print("\nBot: En unity no puedes aprender a programar, aunque si puedes hacer algúnos ejercicios para acomplarte al programa, y para programar lo hace por medio de scripts, que estos son los que le dan vida al juego o al entorno mismo, pero programar requiere de saber sobre programación orientada a objetos")
                                        error=False;
                                        
                                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_tercera and pregunta[2] == "programación"):
                                        print("\nBot: Bueno, puedes aprender sobre aprender a programar, viendo videos o tomando un curso respecto a esto")
                                        error=False;
                                        
                                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_tercera and pregunta[2] == "diseño"):
                                        print("\nBot: El diseño es un arte gráfico del cual , la única forma de aprenderlo es hacieno diseños o dibujos coloreados, es un proceso bonito y largo")
                                        error=False;
                                    
                                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_tercera and pregunta[2] == "animación"):
                                        print("\nBot: La animación de puede hacer por Unity con su interfaz que ofrece, mediante frames, se puede hacer la animación más rapida o más lenta, eso lo aprender en videos en youtube o en la documentacion de unity")
                                        error=False;
                                    
                                    ###########################Cómo """""""""""""""""""""""
                                    
                                    
                                    #                                   
                                    #                                   
                                    #                                  
                                    
                                    
                                    #   
                                    
                                    
                                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_tercera and pregunta[2] == "unity"):
                                        print("\nBot: En unity no tiene un programa integrtado para programar, sin embargo al momento de instalar unity, te pide que intalse Visula Studio para poder programar, el mimso es muy intuitivo para unity")
                                        error=False;
                                        
                                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_tercera and pregunta[2] == "programación"):
                                        print("\nBot: La programación la puedes aprender en tutoriales o en cursos, aunque los lemguajes cambian, el razonamiento lógico y aprender un lenguaje es mas que suficiente para entender los demás lenguajes")
                                        error=False;
                                        
                                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_tercera and pregunta[3] == "diseño"):
                                        print("\nBot: El diseño lo puedes aprender en programas externos a unity, ya que en unity es muy simple el que tiene unity, puedes aprender más en Youtube")
                                        error=False;
                                    
                                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_tercera and pregunta[2] == "animación"):
                                        print("\nBot: La animación la encuentras en una pestaña llamada 'animation', en donde tiene dos opciones para el diseño y otras para como va a mover la animación el script, puedes encontrar en la documentacion como puede animar y como hacerlo correctamente.")
                                        error=False;
                                        
                                    ###########################Donde """""""""""""""""""""""
                                 
                                    
                                    
                                #Esta es una pregunta simple =====  interrigativo + verbo posesivo + complemento
                                #                                   ¿Dónde puedo programar?
                                elif (pregunta[0] in interrogativos  and pregunta[1] in verbos_yo and pregunta[2] in complemento):
                                    #print("este es el 4o")
                                    
                                    #res =5;
                                    
                                    #5555555555555555555555555
                                    
                                    #-----------------------------------------------------------------------------------
                                    #-----------------------------------------------------------------------------------
                                    #print(pregunta)
                                    if(pregunta[0] == "qué" and pregunta[1] in verbos_yo and pregunta[2] == "unity"):
                                        print("\nBot: Puedes aprender divcersas cosas en unity, como programar, animar, diseñar, pero para ello debes tener un conocimiento básico o avanzado en programación si quieres que sea sencillo")
                                        error=False;
                                        
                                    elif(pregunta[0] == "qué" and pregunta[1] in verbos_yo and pregunta[2] == "programar"):
                                        print("\nBot: Puedes aprende diversas cosas en programación, es fundamental para la resolución de problemas, puedes hacer lo que tu quieras, todo lo que puedas imaginar")
                                        error=False;
                                        
                                    elif(pregunta[0] == "qué" and pregunta[1] in verbos_yo and pregunta[2] == "diseñar"):
                                        print("\nBot: Puedes aprender sobre el diseño, aunque muy basico, existen herramientas externas a unity para el diseño, por ello puedes buscar herramientas externas a ello")
                                        error=False;
                                    
                                    elif(pregunta[0] == "qué" and pregunta[1] in verbos_yo and pregunta[2] == "animar"):
                                        print("\nBot: La animación puedes aprenderla aqui, para animar los personajes, por ello ")
                                        error=False;
                                    ###########################Que """""""""""""""""""""""
                                    
                                    
                                    
                                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_yo and pregunta[2] == "unity"):
                                        print("\nBot: En unity no puedes aprender a programar, aunque si puedes hacer algúnos ejercicios para acomplarte al programa, y para programar lo hace por medio de scripts, que estos son los que le dan vida al juego o al entorno mismo, pero programar requiere de saber sobre programación orientada a objetos")
                                        error=False;
                                        
                                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_yo and pregunta[2] == "programar"):
                                        print("\nBot: Bueno, puedes aprender sobre aprender a programar, viendo videos o tomando un curso respecto a esto")
                                        error=False;
                                        
                                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_yo and pregunta[2] == "diseñar"):
                                        print("\nBot: El diseño es un arte gráfico del cual , la única forma de aprenderlo es hacieno diseños o dibujos coloreados, es un proceso bonito y largo")
                                        error=False;
                                    
                                    elif(pregunta[0] == "cómo" and pregunta[1] in verbos_yo and pregunta[2] == "animar"):
                                        print("\nBot: La animación de puede hacer por Unity con su interfaz que ofrece, mediante frames, se puede hacer la animación más rapida o más lenta, eso lo aprender en videos en youtube o en la documentacion de unity")
                                        error=False;
                                    
                                    ###########################Cómo """""""""""""""""""""""
                                    
                                    
                                    #                                   
                                    #                                   
                                    #                                  
                                    
                                    
                                    #   
                                    
                                    
                                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_yo and pregunta[2] == "unity"):
                                        print("\nBot: En unity no tiene un programa integrtado para programar, sin embargo al momento de instalar unity, te pide que intalse Visula Studio para poder programar, el mimso es muy intuitivo para unity")
                                        error=False;
                                        
                                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_yo and pregunta[2] == "programar"):
                                        print("\nBot: La programación la puedes aprender en tutoriales o en cursos, aunque los lemguajes cambian, el razonamiento lógico y aprender un lenguaje es mas que suficiente para entender los demás lenguajes")
                                        error=False;
                                        
                                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_yo and pregunta[3] == "diseñar"):
                                        print("\nBot: El diseño lo puedes aprender en programas externos a unity, ya que en unity es muy simple el que tiene unity, puedes aprender más en Youtube")
                                        error=False;
                                    
                                    elif(pregunta[0] == "dónde" and pregunta[1] in verbos_yo and pregunta[2] == "animar"):
                                        print("\nBot: La animación la encuentras en una pestaña llamada 'animation', en donde tiene dos opciones para el diseño y otras para como va a mover la animación el script, puedes encontrar en la documentacion como puede animar y como hacerlo correctamente.")
                                        error=False;
                                    
                                    
                                    else: 
                                        error = True;
                                    ###########################Donde """""""""""""""""""""""
                                 
                                    
                                    
                                    
                                    
                                else:
                                    error=True;
                                     
                                  
                                    
                                    
                                 
                            else:
                                print("\nBot : No entiendo tu lenguaje ")
                                    
                                    
                                
            if(error==True):
                
                print("\nBot : No entiendo tu lenguaje ");
           
        else:
             print("Tienes errores grmaticales en como el acento o La mayuscula")
                            
                            
                
        
        
        
       
        
       
        
       
            
        
           
            
           
            
        
    
        
        #---------------------------------------------------------------
        #---------------Aqui se comienza a evaluar----------------------
        #---------------------------------------------------------------
       
      
   
        
        
       
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
            logi=len(salir3);
            
            for n in range(logi):
                if (salir3[n] in off):
                    salir=1;
                    
                    print("\nBot :Hasta luego, espero poder haberte ayudado ");
                else:
                    #print(salir3)
                    #print(off)
                    print("\nBot :Las frases aún no las puedo procesar :(, solo entiendo preguntas simples");
                     
            
                
           
                
           
    
    


         
