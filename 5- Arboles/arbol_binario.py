from cola import Cola

class Arbol(object):

    def __init__(self, info=None, datos=None,frecuencia = 0):
        self.info = info
        self.datos = datos
        self.der = None
        self.izq = None
        self._altura = 0
        self.frecuencia = frecuencia



    def arbol_vacio(self):
        return self.info is None
    
    def altura(self, arbol):
        if(arbol is None):
            return -1
        else:
            return arbol._altura


    def actualizar_altura(self):    #nos va a permitir saber cuando un subarbol esta desvalanceado
        if(self is not None):
            altura_izq = self.altura(self.izq)
            altura_der = self.altura(self.der)
            self._altura = (altura_izq if altura_izq > altura_der else altura_der) + 1
    


    def rotacion_simple(self, control): #el raiz se transforma en el aux
        if(control):
            aux = self.izq
            self.izq = aux.der
            aux.der = self
        else:
            aux = self.der
            self.der = aux.izq
            aux.izq = self
        self.actualizar_altura() #y se actualiza la altura
        aux.actualizar_altura()
        return aux



    def rotacion_doble(self, control):
        if(control):
            self.izq = self.izq.rotacion_simple(False)
            self = self.rotacion_simple(True)
        else:
            self. der = self.der.rotacion_simple(True)
            self = self.rotacion_simple(False)
        return self



    def balancear(self):
        if(self is not None):
            if(self.altura(self.izq)-self.altura(self.der) == 2):
                if(self.altura(self.izq.izq) >= self.altura(self.izq.der)):
                    self = self.rotacion_simple(True)
                else:
                    self = self.rotacion_doble(True)
            elif(self.altura(self.der)-self.altura(self.izq) == 2):
                if(self.altura(self.der.der) >= self.altura(self.der.izq)):
                    self = self.rotacion_simple(False)
                else:
                    self = self.rotacion_doble(False)
        return self




    def insertar_nodo(self, dato, datos=None): #!el self representa el objeto y el dato representa
                                                     #!el nodo que queremos Agregar
        if(self.info is None):
            self.info = dato
            self.datos = datos
        elif(dato < self.info):     #!preguntamos si es mayor o menor que lo que tenemos en el 
            if(self.izq is None):            #info, lo que nos va a determinar si tenemos que ir 
                self.izq = Arbol(dato, datos)   #hacia la izquierda o derecha
            else:
                self.izq = self.izq.insertar_nodo(dato, datos)
        else:   #cada vez que nos vamos a la izq o der se crea otro arbol

            if(self.der is None): #si derecha es vacio,se tiene que crear el nodo para poder cargar la info
                self.der = Arbol(dato, datos)   #sino aplicamos recursividad y volvemos a llamar al nodo
            else:                               #el mismo procedimiento se usa en la izq
                self.der = self.der.insertar_nodo(dato, datos)
        self = self.balancear()
        self.actualizar_altura()
        return self



