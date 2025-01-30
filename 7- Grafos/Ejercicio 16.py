"""16. Implementar un grafo no dirigido para almacenar puntos turísticos de interés de un determi-
nado país teniendo en cuenta los siguientes requerimientos:

a. debe ser un grafo completo es decir que todos los vértices se deben conectar con todos;

b. cargar los siguientes lugares (con sus coordenadas de latitud y longitud) templos de: Ate-
nas (Partenón), Zeus (Olimpia), Hera (Olimpia), Apolo (Delfos),Poseidón (Sunión), Arte-
misa (Éfeso) y Teatro de Dionisio (Acrópolis)

c. hallar el árbol de expansión mínimo partiendo de cualquiera de estos lugares;


d. hallar el camino más corto para ir desde el templo de Atenea, el Partenón, en Atenas hasta
el templo de Apolo, en Delfos."""

from grafo import Grafo

templos = Grafo(dirigido=False)

templos.insertar_vertice("Ateneas",data={'latitud': 37.9, "longitud": 23.7}) #Templo,latitud,longitud
templos.insertar_vertice("Zeus",data={'latitud': 4.944, "longitud": -73.96})
templos.insertar_vertice("Hera",data={'latitud': 37.6, "longitud": 21.6})
templos.insertar_vertice("Apolo",data={'latitud': 38.4, "longitud": 22.5})
templos.insertar_vertice("Poseidon",data={'latitud': 37.6, "longitud": 24.0})
templos.insertar_vertice("Artemisa",data={'latitud': 37.9, "longitud": 27.3})
templos.insertar_vertice("Teatro de Dionisio",data={'latitud': 37.9, "longitud": 23.7})

templos.insertar_arista(1.7,"Ateneas","Zeus") #km
templos.insertar_arista(303,"Ateneas","Hera")
templos.insertar_arista(189,"Ateneas","Apolo")
templos.insertar_arista(61.4,"Ateneas","Poseidon")
templos.insertar_arista(482,"Ateneas","Artemisa")
templos.insertar_arista(0.001,"Ateneas","Teatro de Dionisio") #0.001 = 1m
templos.insertar_arista(302,"Zeus","Hera")
templos.insertar_arista(181,"Zeus","Apolo")
templos.insertar_arista(60.8,"Zeus","Poseidon")
templos.insertar_arista(481,"Zeus","Artemisa")
templos.insertar_arista(2.6,"Zeus","Teatro de Dionisio")
templos.insertar_arista(242,"Hera","Apolo")
templos.insertar_arista(355,"Hera","Poseidon")
templos.insertar_arista(1.503,"Hera","Artemisa")
templos.insertar_arista(294,"Hera","Teatro de Dionisio")
templos.insertar_arista(234,"Apolo","Poseidon")
templos.insertar_arista(1303,"Apolo","Artemisa")
templos.insertar_arista(163,"Apolo","Teatro de Dionisio")
templos.insertar_arista(641,"Poseidon","Artemisa")
templos.insertar_arista(68.8,"Poseidon","Teatro de Dionisio")
templos.insertar_arista(484,"Artemisa","Teatro de Dionisio")



bosque = templos.prim()
print('Arbol de expansion mínimo')
peso = 0
for elemento in bosque:
    print(elemento[1][0], '-', elemento[1][1])
    peso += elemento[0]
print('Costo total', peso)
print()

vertice_origen = templos.buscar_vertice('Ateneas')
vertice_destino = templos.buscar_vertice('Apolo')
camino = templos.dijkstra(vertice_origen, vertice_destino)

print("El camino más corto para ir desde Ateneas hasta Apolo:")
destino = 'Apolo'
costo = None
while(not camino.pila_vacia()):
    dato = camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]
print('El costo total del camino es:', costo)
