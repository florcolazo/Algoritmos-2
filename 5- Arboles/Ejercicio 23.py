""" #23. Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
resuelva las siguientes consultas:
a.listado inorden de las criaturas y quienes la derrotaron;
b.se debe permitir cargar una breve descripción sobre cada criatura;
c.mostrar toda la información de la criatura Talos;
d.determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
e.listar las criaturas derrotadas por Heracles;
f.listar las criaturas que no han sido derrotadas;
g.además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
o dios que la capturo;
h.modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
Erimanto indicando que Heracles las atrapó;
i.se debe permitir búsquedas por coincidencia;
j.eliminar al Basilisco y a las Sirenas;
k.modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
derroto a varias;
l.modifique el nombre de la criatura Ladón por Dragón Ladón;
m.realizar un listado por nivel del árbol;
n.muestre las criaturas capturadas por Heracles. """
from arbol_binario import Arbol

arbol = Arbol( )


criaturas = {"nombre": "Ceto", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Tifon", "capturado_por": "Zeus","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Equidna", "capturado_por": "Argos Panoptes","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Dino", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Pefredo", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Enio", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Escila", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Caribdis", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Euriale", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Esteno", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Medusa", "capturado_por": "Perseo","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Ladon", "capturado_por": "Heracles","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre":"Aguila del Caucaso", "capturado_por":"","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Quimera", "capturado_por": "Belerofonte","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Hidra de Lerna", "capturado_por": "Heracles","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Leon de Nemea", "capturado_por": "Heracles","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Esfinge", "capturado_por": "Edipo","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Dragon de la Colquida", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Cerbero", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Cerda de Cromion", "capturado_por": "Teseo","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Ortro", "capturado_por": "Heracles","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Toro de Creta", "capturado_por": "Teseo","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Jabali de Calidon", "capturado_por": "Atalanta","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Carcinos", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Gerion", "capturado_por": "Heracles","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Cloto", "capturado_por": "Zeus","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Laquesis", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Atropos", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Minotauro de Creta", "capturado_por": "Teseo","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Harpias", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Argos Panoptes", "capturado_por": "Hermes","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Talos", "capturado_por": "Medea","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Sirenas", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Piton", "capturado_por": "Apolo","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Cierva de Cerinea", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Basilisco", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Jabali de Erimanto", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)
criaturas = {"nombre": "Aves del Estinfalo", "capturado_por": "","descripcion":""}
arbol = arbol.insertar_nodo(criaturas["nombre"],criaturas)


#EJERCICIO A
print("Listado inorden de las criaturas y quienes la derrotaron")
arbol.inorden_criaturas()
print

#EJERCICIO B
#arbol.añadir_descripcion()
#arbol.inorden()

 #EJERCICIO C
buscado = "Talos"
pos = arbol.busqueda(buscado)
if pos:
    print ("\nInformacion de la criatura Talos:'",buscado," ",pos.datos)
print()


#EJERCICIO D
dic = {}
arbol.contador_criaturas_derrotadas(dic)
#print(dic)

def ordenar(item):
    return item[1]

lista = list(dic.items())
lista.sort(key=ordenar, reverse=True)


print('\nHeroes/Dioses que derrotaron a la mayor cantidad de criaturas:')
for pos in range (0,3):
    if len(lista[pos]) >= 2:
	    print(lista[pos][0], '(derroto a',  lista[pos][1], 'criatura(s))')
    



#EJERCICIO E e.listar las criaturas derrotadas por Heracles;
print('\nLista de criaturas derrotadas por Heracles:') #E
arbol.inorden_capturados_heracles()

#EJERCICIO F listar las criaturas que no han sido derrotadas;

print('\nCriaturas que no han sido derrotadas')
arbol.inorden_no_derrotados()


#EJERCICIO H modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#Erimanto indicando que Heracles las atrapó;

arbol.modificar_capturador('Cerbero', 'Heracles')
arbol.modificar_capturador('Toro de Creta', 'Heracles')
arbol.modificar_capturador('Cierva de Cerinea', 'Heracles')
arbol.modificar_capturador('Jabalí de Erimanto', 'Heracles')
print()
arbol.inorden_criaturas()

#EJERCICIO I.se debe permitir búsquedas por coincidencia;
clave = input('Comience a escribir parte del nombre de una criatura para buscarla: ')
print('Criaturas que contienen "', clave, '" en su nombre:' )
arbol.busqueda_proximidad2(clave)
print()

#EJERCICIO J .eliminar al Basilisco y a las Sirenas;

info, datos = arbol.eliminar_nodo('Basilisco')
print (info, 'ha sido eliminado')
info, datos = arbol.eliminar_nodo('Sirenas')
print (info, 'ha sido eliminado')
print()


print()
print("Barrido sin los nodos de Basilisco y Sirenas")
arbol.inorden()
print() 

#EJERCICIO K modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#derroto a varias; NO FUNCIONA
buscado = "Toro de Creta"
pos = arbol.busqueda(buscado)

print("Resultado de búsqueda Estinfalo:", pos)
if pos is not None:
    print("Antes de la modificación:", pos)  
    pos.datos['capturado_por'] = 'Heracles'
    pos.datos['descripcion'] = 'Heracles derrotó a varias.'
    print("Después de la modificación:", pos) 
else:
    print("No se encontró 'Aves del Estinfalo' en el árbol.")

#EJERCICIO L.modifique el nombre de la criatura Ladón por Dragón Ladón;

pos = arbol.busqueda('Ladon')  # Buscar el nodo
print("Resultado de búsqueda Ladon:", pos)

if pos:
    nombre, datos = arbol.eliminar_nodo('Ladon')  
    print("Eliminado:", nombre, datos)
    
    if datos is not None:  
        datos['nombre'] = 'Dragón Ladón'  
        arbol = arbol.insertar_nodo('Dragón Ladón', datos)  
    else:
        print("No se pudo eliminar 'Ladón' o el nodo no existe.")  


print("Árbol actualizado Ladon:")
arbol.inorden()


#EJERCICIO M , realizar un listado por nivel del arbol

print('Barrido por nivel del arbol:')
arbol.barrido_por_nivel()
print()

#EJERCICIO N , muestre las criaturas capturadas por Heracles
print ('Capturadas por Heraccles')
arbol.inorden_capturados_heracles()
print()

print('lista completa')
arbol.inorden()