#los 3 barridos son iguales pero lo que cambia es el orden de las llamadas recursivas

    #este barrido permite hacer un listado en orden ascendente 
    def inorden(self):  
        if(self.info is not None):  #la raiz del arbol es "info"
            if(self.izq is not None): #este primero hace la llamada recursiva con el izq, cuando termina de barrer el arbol izq
                                        #muestra el nodo raiz y despues barre el arbol derecho 
                self.izq.inorden()
            print(self.info, self.datos)
            if(self.der is not None):
                self.der.inorden()



    def postorden(self): #cuando se hace el postorden, primero va al derecho, despues muestra la info, y desp va a la izq
        if(self.info is not None):
            if(self.der is not None):   
                print(self.info)
            if(self.izq is not None):
                self.izq.postorden()

    def postorden_heroes(self, clave = None): #EJERCICIO 5
        if (self.info is not None):
            if (self.der is not None):
                self.der.postorden_heroes()
            if (self.datos["heroe"] == True):
                print(self.info)
            if (self.izq is not None) :
                self.izq.postorden_heroes()      


    def preorden(self): #cuando hace el preorden primero se muestra la info, despues va a la izq y desp al derecho
        
        if(self.info is not None): 
            print(self.info, self._altura)
            if(self.izq is not None): #se va a la izq
                self.izq.preorden()
            if(self.der is not None):
                self.der.preorden() #se va al derecho

    def busqueda(self, clave): #es parecida al preorden
        pos = None  
        if(self.info is not None):  
            if(self.info == clave): #si self.info es igual a lo que estamos buscando
                pos = self  #a pos le asignamos self
            elif(clave < self.info and self.izq is not None): #si lo que estamos buscando es menor a lo que esta en el self.info y en el subarbol izq hay un nodo probamos buscar
                pos = self.izq.busqueda(clave)  
            elif(self.der is not None): #chequeamos que haya un nodo a la derecha
                pos = self.der.busqueda(clave)
        return pos  #si pos sale con valor NONE significa que no lo encontramos
    
    def busqueda_proximidad(self, clave): #EJERCICIO 5
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad(clave)
            if(self.info[0:len(clave)] == clave):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_proximidad(clave)


    def busqueda_proximidad2(self, clave):  #usada en el ej 23
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad2(clave)
            if(self.datos['derrotada_por'][0:len(clave)] == clave):
                print(self.info, self.datos)
            if(self.der is not None):
                self.der.busqueda_proximidad2(clave)    


    def busqueda_proximidad3(self, clave):  #usada en el ej 23
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad3(clave)
            if(self.datos['capturada_por'][0:len(clave)] == clave):
                print(self.info, self.datos)
            if(self.der is not None):
                self.der.busqueda_proximidad3(clave) 



    def remplazar(self):#el reemplazar es utilizado por el eliminar
        """Determina el nodo que remplazará al que se elimina."""
        info, datos = None, None    #aux 
        if(self.der is None): #si la derecha del nodo esta vacia significa que ese es el mayor
            info = self.info
            datos = self.datos
            if(self.izq is not None):
                self.info = self.izq.info
                self.der = self.izq.der
                self.izq = self.izq.izq
                self.datos = self.izq.datos
            else:
                self.info = None
                self.datos = None
        else:
            info, datos = self.der.remplazar()
        return info, datos

    def eliminar_nodo(self, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
        info, datos = None, None #ponemos el dato que queremos eliminar
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):#si el dato que se quiere eliminar es menor nos vamos a la izq
                
                    info, datos = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):#si el dato es mayor vamos por la derecha
                    info, datos = self.der.eliminar_nodo(clave)
            else:                           #si no es mayor ni menor lo encontramos
                info = self.info
                datos = self.datos

                if(self.der is None and self.izq is None):
                    self.info = None
                    self.datos = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                    self.datos = self.datos
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                    self.datos = self.datos
                else:
                    info_aux, datos_aux = self.izq.remplazar()
                    self.info = info_aux
                    self.datos = datos_aux
                    # raiz.info, raiz.nrr = aux.info, aux.nrr
        # self = self.balancear()
        self.actualizar_altura()
        return info, datos
    
    def contar_ocurrencias(self, buscado):#usado para el ej1
        cantidad = 0
        if(self.info is not None):
            if(self.info == buscado):   
                cantidad += 1   #incrementamos cantidad
            if(self.izq is not None):
                cantidad += self.izq.contar_ocurrencias(buscado)
            if(self.der is not None):
                cantidad += self.der.contar_ocurrencias(buscado)
        return cantidad
    
    def contar_pares_impares(self): #usado para el ej1
        pares, impares = 0, 0   #Ponemos pares e impares y inicializamos a las 2 en cero
        if(self.info is not None):
            if(self.info % 2 == 0):
                pares += 1
            else:
                impares += 1
            if(self.izq is not None):
                par, impar = self.izq.contar_pares_impares()
                pares += par
                impares += impar
            if(self.der is not None):
                par, impar = self.der.contar_pares_impares()
                pares += par
                impares += impar
        return pares, impares

    def barrido_por_nivel(self):   
        pendientes = Cola() #creamos una cola sobre la que vamos a trabajar
        pendientes.arribo(self)#arribamos la info
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info)
            if(nodo.izq is not None):#chequeamos si el nodo izq no esta vacio y arribamos
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)    

    def barrido_por_nivel_huff(self):
        pendientes = Cola()
        pendientes.arribo(self)
        while(not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print(nodo.info, nodo.frecuencia)
            if(nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if(nodo.der is not None):
                pendientes.arribo(nodo.der)


    def contar_buscados(self, buscado):#usado para el ej5
        cantidad = 0
        if(self.info is not None):
            if(self.info[0]== buscado):   
                cantidad += 1   
            if(self.izq is not None):
                cantidad += self.izq.contar_buscados(buscado)
            if(self.der is not None):
                cantidad += self.der.contar_buscados(buscado)
        return cantidad

    def contar_superheroes(self):# EJERCICIO 5
        cantidad_superheroes = 0
        if(self.info is not None):
            if(self.datos['villano']== False):   
                cantidad_superheroes += 1   
            if(self.izq is not None):
                cantidad_superheroes += self.izq.contar_superheroes()
            if(self.der is not None):
                cantidad_superheroes += self.der.contar_superheroes()
        return cantidad_superheroes
    
    def contador_criaturas(self, dic):
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.contador_criaturas(dic)
            if (self.datos['capturada_por'] in dic and self.datos['capturada_por'] != ''):
                dic[self.datos['capturada_por']] += 1 #el dic tiene un solo campo, el nombre del heroe, al que se le asigna un valor numericoo (Cantidad de capturas)
            elif (self.datos['capturada_por'] != ''):
                dic[self.datos['capturada_por']] = 1
            if (self.der is not None):
                self.der.contador_criaturas(dic)



    def modificar(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.modificar(clave)
            if(self.info[0:len(clave)] == clave):
                self.info ='Doctor Strange'
                self.datos['name']='Doctor Strange'
            if(self.der is not None):
                self.der.modificar(clave)      


    def dos_arboles(self,arbol_superheroes, arbol_villanos): #EJERCICIO 5
                if(self.info is not None):
                        if(self.datos['heroe'] == True):
                            arbol_superheroes = arbol_superheroes.insertar_nodo(self.info, self.datos)
                        else:
                            arbol_villanos = arbol_villanos.insertar_nodo(self.info, self.datos)
                        if(self.izq is not None):
                            self.izq.dos_arboles(arbol_superheroes, arbol_villanos)
                        if(self.der is not None):
                            self.der.dos_arboles(arbol_superheroes, arbol_villanos)

    def contar_nodos(self): #EJERCICIO 5
        cantidad_nodos = 0
        if(self.info is not None):  
            cantidad_nodos += 1   
            if(self.izq is not None):
                cantidad_nodos += self.izq.contar_nodos()
            if(self.der is not None):
                cantidad_nodos += self.der.contar_nodos()
        return cantidad_nodos  


    def modificar(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.modificar(clave)
            if(self.info[0:len(clave)] == clave):
                self.info ='Dragón Ladón'
                self.datos['criatura']='Dragón Ladón'
            if(self.der is not None):
                self.der.modificar(clave) 


    def inorden_criaturas(self):  
        if(self.info is not None):  
            if(self.izq is not None): 
                self.izq.inorden_criaturas()
                print(self.datos)
            if(self.der is not None):
                self.der.inorden_criaturas() 

    
    
    def inorden_villanos(self,clave = None): #EJERCICIO 5
            if(self.info is not None):
                if(self.izq is not None):
                    self.izq.inorden_villanos()  
                if (self.datos["heroe"] == False):  
                    print(self.info)
                if(self.der is not None):
                    self.der.inorden_villanos()

                 


        
    def contador_criaturas_derrotadas(self, dic):
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.contador_criaturas_derrotadas(dic)
            if (self.datos['capturado_por'] in dic and self.datos['capturado_por'] != ''):
                dic[self.datos['capturado_por']] += 1 #el dic tiene un solo campo, el nombre del heroe, al que se le asigna un valor numericoo (Cantidad de capturas)
            elif (self.datos['capturado_por'] != ''):
                dic[self.datos['capturado_por']] = 1
            if (self.der is not None):
                self.der.contador_criaturas_derrotadas(dic)                
                        
    def inorden_capturados_heracles(self,clave = None):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_capturados_heracles()  
            if (self.datos["capturado_por"] == "Heracles"):  
                print(self.info)
            if(self.der is not None):
                self.der.inorden_capturados_heracles() 

    def inorden_no_derrotados(self,clave = None):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.inorden_no_derrotados()  
            if (self.datos["capturado_por"] == ""):  
                print(self.info)
            if(self.der is not None):
                self.der.inorden_no_derrotados()     

    def añadir_descripcion(self):
            if(self.info is not None):
                if(self.izq is not None):
                    self.izq.añadir_descripcion()
                print("La criatura es",self.info)
                nueva_descripcion = input("Ingrese una descripcion")
                self.datos["descripcion"]= nueva_descripcion
                if(self.der is not None):
                    self.der.añadir_descripcion()

    def modificar_capturador(self, criatura, heroe):
            pos = self.busqueda(criatura)
            if (pos):
                pos.datos['capturado_por'] = heroe
            else:
                print('No hay ninguna criatura con el nombre', criatura, 'en el arbol.')

    def busqueda_por_coincidencia(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_por_coincidencia(clave)
            if(clave in self.info):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_por_coincidencia(clave)

        