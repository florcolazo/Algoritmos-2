""" Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

b.listar los entrenadores que hayan ganado más de tres torneos;
[114]c.el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d.mostrar todos los datos de un entrenador y sus Pokémos;
e.mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;

g.el promedio de nivel de los Pokémons de un determinado entrenador;
h.determinar cuántos entrenadores tienen a un determinado Pokémon;
i.mostrar los entrenadores que tienen Pokémons repetidos;
j.determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te
rrakion o Wingull;
k.determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos; """

from lista import Lista

lista_entrenadores = Lista()

entrenadores = [ {"nombre": "Juan","torneos_ganados": 2, "batallas_perdidas":6 ,"batallas_ganadas": 25, "pokemons" : Lista() },
                 {"nombre": "Maria","torneos_ganados":8, "batallas_perdidas": 9,"batallas_ganadas": 20,"pokemons" : Lista() },
                 {"nombre": "Pedro","torneos_ganados":12, "batallas_perdidas": 8,"batallas_ganadas": 31,"pokemons" : Lista() }
            ]

pokemons = [{"nombre":"Tyrantrum", "nivel": 12 ,"tipo":"fuego", "subtipo":"planta", "entrenador": "Juan" },
            {"nombre":"Wingull", "nivel": 180 ,"tipo":"agua","subtipo":"volador", "entrenador": "Juan"},
            {"nombre":"Wolverine", "nivel":3  ,"tipo":"fuego"  ,"subtipo":"terreno", "entrenador": "Pedro" },
            {"nombre":"Tyrantrum"  , "nivel": 12 ,"tipo":"fuego"  ,"subtipo":"planta", "entrenador": "Maria" },
            {"nombre":"Wingull" , "nivel": 18 ,"tipo":"agua"  ,"subtipo":"volador", "entrenador": "Pedro" },
            {"nombre":"Tyrantrum"  , "nivel": 12 ,"tipo":"fuego"  ,"subtipo":"planta", "entrenador": "Maria" },
            {"nombre":"Gigante" , "nivel": 21 ,"tipo":"agua","subtipo":"volador", "entrenador": "Juan" },
            {"nombre":"Rayo" , "nivel":3  ,"tipo":"fuego"  ,"subtipo":"terreno", "entrenador": "Pedro" }
]

for entrenador in entrenadores:
    lista_entrenadores.insertar(entrenador, 'nombre')

for pokemon in pokemons:
    pos = lista_entrenadores.busqueda(pokemon['entrenador'],'nombre')
    if (pos > -1):
        del pokemon['entrenador']
        lista_entrenadores.obtener_elemento(pos)['pokemons'].insertar(pokemon,'nombre')

#A
buscado = input('Ingrese nombre del entrenador a buscar')
pos = lista_entrenadores.busqueda(buscado, 'nombre')
if ( pos > -1):
    print('la cantidad de pokemons del entrenador es',lista_entrenadores.obtener_elemento(pos)['pokemons'].tamanio())
else:
    print('No se encontro el entrenador')
print()


    

#B LISTAR LOS ENTRENADORES QUE HAYAN GANADO MAS DE TRES TORNEOS

for i in range(lista_entrenadores.tamanio()):
    pos = lista_entrenadores.obtener_elemento(i)
    if (pos['torneos_ganados'] > 3):
        print('El entrenador', pos['nombre'], 'ha ganados mas de tres torneos')

#C el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados

maximo = 0
pos_maximo = -1

# Recorremos la lista de entrenadores para encontrar al que tiene más torneos ganados

for i in range(lista_entrenadores.tamanio()):
    if(lista_entrenadores.obtener_elemento(i)['torneos_ganados'] > maximo):
        maximo = lista_entrenadores.obtener_elemento(i)['torneos_ganados']
        pos_maximo = i # Guardamos el índice correcto del entrenador con más torneos ganados

#obtenemos los datos del entrenador que tiene más torneos ganados
entrenador_max = lista_entrenadores.obtener_elemento(pos_maximo)
print('El entrenador con mayor torneos ganados es:')
print(entrenador_max['nombre'])

# Buscamos el Pokémon de mayor nivel de este entrenador
max_nivel = 0
pokemon_max = None

# Recorremos la lista de Pokémon del entrenador

for j in range(entrenador_max['pokemons'].tamanio()):
    pokemon = entrenador_max['pokemons'].obtener_elemento(j)
    if pokemon['nivel'] > max_nivel:
        pokemon_max = pokemon['nivel']
        pokemon_max = pokemon #guardamos el pokemon con mayor nivel

#si se encontro un pokemon de mayor nivel, lo mostramos

if pokemon_max:
    print(f'El pokemon de mayor nivel es {pokemon_max["nombre"]} con nivel {pokemon_max["nivel"]}')
else:
    print ('Este esntrenador no tiene Pokemon')

#D - .mostrar todos los datos de un entrenador y sus Pokémos;

def mostrar_pokemones(lista_entrenadores, nombre_entrenador):
    nombre_entrenador = input('Ingrese nombre del entrenador para ver sus pokemones')
    pos = lista_entrenadores.busqueda(nombre_entrenador, 'nombre')

    if pos != -1: # Si el entrenador existe
        entrenador = lista_entrenadores.obtener_elemento(pos)
        print(f"Entrenador: {entrenador['nombre']}")
        print(f"Torneos ganados: {entrenador['torneos_ganados']}")
        print(f"Batallas ganadas: {entrenador['batallas_ganadas']}")
        print(f"Batallas perdidas: {entrenador['batallas_perdidas']}")

    if entrenador['pokemons'].tamanio() > 0:
        print(f"Pokemons de {entrenador['nombre']}:")
        for i in range(entrenador['pokemons'].tamanio()):
            pokemon = entrenador['pokemons'].obtener_elemento(i)
            print(f"-{pokemon['nombre']} (Nivel: {pokemon['nivel']}, Tipo: {pokemon['tipo']}, Subtipo {pokemon['subtipo']})")
        
    else:
        print('entrenador no encontrado')

