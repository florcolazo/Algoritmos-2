#pedir al humano que ingrese los numero que quiera
#ordenar los numeros por burbuja
#mostrar los numero de forma ascendente
#mostrar los numeros de forma descendentres

""" def pedirDatos():
    lista = []
    while True:
        n = int (input("humano ingrese e numero que queiras(0 para terminar):"))
        if n==0:
            return lista
        else:
            lista.append(n)
    return lista

def burbuja(lista):
    tamano = len(lista)
    for _ in range(0,tamano):
        for j in range(0, tamano-1):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

    return lista

def mostrarLista(lista):
    tam = len(lista)
    print("lista ordenada de forma ascendente")
    for i in range(0,tam):
        print(f"{lista[i]}")
    print("lista ordenada de forma ascendente")
    for i in range(tam,0,-1):
        print(f"{lista[i-1]}")

lista = pedirDatos()
lista = burbuja(lista)
mostrarLista(lista)
 """

# calcular las calificaciones con las siguientes caracteristicas
#calificacion de practicas que es 40%
#calificacion de particiṕacion que es 20%
#calificacion de examen que es 40%
#obtener calificacion final sumando y obteniendo el promedio

print('ingresa la calificaciones del alumno')
practicas = float (input('calificacion de las practicas'))
participacion= float (input('calificacion de las participaciones'))
examen = float (input('calificacion delexamen'))
practicas *= 0.40
participacion *= 0.20
examen *= 0.40
final = practicas + participacion+examen
print(f"ESta es la calificacion final:{final:.2f}")

