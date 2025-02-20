""" Implementar los algoritmos necesarios para resolver las siguientes tareas:
a. concatenar dos listas, una atrás de la otra;
b. concatenar dos listas en una sola omitiendo los datos repetidos y manteniendo su orden;
c. contar cuántos elementos repetidos hay entre dos listas, es decir la intersección de ambas;[113]
d. eliminar todos los nodos de una lista de a uno a la vez mostrando su contenido """

from lista import Lista
from random import randint
lista_uno = Lista()
lista_dos = Lista()
lista_concatenada = Lista()

for i in range(5):
    lista_uno.insertar(i) #cargamos las dos listas
    lista_dos.insertar(randint(1,10))

print('lista uno')
lista_uno.barrido()
print()

print('lista dos')
lista_dos.barrido()
print()

cont_repetidos = 0

#A
for i in range(lista_dos.tamanio()): 
     numero = (lista_dos.obtener_elemento(i)) 
     lista_concatenada.insertar(numero)

for i in range(lista_uno.tamanio()):
     numero = (lista_uno.obtener_elemento(i)) 
     lista_concatenada.insertar(numero)

#B
for i in range(lista_dos.tamanio()): 
    num = lista_dos.obtener_elemento(i)
    if(lista_uno.busqueda(num) == -1):
        lista_uno.insertar(num) 
    else:
        cont_repetidos+=1 #C
   
print('la cantidad de elementos repetidos son: ', cont_repetidos)
print('lista concatenada sin repetir')
lista_uno.barrido()  

while(lista_uno.tamanio()>0):#puntoD
    numero = (lista_uno.obtener_elemento(0)) 
    print('numero eliminado: ',numero)
    aux=lista_uno.eliminar(numero)

print('Lista concatenada con todos los elementos :')
lista_concatenada.barrido()    

