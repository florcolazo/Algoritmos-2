from pila import Pila

#14-INGRESAR ELEMENTOS EN UNA PILA
    #OREDENADOS DE FORMA CRECIENTE
    #CREAR PILA AUX-SIN METODOS DE ORDENAMIENTO
'''
pila_datos = Pila

pila_aux = Pila()
for i in range (0,10):
    elemento = int(input('ingrese elemento'))
    
    if(pila_datos.pila_vacia()):
        print (elemento)
        pila_datos.apilar(elemento)
    
    else:
        if (elemento >= pila_datos.elemento_cima() ):
            pila_datos.apilar(elemento)
        else: 
            while(not pila_datos.pila_vacia() and pila_datos.elemento_cima()> elemento):
                pila_aux.apilar(pila_datos.desapilar())

            pila_datos.apilar(elemento)

            while(not pila_aux.pila_vacia()):
                
                pila_datos.apilar(pila_aux.desapilar())
                

while(not pila_datos.pila_vacia()):
    print('Elementos ordenados en orden crecientes:',pila_datos.desapilar())'''

#16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “T
#strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
#permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-bos episodios.
'''
EpisodioV = Pila()
EpisodioVII = Pila()
Pila_Actores = Pila() #pila de interseccion de personajes
paux = Pila() #pila auxiliar para desapilar los personajes no repetidos

EpisodioV.apilar('LEIA')
EpisodioV.apilar('DARTH')
EpisodioV.apilar('LUKE')
EpisodioV.apilar('OBI')
EpisodioV.apilar('CONDE')
EpisodioV.apilar('MACE')

EpisodioVII.apilar('OBI')
EpisodioVII.apilar('PADME')
EpisodioVII.apilar('ANAKIN')
EpisodioVII.apilar('CONDE')
EpisodioVII.apilar('YODE')
EpisodioVII.apilar('MACE')



while not EpisodioV.pila_vacia():
    pila_aux = EpisodioV.desapilar()
    while not EpisodioVII.pila_vacia():
        pila_aux2 = EpisodioVII.desapilar()
        if (pila_aux == pila_aux2):
            Pila_Actores.apilar(pila_aux)
        paux.apilar(pila_aux2)
    while (not paux.pila_vacia()):
        EpisodioVII.apilar(paux.desapilar())

while (not Pila_Actores.pila_vacia()):
    print ('los personajes repetidos en amobos episodios son:',Pila_Actores.desapilar())
        
'''


#EJERCICIO 22. Se recuperaron las bitácoras de las naves del cazarrecompensas Boba Fett y Din Djarin (The
#Mandalorian), las cuales se almacenaban en una pila (en su correspondiente nave) en cada
#misión de caza que emprendió, con la siguiente información: planeta visitado, a quien capturó,
#costo de la recompensa. Resolver las siguientes actividades:
#a. mostrar los planetas visitados en el orden que hicieron las misiones cada uno
#de los cazzarrecompensas;
#b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos
#quien obtuvo mayor fortuna;
#c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la
#que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
#d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.


'''
class Bitacora(object):

    def __init__(self,planeta,capturados,costo,):
        self.planeta = planeta
        self.capturados = capturados
        self.costo = costo


    def __str__(self):
        return self.planeta + '-'+str(self.capturados) +'-'+str(self.costo)

pila_Boba = Pila()
Pila_Din = Pila()


bitacora = Bitacora('tierra','tiver',985.00)
pila_Boba.apilar(bitacora)
bitacora = Bitacora('alderan','han solo',425.00)
pila_Boba.apilar(bitacora)
bitacora = Bitacora('bespin','kenovi',124.00)
pila_Boba.apilar(bitacora)
bitacora = Bitacora('crait','obiwan',693.00)
pila_Boba.apilar(bitacora)

bitacora = Bitacora('malastare','windu',415.00)
Pila_Din.apilar(bitacora)
bitacora = Bitacora('naboo','sing',2500.00)
Pila_Din.apilar(bitacora)
bitacora = Bitacora('mon','arrua',1000.00)
Pila_Din.apilar(bitacora)

pila_aux= Pila()
pila_aux2 = Pila()
'''
#EJERCICIO A- mostrar los planetas visitados en el orden que hicieron las misiones cada uno
#de los cazzarrecompensas
'''while (not pila_Boba.pila_vacia()):
    pila_aux = pila_Boba.desapilar()
    print ('Planetas visitados por Boba:',pila_aux.planeta)

while (not Pila_Din.pila_vacia()):
    pila_aux = Pila_Din.desapilar()
    print ('Planetas visitados por DIN:',pila_aux.planeta)

'''
#EJERCICIO B- determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos
#quien obtuvo mayor fortuna;
'''
Total1 = 0
Total2 = 0


while (not pila_Boba.pila_vacia()):
        pila_aux = pila_Boba.desapilar()
        Total1 += pila_aux.costo
        print('TOTAL RECAUDAD POR BOBA:',Total1)
        while (not Pila_Din.pila_vacia()):
            pila_aux2 = Pila_Din.desapilar()
            Total2 += pila_aux2.costo
            print('TOTAL RECAUDADO POR DIN:',Total2)
            if (Total1 >Total2):
                print('El que mayor recaudo fue Boba')
            else:
                print('El que mayor recaudo fue DIN')
        
   
'''

