# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 08:51:23 2022

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
            r"(.*) mi nombre es (.*)",
            ["Hola %2¿, como estas?",]
            
        ],
        [
            r"(.*) como estas?",
            ["\nbot: estoy bien, no me quejo, ¿En que puedo ayudarte?",]
            
        ],
        [
            r"(.*) que tal?",
            ["\nbot: estoy bien, no me quejo, ¿En que puedo ayudarte?",]
            
        ],
        [
            r"(.*) bien",
            ["\nbot: Genial!, ¿En que puedo ayudarte?",]
            
        ],
        [
            r" bien, (.*)",
            ["\nbot: Genial!, ¿En que puedo ayudarte?",]
            
        ],
        
        [
            r"¿(.*) ip a binario?",
            ["\nbot: Np es complicado pasar una ip a binario, primeramrente tenemos que una ip son 32 bits, y en redes ipv4 se dividen en 4 partes, entonces tendríamos 4 octetos, se verían así, 11111111.11111111.11111111.11111111, ahí son 32 bits y separados en 4 octetos por un punto, ahora tomando un octeto ahora tendríamos que cada uno tiene un valor independiente, del cual SIEMPRE SE LEE DE DERECHA A IZQUIERDA, empezando por derecha tenemos 1=1, el siguiente sería 1=2, luego 1=4, luego = 1=8,luego 1=16,luego 1=32,luego 1=64,luego 1=128, ya viendolo mejor tendríamos el siguiente, 11111111=> 1=128 1=64 1=32 1=16 1=8 1=4 1=2 1=1, una vez que ya tengas esto solo es cosa de ver cuales podemos encender para posterior sumarlos como normalmente se suma, hasta encontrar el valor indicado que hace alucion al número que tenemos, Un EJEMPLO sería el siguiente: tenemos 175.32.4.6 , bueno tomamos el primer octecto que hay, que es 175, ahora sebemos encender ciertos binarios de ese octeto para que nos dé '175', recordemos que tenemos los valores de cada binario que son 1=128 1=64 1=32 1=16 1=8 1=4 1=2 1=1,ahora haciendo una primera prueba, quiero ocupar estos bianrios, y se verían así,  11000000 => 1=128 1=64 1=0 1=0 1=0 1=0 1=0 1=0, así se vería, como estan apagados los demás, se les da un valor a cero ahora sumandolo tendríamos el siguiente valor 128+64+0+0+0+0+0+0=192, no tenemos el número esperado, entonces tenemos que apagar uno porque ya nos pasamos y entoces tendremos que encender otro encedieramos uno más, 10100000 => 1=128 1=0 1=32 1=0 1=0 1=0 1=0 1=0, entonce si lo sumamos quedaría así , 128+0+32+0+0+0+0+0=160, ya tenemos un número menor, ahora nos hace falta 15 para llegar a 175, así que tenemos que encender unos más para llegar a 175,entonces encendemos unos más 10101000=>1=128 1=0 1=32 1=0 1=8 1=0 1=0 1=0, y teniendo la suma, tendríamos algo así, 128+0+32+0+8+0+0+0 = 168, entonces volvemos a activar unos bianrios más (los que consideres),10101110 => 1=128 1=0 1=32 1=0 1=8 1=4 1=2 1=0, ahora tendríamos una suma como esta, 128+0+32+0+8+4+2+0 = 174, bueno, ahora solo nos hace falta un 1 para llegar a 175, entonce encenderíamo uno último, 10101111 => 1=128 1=0 1=32 1=0 1=8 1=4 1=2 1=1, ahora tendríamos una suma como esta, 128+0+32+0+8+4+2+1 = 171, así tendríamos el primer número en binario del primer octecto, solo restaría hacer los sigiuentes 3, es algo sencillo, mientras más lo hagas, será mas facil para ti calcularlo",]
            
        ],
        [
            r"¿(.*) ipv4 a binario?",
            ["\nbot: Genial!, ¿En que puedo ayudarte?",]
            
        ],
        [
            r"¿(.*)es una red ipv4?",
            ["\nbot : 'Este es el Protocolo de Internet versión 4 (en inglés, Internet Protocol version 4, IPv4) es la cuarta versión del Internet Protocol (IP), un protocolo de interconexión de redes basados en Internet, y que fue la primera versión implementada en 1983 para la producción de ARPANET. Definida en el RFC 791, el IPv4 usa direcciones de 32 bits, limitadas a {\displaystyle 2^{32}}2^{{32}} = 4 294 967 296 direcciones únicas, muchas de ellas LAN.1​ Por el crecimiento enorme que ha tenido la seguridad electrónica y la automatización, combinado con el hecho de que hay desperdicio de direcciones en muchos casos (consultar las secciones que siguen), ya hace varios años se observó que escaseaban las direcciones IPv4.' ",]
            
        ],
        [
            r"¿(.*)protocolo ipv4?",
            ["\nbot : 'Este es el Protocolo de Internet versión 4 (en inglés, Internet Protocol version 4, IPv4) es la cuarta versión del Internet Protocol (IP), un protocolo de interconexión de redes basados en Internet, y que fue la primera versión implementada en 1983 para la producción de ARPANET. Definida en el RFC 791, el IPv4 usa direcciones de 32 bits, limitadas a {\displaystyle 2^{32}}2^{{32}} = 4 294 967 296 direcciones únicas, muchas de ellas LAN.1​ Por el crecimiento enorme que ha tenido la seguridad electrónica y la automatización, combinado con el hecho de que hay desperdicio de direcciones en muchos casos (consultar las secciones que siguen), ya hace varios años se observó que escaseaban las direcciones IPv4.' ",]
            
        ],
        [
            r"¿(.*) calcular una red ipv4?",
            ["\nbot : Relamente calcular un red ipv4, no existe tal acción, lo que se puede saber es como calcular la mascara de subred, la wildcard, una dirección de subred, como pasar una ip a binario y pasar una ip binaria a notación punteada",]
            
        ],
        [
            r"¿(.*) calcular (.*) ipv4?",
            ["\nbot : Relamente calcular un red ipv4, no existe tal acción, lo que se puede saber es como calcular la mascara de subred, la wildcard, una dirección de red, como pasar una ip a binario y pasar una ip binaria a notación punteada",]
            
        ],
        [
            r"¿(.*) es una red?",
            ["\nbot : Es un conjunto de equipos conectados por medio de cables, señales, ondas o cualquier otro método de transporte de datos",]
            
        ],
        [
            r"¿(.*) utilizan (.*) ipv4?",
            ["\nbot : Se ocuapn en todos lados, ahora es el protocolo ipv4 con el ipv6, en tu telefono cuando ves las configuraciones avanzadas de la red, se te asigna una ipv4 y una ipv6 para poder conectarte",]
            
        ],
        [
            r"¿(.*) utilizan (.*) redes",
            ["\nbot : Se ocuapn en todos lados, ahora es el protocolo ipv4 con el ipv6, en tu telefono cuando ves las configuraciones avanzadas de la red, se te asigna una ipv4 y una ipv6 para poder conectarte",]
            
        ],
        [
            r"¿(.*) aplicar (.*) ipv4?",
            ["\nbot : Se ocuapn en todos lados, ahora es el protocolo ipv4 con el ipv6, en tu telefono cuando ves las configuraciones avanzadas de la red, se te asigna una ipv4 y una ipv6 para poder conectarte",]
            
        ],
        [
            r"¿(.*) son las redes?",
            ["\nbot : Son un conjunto de equipos conectados por medio de cables, señales, ondas o cualquier otro método de transporte de datos",]
            
        ],
        [
            r"¿(.*) las redes?",
            ["\nbot : Son un conjunto de equipos conectados por medio de cables, señales, ondas o cualquier otro método de transporte de datos",]
            
        ],
        [
            r"¿(.*) características de una red?",
            ["\nbot : Las red tiene características importantes de las cuales son: 1.Velocidad, 2.-Seguridad, 3.-Confiabilidad, 4.-Escabilidad, 5.-Dsiponibilidad",]
            
        ],
        [
            r"¿(.*) características (.*) de una red?",
            ["\nbot : Las red tiene características importantes de las cuales son: 1.Velocidad, 2.-Seguridad, 3.-Confiabilidad, 4.-Escabilidad, 5.-Dsiponibilidad",]
            
        ],
        [
            r"¿(.*) velocidad de (.*) red?",
            ["\nbot : Es la velocidad a la que se transmiten los datos por segundo a través de la red. Suelen medirse con un test de velocidad. La rapidez de subida y descarga de datos será diferente según los estándares que utilicemos y también según el tipo de red o medio a través del que se transmiten los datos (inalámbrica, fibra óptica, cables de teléfono o coaxial), existen dos protocolos para las redes el ipv4 e ipv6.",]
            
        ],
        [
            r"¿(.*) velocidad de red?",
            ["\nbot : Es la velocidad a la que se transmiten los datos por segundo a través de la red. Suelen medirse con un test de velocidad. La rapidez de subida y descarga de datos será diferente según los estándares que utilicemos y también según el tipo de red o medio a través del que se transmiten los datos (inalámbrica, fibra óptica, cables de teléfono o coaxial), existen dos protocolos para las redes el ipv4 e ipv6.",]
            
        ],
        [
            r"¿(.*) segudirdad de red?",
            ["\nbot : Es uno de los aspectos más peligrosos que rodean a las redes inalámbricas, como ya hablamos en otra ocasión. La aparición de intrusos que nos quitan ancho de banda es una de las razones que convierte estas redes en bastante más vulnerables.Por otro lado, las redes cableadas pueden sufrir interferencias como consecuencia del uso de otros aparatos como el microondas. A diferencia de estas, la fibra óptica es la que ofrece una mayor seguridad.",]
            
        ],
        [
            r"¿(.*) confiabilidad de red?",
            ["\nbot : Mide el grado de probabilidades que existe de que uno de los nodos de la red se averíe y por tanto se produzcan fallos. En parte dependerá de la topología de la red que hallamos instalado y del lugar que ocupa el componente averiado. Cuando uno de los componentes no funciona, puede afectar al funcionamiento de toda la red o por el contrario constituir un problema local.",]
            
        ],
        [
            r"¿(.*) escabilidad de red?",
            ["\nbot : Una red no puede añadir nuevos componentes de forma continua y esperar que funcione a la misma velocidad. A medida que añadimos nuevos nodos y estos se hallan funcionando a la vez, la conexión a Internet se reduce, la velocidad de transmisión de datos en general es menor y hay más probabilidad de errores.",]
            
        ],
        [
            r"¿(.*) disponibilidad de red?",
            ["\nbot : Es la capacidad que posee una red para hallarse disponible y completamente activa cuando la necesitamos. Hablamos de la cantidad de tiempo posible en que podemos someter los nodos a unas condiciones de rendimiento necesarias en nuestra empresa. El objetivo es conseguir que la red se halle disponible según las necesidades de uso para las que se ha instalado.",]
            
        ],
        [
            r"¿(.*) es (.*) dirección ip?",
            ["\nbot : Una dirección IP es un número de identificación lógico de un equipo en la red, o de una red o subred. Las direcciones IPv4 tienen 32 bits(del cual pasandolo de forma binaria, se vería de esta manera 11111111.11111111.11111111.11111111) en formato decimal separado por puntos, esta a su vez se dividen en 8 bits",]
            
        ],
        [
            r"¿(.*) calcular (.*) máscara de subred?",
            ["\nbot : Para calcular una mascara de sub red, es algo sencillo, sabiendo la clase y los bits que pertenecen a red, solo sería cosa de convertir los binarios a notacion decimal punteada, ejemplo : Tenemos 192.168.24.2/24, ahora lo pasamos a binario el número de bits de red, 11111111.11111111.11111111.00000000 y quedaría de esta manera, ya solo sería pasarlo a notacion decimal punteada, y quedaría así, 255.255.255.0",]
            
        ],
        [
            r"¿(.*) calcular (.*) submascara de red?",
            ["\nbot : Para calcular una mascara de sub red, es algo sencillo, sabiendo la clase y los bits que pertenecen a red, solo sería cosa de convertir los binarios a notacion decimal punteada, ejemplo : Tenemos 192.168.24.2/24, ahora lo pasamos a binario el número de bits de red, 11111111.11111111.11111111.00000000 y quedaría de esta manera, ya solo sería pasarlo a notacion decimal punteada, y quedaría así, 255.255.255.0",]
            
        ],
        [
            r"¿(.*) son (.*) subredes?",
            ["\nbot : Las subredes son un método para maximizar el espacio de direcciones IPv4 de 32 bits y reducir el tamaño de las tablas de enrutamiento en una interred mayor. En cualquier clase de dirección, las subredes proporcionan un medio de asignar parte del espacio de la dirección host a las direcciones de red, lo cual permite tener más redes.",]
            
        ],
        [
            r"¿(.*) subredes?",
            ["\nbot : Las subredes son un método para maximizar el espacio de direcciones IPv4 de 32 bits y reducir el tamaño de las tablas de enrutamiento en una interred mayor. En cualquier clase de dirección, las subredes proporcionan un medio de asignar parte del espacio de la dirección host a las direcciones de red, lo cual permite tener más redes.",]
            
        ],
        [
            r"¿(.*) tablas de enrutamiento?",
            ["\nbot : Una tabla de enrutamiento es un conjunto de reglas que sirven para determinar qué camino deben seguir los paquetes de datos. Todo esto a través de toda red que trabaje con el protocolo IP.",]
            
        ],
        [
            r"¿(.*) son (.*) host?",
            ["\nbot : Un host es cualquier computadora o máquina conectada a una red a través de un dominio y un número de IP definidos. Su función es proporcionarle recursos, información y servicios a los usuarios.",]
            
        ],
        [
            r"¿(.*) es (.*) máscara de subred?",
            ["\nbot :  la máscara de subred tiene la misma apariencia que una dirección IP, pero en este caso, va a ser la que nos ayude a identificar si un host está dentro de una subred local o en una red remota.",]
            
        ],
        [
            r"¿(.*) máscara de (.*) subred?",
            ["\nbot :  la máscara de subred tiene la misma apariencia que una dirección IP, pero en este caso, va a ser la que nos ayude a identificar si un host está dentro de una subred local o en una red remota.",]
            
        ],
        [
            r"¿(.*) máscara de subred?",
            ["\nbot :  la máscara de subred tiene la misma apariencia que una dirección IP, pero en este caso, va a ser la que nos ayude a identificar si un host está dentro de una subred local o en una red remota.",]
            
        ],
        [
            r"¿(.*) es (.*) máscaras de subred?",
            ["\nbot : Las subredes son un método para maximizar el espacio de direcciones IPv4 de 32 bits y reducir el tamaño de las tablas de enrutamiento en una interred mayor. En cualquier clase de dirección, las subredes proporcionan un medio de asignar parte del espacio de la dirección host a las direcciones de red, lo cual permite tener más redes. La parte del espacio de dirección de host asignada a las nuevas direcciones de red se conoce como número de subred.",]
            
        ],
        [
            r"¿(.*) máscaras de (.*) subred?",
            ["\nbot : Las subredes son un método para maximizar el espacio de direcciones IPv4 de 32 bits y reducir el tamaño de las tablas de enrutamiento en una interred mayor. En cualquier clase de dirección, las subredes proporcionan un medio de asignar parte del espacio de la dirección host a las direcciones de red, lo cual permite tener más redes. La parte del espacio de dirección de host asignada a las nuevas direcciones de red se conoce como número de subred.",]
            
        ],
        [
            r"¿(.*) máscaras de subred?",
            ["\nbot : Las subredes son un método para maximizar el espacio de direcciones IPv4 de 32 bits y reducir el tamaño de las tablas de enrutamiento en una interred mayor. En cualquier clase de dirección, las subredes proporcionan un medio de asignar parte del espacio de la dirección host a las direcciones de red, lo cual permite tener más redes. La parte del espacio de dirección de host asignada a las nuevas direcciones de red se conoce como número de subred.",]
            
        ],
        
        [
            r"¿(.*) es (.*) máscara de red?",
            ["\nbot :  la máscara de subred tiene la misma apariencia que una dirección IP, pero en este caso, va a ser la que nos ayude a identificar si un host está dentro de una subred local o en una red remota.",]
            
        ],
        [
            r"¿(.*) máscara de (.*) red?",
            ["\nbot :  la máscara de subred tiene la misma apariencia que una dirección IP, pero en este caso, va a ser la que nos ayude a identificar si un host está dentro de una subred local o en una red remota.",]
            
        ],
        [
            r"¿(.*) máscara de red?",
            ["\nbot :  la máscara de subred tiene la misma apariencia que una dirección IP, pero en este caso, va a ser la que nos ayude a identificar si un host está dentro de una subred local o en una red remota.",]
            
        ],
        [
            r"¿(.*) es (.*) máscaras de red?",
            ["\nbot : Las subredes son un método para maximizar el espacio de direcciones IPv4 de 32 bits y reducir el tamaño de las tablas de enrutamiento en una interred mayor. En cualquier clase de dirección, las subredes proporcionan un medio de asignar parte del espacio de la dirección host a las direcciones de red, lo cual permite tener más redes. La parte del espacio de dirección de host asignada a las nuevas direcciones de red se conoce como número de subred.",]
            
        ],
        [
            r"¿(.*) máscaras de (.*) red?",
            ["\nbot : Las subredes son un método para maximizar el espacio de direcciones IPv4 de 32 bits y reducir el tamaño de las tablas de enrutamiento en una interred mayor. En cualquier clase de dirección, las subredes proporcionan un medio de asignar parte del espacio de la dirección host a las direcciones de red, lo cual permite tener más redes. La parte del espacio de dirección de host asignada a las nuevas direcciones de red se conoce como número de subred.",]
            
        ],
        [
            r"¿(.*) máscaras de red?",
            ["\nbot : Las subredes son un método para maximizar el espacio de direcciones IPv4 de 32 bits y reducir el tamaño de las tablas de enrutamiento en una interred mayor. En cualquier clase de dirección, las subredes proporcionan un medio de asignar parte del espacio de la dirección host a las direcciones de red, lo cual permite tener más redes. La parte del espacio de dirección de host asignada a las nuevas direcciones de red se conoce como número de subred.",]
            
        ],
        
        
        [
            r"¿(.*) es (.*) notacion decimal punteada?",
            ["\nbot : La notación decimal con puntos es un sistema de presentación de números que es un poco diferente de las convenciones comunes en aritmética como se enseña en las escuelas. Específicamente, la notación decimal con puntos se usa en varios contextos de TI, incluidas las direcciones de protocolo de Internet.",]
            
        ],
        [
            r"¿(.*) es (.*) lan?",
            ["\nbot : LAN es la abreviatura de Local Area Network. Denomina redes con extensión física limitada. La mayoría de las redes LAN se usan en hogares privados o en empresas, para instalar redes de hogar o de empresa. De este modo, distintos dispositivos pueden comunicarse entre ellos. De este modo, el intercambio de datos tiene lugar primero a nivel local. Una red LAN consiste en un mínimo de dos dispositivos finales, pero puede conectar miles. Sin embargo, para las grandes distancias es más conveniente usar redes MAN y WAN. Una red de área local o Local Area Network puede conectar ordenadores, teléfonos inteligentes, impresoras, escáneres, dispositivos de almacenamiento, servidores y otros dispositivos de red entre sí y con Internet. Si, por ejemplo, una impresora está conectada a un ordenador a través de USB, normalmente solo este PC puede acceder a ella. Sin embargo, si la impresora está integrada en la red, varios dispositivos de la casa pueden imprimir a la vez.",]
            
        ],
        [
            r"¿(.*) son (.*) lan?",
            ["\nbot : LAN es la abreviatura de Local Area Network. Denomina redes con extensión física limitada. La mayoría de las redes LAN se usan en hogares privados o en empresas, para instalar redes de hogar o de empresa. De este modo, distintos dispositivos pueden comunicarse entre ellos. De este modo, el intercambio de datos tiene lugar primero a nivel local. Una red LAN consiste en un mínimo de dos dispositivos finales, pero puede conectar miles. Sin embargo, para las grandes distancias es más conveniente usar redes MAN y WAN. Una red de área local o Local Area Network puede conectar ordenadores, teléfonos inteligentes, impresoras, escáneres, dispositivos de almacenamiento, servidores y otros dispositivos de red entre sí y con Internet. Si, por ejemplo, una impresora está conectada a un ordenador a través de USB, normalmente solo este PC puede acceder a ella. Sin embargo, si la impresora está integrada en la red, varios dispositivos de la casa pueden imprimir a la vez.",]
            
        ],
        [
            r"¿(.*) es (.*) man?",
            ["\nbot : MAN es la sigla de Metropolitan Area Network, que puede traducirse como Red de Área Metropolitana. Una red MAN es aquella que, a través de una conexión de alta velocidad, ofrece cobertura en una zona geográfica extensa (como una ciudad o un municipio).",]
            
        ],
        [
            r"¿(.*) son (.*) man?",
            ["\nbot : MAN es la sigla de Metropolitan Area Network, que puede traducirse como Red de Área Metropolitana. Una red MAN es aquella que, a través de una conexión de alta velocidad, ofrece cobertura en una zona geográfica extensa (como una ciudad o un municipio).",]
            
        ],
        [
            r"¿(.*) es (.*) wan?",
            ["\nbot : Las WAN son redes a gran escala que abarcan países e incluso continentes. No conectan ordenadores individuales, sino otras redes como LAN o MAN. Las WAN pueden ser públicas o estar gestionadas por empresas para conectar varias ubicaciones a grandes distancias.",]
            
        ],
        [
            r"¿(.*) son (.*) wan?",
            ["\nbot : Las WAN son redes a gran escala que abarcan países e incluso continentes. No conectan ordenadores individuales, sino otras redes como LAN o MAN. Las WAN pueden ser públicas o estar gestionadas por empresas para conectar varias ubicaciones a grandes distancias.",]
            
        ],
        [
            r"¿(.*) tipos (.*) clases ip (.*)?",
            ["\nbot : Existen 4 y son, Clase A que abarca de 0.0.0.0 a la 127.255.255.255., La clase B que abarca de 128.0.0.0 a la 191.255.255.255, la clase C que abarca de 192.0.0.0 a la 223.255.255.255. y la clase D que abarca de 224.0.0.0 a la 239.255.255.255",]
            
        ],
        [
            r"¿(.*) tipos (.*) clases ip?",
            ["\nbot : Existen 4 y son, Clase A que abarca de 0.0.0.0 a la 127.255.255.255., La clase B que abarca de 128.0.0.0 a la 191.255.255.255, la clase C que abarca de 192.0.0.0 a la 223.255.255.255. y la clase D que abarca de 224.0.0.0 a la 239.255.255.255",]
            
        ],
        [
            r"¿(.*) pertenece (.*) ip?",
            ["\nbot : Puedes saberlo por el primer octeto de la ip, como por ejemplo: 192.168.5.2 -> que si tomamos el primer octeto, tenemos '192', de esa manera puedes ver a que clase pertenece",]
            
        ],
        [
            r"¿(.*) pertenecer (.*) ip?",
            ["\nbot : Puedes saberlo por el primer octeto de la ip, como por ejemplo: 192.168.5.2 -> que si tomamos el primer octeto, tenemos '192', de esa manera puedes ver a que clase pertenece",]
            
        ],
        [
            r"¿(.*) indentificador (.*) host?",
            ["\nbot : El resultado varía según la clase de red, ejemplo la clase A utiliza 8 de red y 24 de host, la Clase b ocupa 16 y de host ocupa 16, de la clase c ocupa 24 de red y 8 de host, un ejemplo sería 178.165.12.3 , primero tenemos que es clase b, segundo identificamos que 16 son de red, entonces tenemos 178.165(ya como decimal quedaria como 11111111.11111111), esos pertenecen a red y .12.3(ya como decimal quedaria como 00000000.00000000) pertenecen a host",]
            
        ],
        [
            r"¿(.*) prefijo de red?",
            ["\nbot : Este viene al final de la red, que no es mas que un numero para saber cuantos bits pertenecen al de red, por ejemplo 192.16.3.5 /24, el cual no esta diciendo que tenemos 24 bits de red, y son 192.16.3",]
            
        ],
        
        [
            r"¿(.*) calcular (.*) direccion de red?",
            ["\nbot : sabiendo que el tenemos la ip, concemos su clase, y su mascara de subred, solo es cosa de tener los binarios de la ip y de la mascara de subred, con ello tendríamos que, hacer una operación AND, por ejemplo:192.168.55.44 una mascara de subred 255.255.255.0, ahora pasandolo a binarios, tendríamos que 192.168.55.44 => 1100000000.10101000.00110111.00101100  y de mascara de subred 255.255.255.0 => 11111111.11111111.11111111.00000000, ahora si aplicamos un AND  a estos dos, tendríamos algo así: 1100000000.10101000.00110111.00101100 AND 11111111.11111111.11111111.00000000 = 11000000.10101000.00110111.00000000, y si lo pasamos a notacion punteada, tendríamos algo así: 11000000.10101000.00110111.00000000 = 192.168.55.0, y esta sería su dirección de red",]
            
        ],
        [
            r"¿Cómo (.*) subnetear?",
            ["\nbot : Para subnetear, debes saber que, teniendo ya la ip, las mascara de subred, debes ver cuantos bits necesitas del host, para tomarlos y ver cuantas subredes puedes crear, por ejemplo, quieres tomar 3 bits prestados del host, ser vería de esta manera = 11111111.11111111.11111111.11100000, y para saber cuantas se ocupa la siguiente formula = 2^(número de bits prestados del host), en este caso seía así, 2^3=8 subredes, y como ya tenemos 3 bits más del host, entonces la submascara de red sería así = 11111111.11111111.11111111.11100000 => 255.255.255.224",]
            
        ],
        [
            r"¿Cómo (.*) ip (.*) a notación punteada?",
            ["\nbot : La forma de pasar una ip a notación punteada es de la siguiente manera, primero diremos que va a llegar maximo al numero 255 y minimo como 0, sabiendo eso pasamos a los 36 bits divididos en 8 bits, tomando primero 8 bits tenemos lo siguiente, 11111111., ahora cada uno tiene un valor independiente, del cual SIEMPRE SE LEE DE DERECHA A IZQUIERDA, empezando por derecha tenemos 1=1, el siguiente sería 1=2, luego 1=4, luego = 1=8,luego 1=16,luego 1=32,luego 1=64,luego 1=128, ya viendolo mejor tendríamos el siguiente, 11111111=> 1=128 1=64 1=32 1=16 1=8 1=4 1=2 1=1, una vez que ya tengas esto solo es cosa de ver cuales estan encedidos para posterior sumarlos como normalmente lo hacemos, Ejemplo: 10100011 = 128+0+32+0+0+0+2+1 => 163, y de esa manera se transforman a notación punteada",]
            
        ],
        [
            r"¿Qué (.*) subnetear?",
            ["\nbot : hace referencia a la subdivisión de una red en varias subredes.",]
            
        ],
        [
            r"¿Qué (.*) dirección de red?",
            ["\nbot : La dirección de Internet (IP Address) se utiliza para identificar tanto al host en concreto como la red a la que pertenece, de manera que sea posible distinguir a los host que se encuentran conectados a una misma red.",]
            
        ],
        [
            r"¿(.*) calcular (.*) ip?",
            ["\nbot : Como tal calcular una ip, no se puede, debe ser de algún protocolo como ipv4 o ipv6, yo solo sé sobre ipv4",]
            
        ],
        [
            r"¿(.*) ip?",
            ["\nbot : Una dirección IP es una dirección única que identifica a un dispositivo en Internet o en una red local. IP significa “protocolo de Internet”, que es el conjunto de reglas que rigen el formato de los datos enviados a través de Internet o la red local.",]
            
        ],
        [
            r"¿Qué (.*) red?",
            ["\nbot : La red informática nombra al conjunto de computadoras y otros equipos interconectados, que comparten información, recursos y servicios. Puede a su vez dividirse en diversas categorías, según su alcance (red de área local o LAN, red de área metropolitana o MAN, red de área amplia o WAN, etc.),",]
            
        ],
        
        [
            r"¿(.*) protocolos ip?",
            ["\nbot : Existen 3 protocolos de internet, los cuales son Ipv4 y Ipv6, del cual solo conozco el ipv4",]
            
        ],
        [
            r"¿(.*) es (.*) enrutamiento?",
            ["\nbot : Este es el proceso de reenviar paquetes entre redes, buscando la ruta más corta",]
            
        ],
        [
            r"¿(.*) es (.*) wildcard?",
            ["\nbot : La wildcard es la máscara inversa de la submascara de red, se utilizan más en las listas de control de acceso, un ejemplo sencillo sería que tenemos una máscara de red de 255.255.255.0, entonces la wildcard sería 0.0.0.255, pasando a un ejemplo mas complejo, teneos una submascara de red de 255.255.255.252 y entonces lo inverso es 0.0.0.3, de una manera más coloquial y facil de comprender es que son los bits que le hacen falta a un octecto de la mascara de red para llegar a 255, ejemplo tenemos una submascara de red 255.252.0.0 y lo inverso a ello , sería 0.3.255.255",]
            
        ],
        [
            r"¿(.*) wildcard?",
            ["\nbot : La wildcard es la máscara inversa de la submascara de red, se utilizan más en las listas de control de acceso, un ejemplo sencillo sería que tenemos una máscara de red de 255.255.255.0, entonces la wildcard sería 0.0.0.255, pasando a un ejemplo mas complejo, teneos una submascara de red de 255.255.255.252 y entonces lo inverso es 0.0.0.3, de una manera más coloquial y facil de comprender es que son los bits que le hacen falta a un octecto de la mascara de red para llegar a 255, ejemplo tenemos una submascara de red 255.252.0.0 y lo inverso a ello , sería 0.3.255.255",]
            
        ],
        [
            r"¿(.*) calcular (.*) wildcard?",
            ["\nbot : No es complicado, solo es lo inverso a la mascara de red, por ejemplo, tenemos una máscara de red de 255.255.255.0, entonces la wildcard sería 0.0.0.255, pasando a un ejemplo mas complejo, teneos una submascara de red de 255.255.255.252 y entonces lo inverso es 0.0.0.3, de una manera más coloquial y facil de comprender es que son los bits que le hacen falta a un octecto de la mascara de red para llegar a 255, ejemplo tenemos una submascara de red 255.252.0.0 y lo inverso a ello , sería 0.3.255.255",]
            
        ],
        [
            r"¿(.*) es (.*) broadcast?",
            ["\nbot : El broadcast es un mensaje que se transmite a todos los miembros de una red y que no necesita ninguna acción de retroalimentación.",]
            
        ],
        [
            r"¿(.*) broadcast?",
            ["\nbot : El broadcast es un mensaje que se transmite a todos los miembros de una red y que no necesita ninguna acción de retroalimentación.",]
            
        ],
        [
            r"¿(.*) calcular (.*) broadcast?",
            ["\nbot : Para calcular el broad cast, no es algo complicado, una ves teniendo la dirección de red, y la wildcard, sería una unión de estas, de manera coloquial, si tenemos un direccionamieto como este: 192.235.6.0, y su wildcar es 0.0.0.255, entonces tendríamos una operación AND (11000000.11101011.00000110.00000000 AND 00000000.00000000.00000000.11111111 => 11000000.11101011.00000110.11111111 = 192.235.6.255)",]
            
        ],
        
    
    ]
def chatear():
    print("Hola que tal!, un gusto en verte, soy un asistene para que puedas aprender a calcular una red ipv4, disculpa, ¿cuál es tu nombre?")
    chat= Chat(pares,refleciones)
    chat.converse()
    respuesta = chat.converse()
    print(respuesta)

while True:
    chatear()
