# Crear el árbol principal con los nombres de héroes y villanos del MCU
from arbol_binario  import Arbol
arbol_mcu = Arbol()

# Insertar datos (Ejemplo: "Iron Man", True -> Es héroe)
personajes = [
    ("Iron Man", True), ("Thanos", False), ("Captain America", True),
    ("Loki", False), ("Spider-Man", True), ("Ultron", False),
    ("Doctor Strange", True), ("Hela", False), ("Black Widow", True),
    ("Red Skull", False), ("Captain Marvel", True), ("Dormammu", False)
]

# Insertar los personajes en el árbol
for nombre, es_heroe in personajes:
    arbol_mcu.insertar_nodo(nombre, es_heroe)

# a. Listar los villanos en orden alfabético
print("Villanos ordenados alfabéticamente:")
arbol_mcu.inorden(lambda nodo: print(nodo.info) if nodo.datos is False else None)

# b. Mostrar los superhéroes que empiezan con "C"
print("\nSuperhéroes que empiezan con 'C':")
arbol_mcu.busqueda_proximidad("C")

# c. Contar cuántos superhéroes hay en el árbol
contador_heroes = arbol_mcu.contar_ocurrencias(True)
print(f"\nNúmero total de superhéroes: {contador_heroes}")

# d. Corregir "Doctor Strange" (buscar y modificar)
print("\nCorrigiendo el nombre de Doctor Strange...")
nodo_strange = arbol_mcu.busqueda_proximidad("Doctor")
if nodo_strange:
    nodo_strange.info = "Doctor Strange"

# e. Listar los superhéroes en orden descendente
print("\nSuperhéroes en orden descendente:")
arbol_mcu.inorden(lambda nodo: print(nodo.info) if nodo.datos is True else None, reverse=True)

# f. Separar en dos árboles: héroes y villanos
arbol_heroes = Arbol()
arbol_villanos = Arbol()

arbol_mcu.separar_heroes_de_villanos(arbol_heroes, arbol_villanos)

# g. I. Contar cuántos nodos tiene cada árbol
print(f"\nCantidad de superhéroes: {arbol_heroes.contar_nodos()}")
print(f"Cantidad de villanos: {arbol_villanos.contar_nodos()}")

# g. II. Listar cada árbol en orden alfabético
print("\nSuperhéroes ordenados:")
arbol_heroes.inorden()
print("\nVillanos ordenados:")
arbol_villanos.inorden()