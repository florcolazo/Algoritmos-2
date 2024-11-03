#Dada una lista de números enteros eliminar de estas los números primos

from lista import Lista
from random import randint

lista_num = Lista()


for i in range(10):
    num = randint(1, 10)
    lista_num.insertar(num)

def es_primo(numero):
    """Función para verificar si un número es primo."""
    cantidad = 0 
    for i in range(1, numero+1):
        if (numero % i == 0 ):
            cantidad +=1
    return cantidad ==2  

print('Lista original:')
lista_num.barrido()

# Eliminar números primos usando el método eliminar
i = 0
while i < lista_num.tamanio():
    numero = lista_num.obtener_elemento(i)
    if es_primo(numero):
        lista_num.eliminar(numero)
    else:
        i += 1

print('Lista sin primos:')
lista_num.barrido()
 

