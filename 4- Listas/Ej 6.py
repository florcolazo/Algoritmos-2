"""EJERCICIO 6-- .Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesa-
rias para poder realizar las siguientes actividades:
7.
a.eliminar el nodo que contiene la información de Linterna Verde; ok
b.mostrar el año de aparición de Wolverine; ok
c.cambiar la casa de Dr. Strange a Marvel;ok
d.mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;ok
e.mostrar el nombre y la casa de los superhéroes cuya fecha de aparición
sea anterior a 1963;ok
f.mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;ok
g.mostrar toda la información de Flash y Star-Lord;ok
h.listar los superhéroes que comienzan con la letra B, M y S;ok
i.determinar cuántos superhéroes hay de cada casa de comic. """

from lista import Lista

class Superheroe (object): 
    def __init__(self, nombre, anio_aparicion, casa, biografia): #inicializar los atributos de la instancia (objeto) de la clase. 
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

lista_personajes = Lista()


Superheroes = [ {'nombre': 'Linterna Verde','aparicion': 1999 ,'casa': 'DC' ,'biografia':'espada'},
                {'nombre': 'Wolverine','aparicion': 1974 ,'casa': 'Marvel' ,'biografia':'traje'},
                {'nombre': 'Deadpool','aparicion': 1960 ,'casa': 'Marvel' ,'biografia':'espada'},
                {'nombre': 'Dr Strange','aparicion': 1962 ,'casa': 'DC' ,'biografia':'armadura'},
                {'nombre': 'Capitana Marvel','aparicion': 1998 ,'casa': 'Marvel' ,'biografia':'armadura'},
                {'nombre': 'Mujer Maravilla','aparicion': 1979 ,'casa': 'DC' ,'biografia':'espada'},
                {'nombre': 'Flash','aparicion': 1980 ,'casa': 'DC' ,'biografia':'espada'},
                {'nombre': 'Star-Lord','aparicion': 1961,'casa': 'Marvel' ,'biografia':'traje'},
                {'nombre': 'Batman','aparicion': 1939,'casa': 'DC' ,'biografia':'capa'}
            ]

for superheroe in Superheroes :
    lista_personajes.insertar(superheroe, 'nombre')



print('Lista Superheroes')
lista_personajes.barrido()
print()

#A

lista_personajes.eliminar('Linterna Verde', 'nombre')

#B
pos = lista_personajes.busqueda('Wolverine','nombre')
if(pos > -1):
    print('El año de aparicion de Wolverine es', lista_personajes.obtener_elemento(pos)['aparicion'])

#C 
pos=lista_personajes.busqueda('Dr. Strange','nombre')
if (pos > -1):
    lista_personajes.obtener_elemento(pos)['casa'] = 'Marvel'


#D
con_traje = ''
con_armadura = ''

for i in range(lista_personajes.tamanio()):
    pos= lista_personajes.obtener_elemento(i)
    if (pos['biografia']=='traje'):
        con_traje +=(pos['nombre'] + "/")
    elif (pos['biografia'] =='armadura'):
        con_armadura +=(pos['nombre']+ '/')

print('Los personajes que en su biografia figura la palabra traje son: ',con_traje)
print('Los personajes que en su biografia figura la palabra armadura son: ',con_armadura)
print()

#E
for i in range(lista_personajes.tamanio()):
    pos= lista_personajes.obtener_elemento(i)

    if (pos ['aparicion'] < 1963):
        print ('Superheroe cuya aparicon es anterior a 1963:',pos['nombre'],'del comic',pos['casa'])

#I
cont_casa = 0
cont_casa2 = 0

for i in range(lista_personajes.tamanio()):
    pos = lista_personajes.obtener_elemento(i)
   
    if (pos['casa'] == 'Marvel'):
        cont_casa += 1
    elif (pos['casa'] == 'DC'):
        cont_casa2 += 1

print('La cantidad de super heroes que hay en el comic  Marvel son : ', cont_casa)
print('La cantidad de super heroes que hay en el comic dc son : ', cont_casa2)
cont_s = ""
cont_b = ""
cont_m = ""

for i in range(lista_personajes.tamanio()):
    pos = lista_personajes.obtener_elemento(i)

    if (pos['nombre'][0] == 'S'):
        cont_s += (pos['nombre']+'  ')
    elif (pos['nombre'][0] == 'B'):
        cont_b += (pos['nombre']+'  ')
    elif(pos['nombre'][0] == 'M'):
            cont_m += (pos['nombre']+'  ')

print('Superheroes cuyo nombre empiezan con S: ',cont_s)
print('Superheroes cuyo nombre empiezan con M: ',cont_m)
print('Superheroes cuyo nombre empiezan con B: ',cont_b)

#F
pos = lista_personajes.busqueda('Capitana Marvel','nombre')
if (pos> -1):
    print('la casa a la que pertenece la capitana marvel es', lista_personajes.obtener_elemento(pos)['casa'])

pos = lista_personajes.busqueda('Mujer Maravilla','nombre')
if (pos > -1):
    print('La casa de la mujer maravilla es:',lista_personajes.obtener_elemento(pos)['casa'])

#G
pos = lista_personajes.busqueda ('Flash','nombre')
if (pos > -1):
    print('Informacion de Flash:',lista_personajes.obtener_elemento(pos))
pos = lista_personajes.busqueda('Star-Lord','nombre')
if (pos > -1):
    print('Informacion de Star-Lord:',lista_personajes.obtener_elemento(pos))


print('Barrido sin contar a linterna verde porque se elimino:')

lista_personajes.barrido()