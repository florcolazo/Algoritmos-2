""" Dada una lista que contiene información de los personajes de la saga de Star Wars con la si
a. listar todos los personajes de género femenino;
b. listar todos los personajes de especie Droide que aparecieron en los primeros seis episodios de la saga;
c. mostrar toda la información de Darth Vader y Han Solo;
d. listar los personajes que aparecen en el episodio VII y en los tres anteriores;
e. mostrar los personajes con edad mayor a 850 años y de ellos el mayor;
f. eliminar todos los personajes que solamente aparecieron en los episodios IV, V y VI;
g. listar los personajes de especie humana cuyo planeta de origen es Alderaan;
h. mostrar toda la información de los personajes cuya altura es menor a 70 centímetros;
i. determinar en qué episodios aparece Chewbacca y mostrar además toda su información """

from lista import Lista

class Personajes_sw (object):
    def __init__ (self, nombre,altura, edad, genero, especie, planeta_natal, episodios_queaparecio ): 
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planeta_natal = planeta_natal
        self.episodios_queaparecio = episodios_queaparecio
        

lista_personajes_sw = Lista()
lista_femenina = Lista()
lista_Droide = Lista()
lista_alderaan = Lista()
lista_episodioVII = Lista()
Lista_altura = Lista()


personajes_sw = [
    {'nombre':'Leia','altura':'0,60', 'edad':19,'genero':'F', 'especie': 'humana', 'planeta_natal': 'Alderaan', 'episodios_queaparecio':['I','II','III','IV','V','VI','VII']},
    {'nombre':'Darth Vader','altura':'2,16', 'edad':854,'genero':'M', 'especie': 'Droide', 'planeta_natal': 'Alderaan', 'episodios_queaparecio':['I','II','III','IV','V','VI']},
    {'nombre':'Han solo','altura':'2,03', 'edad':900,'genero':'M', 'especie': 'humana', 'planeta_natal': 'Alderaan', 'episodios_queaparecio':['I','II','III','IV','V','VI','VII']},
    {'nombre':'Chewbacca','altura':'0,40', 'edad':200,'genero':'F', 'especie': 'Droide', 'planeta_natal': ' forestal,', 'episodios_queaparecio':['I','II','III','IV','V','VI','VII']},
    {'nombre':'Phasma','altura':'4,01', 'edad':890,'genero':'F', 'especie': 'humana', 'planeta_natal': 'pantanoso', 'episodios_queaparecio':['IV','V','VI']},
]

mayor_personaje = 0
mayor = 0

for personajes_sw in personajes_sw:
    lista_personajes_sw.insertar(personajes_sw,'nombre')

posDart = lista_personajes_sw.busqueda('Darth Vader', 'nombre') #puntoC
info_dart = lista_personajes_sw.obtener_elemento(posDart)
print('--la info de Darth Vader es--', 'altura:',info_dart['altura'],'edad:', info_dart['edad'],'anios', 'genero:', info_dart['genero'])
print('especie:', info_dart['especie'],'planeta natal:', info_dart['planeta_natal'], 'episodios en los que aparecio:', info_dart['episodios_queaparecio'])  

poshan_solo = lista_personajes_sw.busqueda('Han solo', 'nombre') #puntoC
info_han = lista_personajes_sw.obtener_elemento(poshan_solo)
print('--la info de Han Solo es--', 'altura:',info_han['altura'],'edad:', info_han['edad'],'anios', 'genero:', info_han['genero'])
print('especie:', info_han['especie'],'planeta natal:', info_han['planeta_natal'], 'episodios en los que aparecio:', info_han['episodios_queaparecio'])  

lista_personajes_sw.eliminar(['IV','V','VI'],'episodios_queaparecio')#puntoF


pos_Chewbacca= lista_personajes_sw.busqueda('Chewbacca', 'nombre') #puntoI
info_Chewbacca = lista_personajes_sw.obtener_elemento(pos_Chewbacca)
print('los episodios en los que aparece Chewbacca son: ', info_Chewbacca['episodios_queaparecio'])
print('--Y su info es--: ','altura:',info_Chewbacca['altura'],'edad:', info_Chewbacca['edad'],'anios', 'genero:', info_Chewbacca['genero'])
print('especie:', info_Chewbacca['especie'],'planeta natal:', info_Chewbacca['planeta_natal'])  


#lista_personajes_sw.barrido()

print('####################################################################################')

for i in range(lista_personajes_sw.tamanio()): 
        personaje = lista_personajes_sw.obtener_elemento(i)

        if (personaje['edad'] > 850): #puntoE
            print('el personaje con edad mayor a 850 es: ',personaje['nombre'], 'con edad', personaje['edad'])
            if (personaje['edad'] > mayor):
                mayor = personaje['edad']
                mayor_personaje = personaje ['nombre']

        if (personaje['altura'] < '0,70'): #puntoH
            Lista_altura.insertar(personaje,'nombre')
            # print('--INFO DE LOS PERSONAJES CON  ALTURA < A 70 CM--:','nombre:',personaje['nombre'],'edad:', personaje['edad'],'genero:', personaje['genero'])    
            # print('especie:', personaje['especie'],'planeta natal', personaje['planeta_natal'],'episodios en los que aparecio', personaje['episodios_queaparecio'])
                
        if (personaje['especie'] == 'humana' and personaje['planeta_natal'] == 'Alderaan'):#puntoG
            lista_alderaan.insertar(personaje['nombre'])


        if  ('VII' in personaje['episodios_queaparecio'] and 'VI' in personaje['episodios_queaparecio'] and 'V' in personaje['episodios_queaparecio'] and 'IV' in personaje['episodios_queaparecio']):
            lista_episodioVII.insertar(personaje['nombre']) #puntoD
        

        if (personaje['genero'] == 'F'): #puntoF
            lista_femenina.insertar(personaje['nombre']) 

        if (personaje['especie'] == 'Droide' and 'I' in personaje['episodios_queaparecio'] and 'II' in personaje['episodios_queaparecio'] and 'III' in personaje['episodios_queaparecio'] and 'IV' in personaje['episodios_queaparecio'] and 'V' in personaje['episodios_queaparecio']and 'VI' in personaje['episodios_queaparecio']): #puntoB
           lista_Droide.insertar(personaje['nombre']) #puntoB
            

print('los personajes con especie humana y planeta natal alderan son ') 
lista_alderaan.barrido()
print ('el personaje mayor es : ', mayor_personaje, ' y su edad es ', mayor)    
print('los personajes femeninos son: ') 
lista_femenina.barrido()
print('los personajes que aparecen en los episodios IV, V, VI, VII son:')
lista_episodioVII.barrido()
print('los personajes que miden menos de 70cm son:')
Lista_altura.barrido_personaje()
print('los personajes de especie droide que aparecen en los primeros VI episodios son : ')
lista_Droide.barrido()           
