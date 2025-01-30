from arbol_binario  import Arbol

arbol = Arbol()
arbol_superheroes = Arbol()
arbol_villanos = Arbol()

superheroe = {'nombre': 'Doctor Strnge', 'heroe': False, 'aparicion': 1942}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Capitan America', 'heroe': True, 'aparicion': 1960}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Iron Man', 'heroe': True, 'aparicion': 1960}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Hulk', 'heroe': False, 'aparicion': 1960}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Capitana Marvel', 'heroe': True, 'aparicion': 1960}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)


#b. listar los villanos ordenados alfabéticamente;
print("Listado en orden alfabetico de villanos")
arbol.inorden_villanos()
print()

#c. mostrar todos los superhéroes que empiezan con C;
print("Héroes que empiezan con C: ") 
arbol.busqueda_proximidad('C')

print()
#d. determinar cuántos superhéroes hay el árbol;
print("La cantidad de superheroes que hay son:")
print(arbol.contar_nodos())


#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre;
buscado = input("Ingrese el nombre que desee modificar: ")
arbol.busqueda_proximidad(buscado)
buscado = input("Ingrese nuevamente el nombre a modificar: ")
pos = arbol.busqueda(buscado)

if pos:
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        nombre, superheroe = arbol.eliminar_nodo(buscado)
        superheroe["nombre"] = nuevo_nombre
        arbol = arbol.insertar_nodo(nuevo_nombre,superheroe)
else:
    print("El nombre a modificar no se encuentra")

print()

print("Barrido con el nombre modificado: ")
arbol.inorden()
print()

#f. listar los superhéroes ordenados de manera descendente;
print("Barrido de manera descendente de los heroes: ")
arbol.postorden_heroes()
print()

#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#los villanos, luego resolver las siguiente tareas:
#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#los villanos, luego resolver las siguiente tareas:
arbol.dos_arboles(arbol_superheroes,arbol_villanos)

#I. determinar cuántos nodos tiene cada árbol;
print("Cantidad de nodos del arbol de villanos: ", arbol_villanos.contar_nodos())
print("Cantidad de nodos del arbol de heroes: ",arbol_superheroes.contar_nodos())
print()
#II. realizar un barrido ordenado alfabéticamente de cada árbol.
print("Barrido del arbol de villanos:")
arbol_villanos.inorden()
print()
print("Barrido del arbol de heroes")
arbol_superheroes.inorden()