mostrar_pokemones(lista_entrenadores, 'nombre')

#e.mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;


for i in range (lista_entrenadores.tamanio()):
    entrenador = lista_entrenadores.obtener_elemento(i)
    total_batallas = entrenador['batallas_ganadas'] + entrenador['batallas_perdidas']
    if total_batallas > 0 and (entrenador['batallas_ganadas'] / total_batallas) * 100 > 79:
        print(f"{entrenador['nombre']} ({(entrenador['batallas_ganadas'] / total_batallas) * 100:.2f}% victorias)")



#F.los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo);

def entrenadores_con_pokemon_especifico(lista_entrenadores):
    for i in range(lista_entrenadores.tamanio()):
        entrenador = lista_entrenadores.obtener_elemento(i)
        tiene_pokemon_especifico = False

        for j in range(entrenador['pokemons'].tamanio()):
            pokemon = entrenador['pokemons'].obtener_elemento(j)
            # Verificar si el Pokémon es de tipo fuego/planta o agua/volador
            if (pokemon['tipo'] == 'fuego' and pokemon['subtipo'] == 'planta') or \
               (pokemon['tipo'] == 'agua' and pokemon['subtipo'] == 'volador'):
                tiene_pokemon_especifico = True
                break
        
        if tiene_pokemon_especifico:
            print(f"{entrenador['nombre']} tiene Pokémon tipo fuego/planta o agua/volador.")

entrenadores_con_pokemon_especifico(lista_entrenadores)

#G el promedio de nivel de los Pokémons de un determinado entrenador;
cont_nivel = 0
cant_pokemons = 0
buscado = input('Ingrese nombre del entrenador para ver el promedio de nivel sus pokemons: ')
pos = lista_entrenadores.busqueda(buscado,'nombre')
if (pos > -1 ):
    for i in range(lista_entrenadores.obtener_elemento(pos)['pokemons'].tamanio()):
        cont_nivel += lista_entrenadores.obtener_elemento(pos)['pokemons'].obtener_elemento(i)["nivel"] 
        cant_pokemons += 1


print("El promedio de nivel de los pokemons del entrenador", buscado, " es de ", cont_nivel/cant_pokemons,"%")
print()

#h.determinar cuántos entrenadores tienen a un determinado Pokémon;

cont_pokemon = 0
buscado = input("Ingrese el nombre del pokemon ")
for i in range(lista_entrenadores.tamanio()):
    pos = lista_entrenadores.obtener_elemento(i)["pokemons"].busqueda(buscado,"nombre")
    if (pos > -1):
        cont_pokemon +=1

print("La cantidad de entrenadores que tienen al pokemon ",buscado," son ",cont_pokemon)
print()


#i-entrenadores de Pokémon que tengan duplicados de algún Pokémon en su lista.

entrenadores_aux = []

for i in range(lista_entrenadores.tamanio()):
    entrenador = lista_entrenadores.obtener_elemento(i)
    pokemons = entrenador["pokemons"]

   

    for j in range(pokemons.tamanio()):
        pokemon = pokemons.obtener_elemento(j)
  


        for k in range(j+1, pokemons.tamanio()):
            pokemon_aux = pokemons.obtener_elemento(k)
           

            if pokemon['nombre'] == pokemon_aux['nombre']:
                
                    entrenadores_aux.append(entrenador['nombre'])
                    
                
                
print("Los entrenadores que tienen pokemon repetidos son : ", entrenadores_aux)
print()


#j.determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull;

cont_tyrantrum = ''
cont_terrakion = ''
cont_wingull = ''

for i in range(lista_entrenadores.tamanio()):
    entrenador = lista_entrenadores.obtener_elemento(i)
    pokemons = entrenador['pokemons']

    pos1 = pokemons.busqueda("Tyrantrum", 'nombre')
    pos2 = pokemons.busqueda("Terrakion", 'nombre')
    pos3 = pokemons.busqueda("Wingull", 'nombre')

    if pos1 > -1 :
        cont_tyrantrum += entrenador['nombre'] + " "
    if pos2 > -1 :
        cont_terrakion += entrenador['nombre'] + " "
    if pos3 > -1 :
        cont_wingull += entrenador['nombre'] + " "

print("Entrenadores que tienen el Pokémon Tyrantrum: ", cont_tyrantrum if cont_tyrantrum else "Ninguno")
print("Entrenadores que tienen el Pokémon Terrakion: ", cont_terrakion if cont_terrakion else "Ninguno")
print("Entrenadores que tienen el Pokémon Wingull: ", cont_wingull if cont_wingull else "Ninguno")

#k.determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos

buscado1 = input('Ingrese el nombre del entrenador:')
buscado2 = input('Ingrese el nombre del Pokemon:')

pos1 = lista_entrenadores.busqueda(buscado1,'nombre')

if pos1 > -1 :
    entrenador = lista_entrenadores.obtener_elemento(pos1)
    pos2 = entrenador ['pokemons'].busqueda(buscado2,'nombre')

    if pos2 > -1:
        pokemon = entrenador['pokemons'].obtener_elemento(pos2)
        print(f'El entrenador {buscado1} tiene el pokemon {buscado2}')
        print(f'Datos del entrenador : {entrenador}')
        print (f'Datos del Pokemon:{pokemon}')
    else:
        print(f'El entrenador{buscado1} no tiene al pokemon {buscado2}')
else:
    print(f'El entrenador {buscado1} no fue encontrado')