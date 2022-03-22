import random



#los datos conocidos para que este pueda evaluar 



terminar_chat=[
    "terminar chat",
    "terminar",
    "es todo",
    "fin chat",
    "terminar conversacion",
    "fin de la converacion",
    "conversacion terminada",
    ]

confirmacion=[
    "si",
    "por favor",
    "favor"
    ]
ayuda=[
       "ayuda",
       "ayudame",
       "ayudarme"
       ]

negaciones=[
    "no",
    "desconozo",
    ]

saludos=[
    "hola",
    "buenos dias",
    "que tal",
    "buenas",
    ]


sin_opciones=[   #Este sirve especialmente cuando el usuario no sabe que preguntar
    "no",
    "se",
    "opciones",
    "jaque"
    
    ]


#Aqui terminan los datos amor 

#Valiables a usar -------------
#---------------------
terminar=False;#Esta es para terminar el chat

preg1=False;
preg2=False;
preg3=False;
preg4=False;
preg5=False;

#---------------------
#Aquí terminan las variables a usar -------------


print(" -----------------------------------------------")
print(" -----------------------------------------------")
print(" hola que tal, bienvenido a el chatbot sobre la creacion de juegos en unity ")
print(" -----------------------------------------------")
print(" -----------------------------------------------")
print(" ¿Cómo te llamas?")

texto = input();#Entrada de texto
minus = texto.lower();#Pasarl el texto a minusculas
nombre =texto;#guardar el nombre

print(" -----------------------------------------------")
print(" -----------------------------------------------")
print(" Genial ",nombre," , Buenos días, ¿Que te gustaría saber?")
#texto = str(texto);
#texts = texto.split();


#Aquí comineza el chatbot
while (terminar != True):
    teclado = input();
    teclado = teclado.lower();
    texts = teclado.split();
    longitud=len(texts);
    
    
    for n in range(longitud):
        #print(texts[n]);
        
        #para saber si no tiene opcines el man
        if(texts[n] in sin_opciones or texts[n] in ayuda or preg1):
            num = random.randint(0,2);
            if num ==0:
                print("Podrías intentar preguntando algo referente a la programacion en unity")
            if num ==1:
                print("¿Te gustaría saber por donde comenzar?");
                teclado = input();
                teclado = teclado.lower();
                texts = teclado.split();
                longitud=len(texts);
                
                for n in range(longitud):
                    if texts[n] in confirmacion :
                        print("     ")
                        print("bueno, primeramente saber programar, eso es una parte fundamental ",nombre,""
                              "Lo siguiente sería ser bueno programando, o tomarte el tiempo necesario para poder hacerlo",
                              ", no quiero que te ofendas ",nombre,",solo que si es importante, ya que necesitas un nivel intermedio,",
                              "Además de que sea dirigido a POO (Programación orientada a objetos), con esto ya estas del otro lado");
                        
                        print("¿Eres programador solitario? o ¿quieres programar solo?");
                        teclado = input();
                        teclado = teclado.lower();
                        texts = teclado.split();
                        longitud=len(texts);
                        for n in range(longitud):
                            if(texts[n] in confirmacion):
                                print("Bueno, entoces saber sobre hacer musica, diseñar y animar será algo que debrás aprender para hacelo, solo que tienes que aprender tambien como exportar dicha información a unity, no es complicado, en youtube encuentras mucha información sobre esto.");
                                
                            
                            else :
                                if (texts[n] in negaciones):
                                    print("Bueno, en tu equipo deberás tener algún diseñador, algún productor de melodías o musica, y un animador, igual si no eres programador, tendrás que contar con uno");
                
                    
                    else:
                        if(texts[n] == longitud):
                            print("Disculpa, no te he entendido ",nombre," mi programador me hizo con carencia de inteligenaia :(")
                           
                        
                
            if num==2:
                print("Yo soy un bot que te va a ayudar a saber algo referente a el entorno de unity, como lo es el diseño, la programación, o que necesitas saber si quieres utilizarlo")
            
            
            
    
    
    
    print("")


#Aqui termina el chat boot
print("ten un excelente día ",nombre,", hasta luego");
#texts = minus.split();
#evaluacion2 = False;
#print(texts);
 
#print(texts[0]);
#longitud=len(texts);

#for n in range(longitud):
    #print(texts[n]);
#    if(texts[n] in prueba):
#        evaluacion2 = True;
    
    
    
#if(evaluacion2 == True):
 #   print("Buenos días, ¿En que puedo ayudarte?");
    
    
    
    
#else:
 #   print("Perdon, no entiendo tu exprecion");
    #print(confirmacion)