#EJERCICIO C-determinar el número de la misión –es decir su posición desde el fondo de la pila– en la
#que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;

""""
while (not pila_Boba.pila_vacia()):
    pos = 1
    pila_aux = pila_Boba.desapilar()
    pos = pos + 1
    if (pila_aux.capturados == 'han solo'):
        print('boba fett capturo a HAN SOLO en la mision numero:',pos)
"""

#EJERCICIO D- indicar la cantidad de capturas realizadas por cada cazarrecompensas.

"""print('Cantidad de capturas realizadas por Boba Fett:',pila_Boba.tamanio())
print('Cantidad de capturas realizadas por Din Djarin:',Pila_Din.tamanio())

if (pila_Boba.tamanio()> Pila_Din.tamanio()):
    print ('El casarecompensas Boba Fett realizo mas capturas')
else:
    print('El casarecompensas Din Djarin realizo mas capturas')
"""

#EJERCICIO 24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:
#a.
#determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
#ción uno la cima de la pila;
#[ 85 ]b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#car la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
'''
Pila_Personaje = Pila()

class Personaje(object):

    def __init__(self,nombre,peliculas):
        self.nombre = nombre
        self.peliculas = peliculas
        


    def __str__(self):
        return self.nombre + '-'+str(self.peliculas)


personaje = Personaje('Thanos',3)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Iron Man',7)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Toki',1)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Rocket Raccoon',3)
Pila_Personaje.apilar(personaje)
personaje = Personaje('James Barnes',6)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Valquiria',4)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Groot',4)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Chewbacca',5)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Viuda Negra',1)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Del Goren',10)
Pila_Personaje.apilar(personaje)
'''
#pila_aux = Pila()
#pos = 0

#.EJERCICIO A-determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-ción uno la cima de la pila;
'''
pila_aux = Pila()
pila_inversa = Pila()

while(not Pila_Personaje.pila_vacia()):
        x = Pila_Personaje.desapilar()
        pila_aux.apilar(x)
        pila_inversa.apilar(x)
        
while (not pila_aux.pila_vacia()):
    x = pila_aux.desapilar()
    Pila_Personaje.apilar((x))
    pos+=1
    if (x.nombre == 'Rocket Raccoon'):
            print('Rocket Raccoon se encuentra en la posicion numero:',pos)

        

#EJERCICIO B- determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#car la cantidad de películas en la que aparece;

while (not Pila_Personaje.pila_vacia()):
    pila_aux = Pila_Personaje.desapilar()
    if pila_aux.peliculas > 5 :
        
        print ('Personaje que participo en mas de 5 peliculas:',pila_aux.nombre,'--Cantidad de peliculas en que aparece:',pila_aux.peliculas)

#EJERCICO C-determinar en cuantas películas participo la Viuda Negra (Black Widow);

while (not Pila_Personaje.pila_vacia()):
    pila_aux = Pila_Personaje.desapilar()
    if (pila_aux.nombre == 'Viuda Negra'):
        print('La Viuda Negra participo en ',pila_aux.peliculas,'peliculas')

'''
#EJERCICIO D-. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
'''
while (not Pila_Personaje.pila_vacia()):
    pila_aux = Pila_Personaje.desapilar()
    if (pila_aux.nombre[0] == 'C') :
        print('Personajes cuyo nombre empieza con C',pila_aux.nombre)
    if (pila_aux.nombre[0] == 'D'):
        print('Personajes cuyo nombre empieza con D',pila_aux.nombre)
    if (pila_aux.nombre[0] == 'G'):
            print('Personajes cuyo nombre empieza con G',pila_aux.nombre)

'''


#de los cazzarrecompensas;
#b. determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos
#quien obtuvo mayor fortuna;
#c. determinar el número de la misión –es decir su posición desde el fondo de la pila– en la
#que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;
#d. indicar la cantidad de capturas realizadas por cada cazarrecompensas.


