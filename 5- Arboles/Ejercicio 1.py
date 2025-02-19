#Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea-
#toria– que resuelva las siguientes actividades:
#a.realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
#b.determinar si un número está cargado en el árbol o no;
#c.eliminar tres valores del árbol;
#d.determinar la altura del subárbol izquierdo y del subárbol derecho;
#e.determinar la cantidad de ocurrencias de un elemento en el árbol;
#f.contar cuántos números pares e impares hay en el árbol.

import random
from arbol_binario  import Arbol


arbol = Arbol()

for i in range(1000):
    arbol.insertar_nodo(random.randint(1, 1000))

print()

