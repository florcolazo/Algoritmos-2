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
    {'nombre_aprendiz':'Darth Maul','maestro':'luke Skywalker','color_sable': ['violeta'],'especie': 'humana'},
    {'nombre_aprendiz':'Padmé Amidala','maestro':'Yoda','color_sable': ['amarillo'],'especie': 'twilek'},

]

for jedi in jedis:
   
    lista_jedi.insertar(jedi,'especie')

lista_jedi.ordenar('nombre_aprendiz')

#lista_jedi.ordenar('especie')
#print()


# poshan_ahsoka = lista_jedi.busqueda('Ahsoka Tano', 'nombre_aprendiz') #puntoB
# info_ahsoka= lista_jedi.obtener_elemento(poshan_ahsoka)
# print('--la info de ahsoka tano es--', 'maestro:',info_ahsoka['maestro'],'color de sable de luz:', info_ahsoka['color_sable'], 'especie:', info_ahsoka['especie'])

# pos_kit = lista_jedi.busqueda('Kit Fisto', 'nombre_aprendiz') #puntoB
# info_kit= lista_jedi.obtener_elemento(pos_kit)
# print('--la info de Kit Fisto tano es--', 'maestro:',info_kit['maestro'],'color de sable de luz:', info_kit['color_sable'], 'especie:', info_kit['especie'])

lista_jedi.barrido()

# for i in range(lista_jedi.tamanio()): 
#     personaje = lista_jedi.obtener_elemento(i)

#     if (personaje['maestro'] == 'Yoda'): #puntoC
#             lista_yoda.insertar(personaje['nombre_aprendiz']) 

#     if (personaje['maestro'] == 'Luke Skywalker'): #puntoC
#             lista_luke.insertar(personaje['nombre_aprendiz']) 

#     if (personaje['especie'] == 'humana' or personaje['especie'] =='twilek'): #puntoD
#             lista_especie.insertar(personaje['nombre_aprendiz'])        
               
#     if (personaje['nombre_aprendiz'][0] == 'A'): #puntoD
#         listado_A.insertar(personaje['nombre_aprendiz'])
   

#     if  (len(personaje['color_sable']) > 1):
#         lista_sables.insertar(personaje['nombre_aprendiz']) #puntoF    


#     if (personaje['color_sable'] == 'violeta' or personaje['color_sable'] == 'amarillo'): #puntoG
#             lista_sable.insertar(personaje['nombre_aprendiz'])
#             lista_sable.insertar(personaje['maestro'])  

#     if (personaje['maestro'] == 'Qui-Gon Jin'): #puntoH
#         lista_quigon.insertar(personaje['nombre_aprendiz'])
#     if (personaje['maestro'] == 'Mace Windu'): #puntoH
#         lista_mace.insertar(personaje['nombre_aprendiz'])    
                     
    

# print ('los aprendices de yoda son ')
# lista_yoda.barrido() 
# print ('los aprendices de Luke Skywalker son ')
# lista_luke.barrido() 
# print ('los jedis de especie humana y twilek son ')
# lista_especie.barrido() 
# print('el nombre de los jedis que empiezan con A son: ')   
# listado_A.barrido()  
# print('los jedis que usaron sable de luz color amarillo o violeta son: ')   
# lista_sable.barrido()  
# print(' el nombre de los padawans(aprendices) de Qui-Gon Jin son : ')   
# lista_quigon.barrido() 
# print(' el nombre de los padawans(aprendices) de son mace windu son: ')   
# lista_mace.barrido() 
# print('Jedis que usaron sable de luz de más de un color')
# lista_sables.barrido()
