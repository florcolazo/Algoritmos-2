# Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, 
# colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las 
# actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twilek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron

from lista import Lista

class Jedi (object):
    def __init__ (self, nombre_aprendiz, maestro, color_sable,especie): 
        self.nombre_aprendiz = nombre_aprendiz
        self.maestro = maestro
        self.color_sable = color_sable
        self.especie = especie
        

lista_jedi = Lista()
lista_yoda = Lista()
lista_luke = Lista()
lista_especie = Lista()
listado_A = Lista()
lista_sable = Lista()
lista_quigon = Lista ()
lista_mace = Lista ()
lista_sables = Lista ()


jedis = [
    {'nombre_aprendiz':'Jar Jar Binks','maestro':'Mace Windu','color_sable':['rojo', 'amarillo', 'azul'],'especie': 'humana'},
    {'nombre_aprendiz':'Palpatine.','maestro':'Yoda','color_sable': ['violeta'],'especie': 'humana'},
    {'nombre_aprendiz':'Ahsoka Tano','maestro':'Qui-Gon Jin','color_sable': ['violeta'],'especie': 'twilek'},
    {'nombre_aprendiz':'Kit Fisto','maestro':'Yoda','color_sable': ['amarillo', 'violeta', 'azul'],'especie':'twilek'},
    {'nombre_aprendiz':'Darth Maul','maestro':'Luke Skywalker','color_sable': ['violeta'],'especie': 'humana'},
    {'nombre_aprendiz':'Padmé Amidala','maestro':'Yoda','color_sable': ['amarillo'],'especie': 'twilek'},

]
# Insertar Jedi en la lista y ordenar por nombre
for jedi in jedis:
    lista_jedi.insertar(jedi, 'nombre_aprendiz')
lista_jedi.ordenar('nombre_aprendiz')

# Mostrar Jedi ordenados por nombre y especie
print("Jedi ordenados por nombre:")
lista_jedi.barrido()

# B Mostrar información de Ahsoka Tano y Kit Fisto

pos_ahsoka = lista_jedi.busqueda('Ahsoka Tano', 'nombre_aprendiz') 
info_ahsoka= lista_jedi.obtener_elemento(pos_ahsoka)
print('La informacion de Ahsoka Tano es:', 'Maestro:',info_ahsoka['maestro'],'Color de sable de luz:', info_ahsoka['color_sable'], 'Especie:', info_ahsoka['especie'])

pos_kit = lista_jedi.busqueda('Kit Fisto', 'nombre_aprendiz') 
info_kit= lista_jedi.obtener_elemento(pos_kit)
print('La informacion de Kit Fisto tano es:', 'Maestro:',info_kit['maestro'],'Color de sable de luz:', info_kit['color_sable'], 'Especie:', info_kit['especie'])

lista_jedi.barrido()

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
lista_yoda = Lista()
lista_luke = Lista()
for i in range(lista_jedi.tamanio()):
    jedi = lista_jedi.obtener_elemento(i)
    if jedi['maestro'] == 'Yoda':
        lista_yoda.insertar(jedi['nombre_aprendiz'])
    elif jedi['maestro'] == 'Luke Skywalker':
        lista_luke.insertar(jedi['nombre_aprendiz'])

print("Padawans de Yoda:")
lista_yoda.barrido()
print("Padawans de Luke Skywalker:")
lista_luke.barrido()

# d. mostrar los Jedi de especie humana y twilek;

aprendiz_yoda = ""
aprendiz_luke = ""
for i in range (lista_jedi.tamanio()):
    pos = lista_jedi.obtener_elemento(i)
    if (pos["maestro"] == "Yoda"):
        aprendiz_yoda += (pos["nombre_aprendiz"]+ "  ")
    if (pos["maestro"] == "Luke Skywalker"):
        aprendiz_luke += (pos["nombre_aprendiz"]+ "  ")    

print("Los Padawan de Yoda son: ", aprendiz_yoda)
print("Los Padawan de Luke Skywalker son: ", aprendiz_luke)
print()

# e. listar todos los Jedi que comienzan con A;

listado_A = Lista()
for i in range(lista_jedi.tamanio()):
    jedi = lista_jedi.obtener_elemento(i)
    if jedi['nombre_aprendiz'][0] == 'A':
        listado_A.insertar(jedi['nombre_aprendiz'])

print("Jedi cuyos nombres comienzan con 'A':")
listado_A.barrido()

# f. mostrar los Jedi que usaron sable de luz de más de un color;

lista_sables = Lista()
for i in range(lista_jedi.tamanio()):
    jedi = lista_jedi.obtener_elemento(i)
    if len(jedi['color_sable']) > 1:
        lista_sables.insertar(jedi['nombre_aprendiz'])

print("Jedi que usaron sable de más de un color:")
lista_sables.barrido()

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;

lista_sable = Lista()
for i in range(lista_jedi.tamanio()):
    jedi = lista_jedi.obtener_elemento(i)
    if 'amarillo' in jedi['color_sable'] or 'violeta' in jedi['color_sable']:
        lista_sable.insertar(jedi['nombre_aprendiz'])

print("Jedi que usaron sable de luz amarillo o violeta:")
lista_sable.barrido()

# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron
lista_quigon = Lista()
lista_mace = Lista()
for i in range(lista_jedi.tamanio()):
    jedi = lista_jedi.obtener_elemento(i)
    if jedi['maestro'] == 'Qui-Gon Jin':
        lista_quigon.insertar(jedi['nombre_aprendiz'])
    elif jedi['maestro'] == 'Mace Windu':
        lista_mace.insertar(jedi['nombre_aprendiz'])

print("Padawans de Qui-Gon Jin:")
lista_quigon.barrido()
print("Padawans de Mace Windu:")
lista_mace.barrido()   
