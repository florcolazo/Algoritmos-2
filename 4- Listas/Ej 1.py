1.Diseñar un algoritmo que permita contar la cantidad de nodos de una lista.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    # Método para agregar un nodo al final de la lista
    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # Método para contar los nodos
    def contar_nodos(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

# Ejemplo de uso:
lista = ListaEnlazada()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

print("Cantidad de nodos en la lista:", lista.contar_nodos())