'''
class Bitacora(object):

    def __init__(self,planeta,capturados,costo,):
        self.planeta = planeta
        self.capturados = capturados
        self.costo = costo


    def __str__(self):
        return self.planeta + '-'+str(self.capturados) +'-'+str(self.costo)

pila_Boba = Pila()
Pila_Din = Pila()


bitacora = Bitacora('tierra','tiver',985.00)
pila_Boba.apilar(bitacora)
bitacora = Bitacora('alderan','han solo',425.00)
pila_Boba.apilar(bitacora)
bitacora = Bitacora('bespin','kenovi',124.00)
pila_Boba.apilar(bitacora)
bitacora = Bitacora('crait','obiwan',693.00)
pila_Boba.apilar(bitacora)

bitacora = Bitacora('malastare','windu',415.00)
Pila_Din.apilar(bitacora)
bitacora = Bitacora('naboo','sing',2500.00)
Pila_Din.apilar(bitacora)
bitacora = Bitacora('mon','arrua',1000.00)
Pila_Din.apilar(bitacora)

pila_aux= Pila()
pila_aux2 = Pila()
'''
#EJERCICIO A- mostrar los planetas visitados en el orden que hicieron las misiones cada uno
#de los cazzarrecompensas
'''while (not pila_Boba.pila_vacia()):
    pila_aux = pila_Boba.desapilar()
    print ('Planetas visitados por Boba:',pila_aux.planeta)

while (not Pila_Din.pila_vacia()):
    pila_aux = Pila_Din.desapilar()
    print ('Planetas visitados por DIN:',pila_aux.planeta)

'''
#EJERCICIO B- determinar cuántos créditos galácticos recaudo en total cada cazarrecompensas y de estos
#quien obtuvo mayor fortuna;
'''
Total1 = 0
Total2 = 0


while (not pila_Boba.pila_vacia()):
        pila_aux = pila_Boba.desapilar()
        Total1 += pila_aux.costo
        print('TOTAL RECAUDAD POR BOBA:',Total1)
        while (not Pila_Din.pila_vacia()):
            pila_aux2 = Pila_Din.desapilar()
            Total2 += pila_aux2.costo
            print('TOTAL RECAUDADO POR DIN:',Total2)
            if (Total1 >Total2):
                print('El que mayor recaudo fue Boba')
            else:
                print('El que mayor recaudo fue DIN')
        
   
'''

#EJERCICIO C-determinar el número de la misión –es decir su posición desde el fondo de la pila– en la
#que Boba Fett capturo a Han Solo, suponga que dicha misión está cargada;

""""
while (not pila_Boba.pila_vacia()):
    pos = 1
    pila_aux = pila_Boba.desapilar()
    pos = pos + 1
    if (pila_aux.capturados == 'han solo'):
        print('boba fett capturo a HAN SOLO en la mision numero:',pos)
"""

#EJERCICIO D- indicar la cantidad de capturas realizadas por cada cazarrecompensas.

"""print('Cantidad de capturas realizadas por Boba Fett:',pila_Boba.tamanio())
print('Cantidad de capturas realizadas por Din Djarin:',Pila_Din.tamanio())

if (pila_Boba.tamanio()> Pila_Din.tamanio()):
    print ('El casarecompensas Boba Fett realizo mas capturas')
else:
    print('El casarecompensas Din Djarin realizo mas capturas')
"""
'''
24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:
a.
determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
ción uno la cima de la pila;
[ 85 ]b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
car la cantidad de películas en la que aparece;
c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.'''

Pila_Personaje = Pila()

class Personaje(object):

    def __init__(self,nombre,peliculas):
        self.nombre = nombre
        self.peliculas = peliculas
        


    def __str__(self):
        return self.nombre + '-'+str(self.peliculas)


personaje = Personaje('Thanos',3)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Iron Man',7)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Toki',1)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Rocket Raccoon',3)
Pila_Personaje.apilar(personaje)
personaje = Personaje('James Barnes',6)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Valquiria',4)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Groot',4)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Chewbacca',5)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Viuda Negra',1)
Pila_Personaje.apilar(personaje)
personaje = Personaje('Del Goren',10)
Pila_Personaje.apilar(personaje)

pila_aux = Pila()
pos = 0
#.EJERCICIO A-determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-ción uno la cima de la pila;
'''
pila_aux = Pila()
pila_inversa = Pila()

while(not Pila_Personaje.pila_vacia()):
        x = Pila_Personaje.desapilar()
        pila_aux.apilar(x)
        pila_inversa.apilar(x)
        
while (not pila_aux.pila_vacia()):
    x = pila_aux.desapilar()
    Pila_Personaje.apilar((x))
    pos+=1
    if (x.nombre == 'Rocket Raccoon'):
            print('Rocket Raccoon se encuentra en la posicion numero:',pos)

        

        



#[ 85 ]b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
#car la cantidad de películas en la que aparece;

while (not Pila_Personaje.pila_vacia()):
    pila_aux = Pila_Personaje.desapilar()
    if pila_aux.peliculas > 5 :
        
        print ('Personaje que participo en mas de 5 peliculas:',pila_aux.nombre,'--Cantidad de peliculas en que aparece:',pila_aux.peliculas)

#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

while (not Pila_Personaje.pila_vacia()):
    pila_aux = Pila_Personaje.desapilar()
    if (pila_aux.nombre == 'Viuda Negra'):
        print('La Viuda Negra participo en ',pila_aux.peliculas,'peliculas')

'''
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

while (not Pila_Personaje.pila_vacia()):
    pila_aux = Pila_Personaje.desapilar()
    if (pila_aux.nombre[0] == 'C') :
        print('Personajes cuyo nombre empieza con C',pila_aux.nombre)
    if (pila_aux.nombre[0] == 'D'):
        print('Personajes cuyo nombre empieza con D',pila_aux.nombre)
    if (pila_aux.nombre[0] == 'G'):
            print('Personajes cuyo nombre empieza con G',pila_aux.nombre)


