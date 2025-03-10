#Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Univer-
#se (MCU), desarrollar un algoritmo que contemple lo siguiente:
#a.además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo boo-
#leano que indica si es un héroe o un villano, True y False respectivamente;
#b.listar los villanos ordenados alfabéticamente;
#c.mostrar todos los superhéroes que empiezan con C;
#d.determinar cuántos superhéroes hay el árbol;
#e.Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre;
#f.listar los superhéroes ordenados de manera descendente;
#g.generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
#los villanos, luego resolver las siguiente tareas:
#I.determinar cuántos nodos tiene cada árbol;
#II.realizar un barrido ordenado alfabéticamente de cada árbol.


from arbol_binario  import Arbol

arbol = Arbol()
arbol_superheroes = Arbol()
arbol_villanos = Arbol()

superheroe = {'nombre': 'Doctor Strnge', 'heroe': False}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Capitan America', 'heroe': True}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Iron Man', 'heroe': True}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Hulk', 'heroe': False}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Capitana Marvel', 'heroe': True}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Thanos', 'heroe': False}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Black Widows', 'heroe': True}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Ravonna Renslayer', 'heroe': False}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Taneleer Tivan', 'heroe': False}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)
superheroe = {'nombre': 'Kang', 'heroe': False}
arbol = arbol.insertar_nodo(superheroe['nombre'], superheroe)


#b. listar los villanos ordenados alfabéticamente;
print("Listado en orden alfabetico de los villanos")
arbol.inorden_villanos()
print()

#c. mostrar todos los superhéroes que empiezan con C;
print("Héroes que empiezan con C: ") 
arbol.busqueda_proximidad('C')

print()
#d. determinar cuántos superhéroes hay el árbol;
print("La cantidad de superheroes que hay son:")
print(arbol.contar_superheroes())


#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre;
print('Buscando posibles coincidencias')
arbol.busqueda_proximidad("Doctor")

nombre_incorrecto = 'Doctor Strnge'
pos = arbol.busqueda(nombre_incorrecto)

if pos:
    print('Dato a corregir: ', nombre_incorrecto)
    nombre, datos = arbol.eliminar_nodo(nombre_incorrecto)
    datos["nombre"] = input("Ingrese nombre bien escrito").capitalize()
    arbol = arbol.insertar_nodo(datos["nombre"],datos)
else:
    print('No se encontro el nombre incorrecto')

print("Listado en orden alfabetico corregido")
arbol.inorden()
print()


#f. listar los superhéroes ordenados de manera descendente;
print("Barrido de manera descendente de los heroes: ")
arbol.postorden_heroes()
print()


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