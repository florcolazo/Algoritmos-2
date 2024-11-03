
# Ejercicio 1 : Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.
def fib(n):  
    if (n ==0  or n == 1):
        return (n)
    else:
        return ( fib(n-1) + fib(n-2) )
# Ejercicio 2 Implementar una función que calcule la suma de todos los números enteros comprendidos entre cero y un número entero positivo dado.


def sum(n):  
    if (n == 0):
        return (n)
    else:
        return (n + sum(n-1))

#Ejercicio 3 Implementar una función para calcular el producto de dos números enteros dados.
def prod(n1, n2):  
    if (n2 == 1):
        return (n1)
    else:
        return (n1 + prod(n1, n2-1))

# Ejercicio 4 calcular la potencia dado dos números enteros, el primero re- presenta la base y segundo el exponente.
def pot(base, exp): 
    if (exp == 0):
        return (1)
    else:
        return (base * pot(base, exp-1))

#Ejercicio 5 Desarrollar una función que permita convertir un número romano en un número decimal.
def romano(n): 
    if (n == ""):
        return (0)
    elif (n == "M"):
        return (1000)
    elif (n == "D"):
        return (500)
    elif (n == "C"):
        return (100)
    elif (n == "L"):
        return (50)
    elif (n == "X"):
        return (10)
    elif (n == "V"):
        return (5)
    elif (n == "I"):
        return (1)
    else:
        if (romano(n[0]) < romano(n[1])):
            return (romano(n[1]) - romano(n[0])) + romano(n[2:] )
        else:
            return (romano(n[0]) + romano(n[1:]))

# Ejercicio 6 Dada una secuencia de caracteres, obtener dicha secuencia invertida.
def invert(s):  
    if (len(s) == 1):
        return (s)
    else:
        return (s[-1]+invert(s[:-1]))


def serie(n):  # Ejercicio 7
    if (n == 1):
        return (n)
    else:
        return (1/serie(n-1))

# Ejercicio 8-Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema binario.
def invertDecaBin(n):  # Ejercicio 8
    if (n == 0):
        return ("")
    else:
        return invertDecaBin(n//2) + str(n % 2)
    
decimal=int(input('Ingrese numero a convertir'))
def decimal_abinario(decimal):
    binario= ''
    while decimal // 2!= 0:  #si el cociente  es distinto de 0 
        binario = str(decimal % 2) + binario  #se asigna a binario el resto
        decimal = decimal //2
        
    return binario
            

print('Conversion de numero decimal a binario:',decimal_abinario(decimal))  

def logaritmo(base, num):  # Ejercicio 9
    if (num <= base):
        return (1)
    else:
        return logaritmo(base, num/base) + 1

"""
%  -> Modulo
// -> Division Entera
/  -> Division Real
"""

def cont(num, ac):  # Ejercicio 10
    if ((num // 10) < 1):
        return (ac+1)
    else:
        return cont(num//10, ac+1)


def inversion(num, pos):  # Ejercicio 11
    if (num < 10):
        return (num)
    else:
        return ((num % 10) * 10**pos + inversion(num // 10, pos-1))


def mcd(n, n2):  # Ejercicio 11
    if (n2 == 0):
        return (n)
    else:
        return (n2, n % n2)



def Usarlafuerza(lista, O_buscado, indice):
        if (lista[indice] == O_buscado):
            print(O_buscado)
            print('se sacaron ', (indice+1), 'objetos')
        else:
            print(lista[indice]) 
            Usarlafuerza(lista, O_buscado, (indice+1))

#print (romano("XCVII"))

#mochila = ['objeto1','objeto2','objeto3','sable de luz','objeto4','objeto5']
#Usarlafuerza(mochila,'objeto5',0)
#print (invertDecaBin(5))



def laberinto(x, y, matriz):
    camino=[]
    if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
        if (matriz[x][y] == 2):
            print("Se Salio del Laberinto")
        elif (matriz[x][y] == 1):
            matriz[x][y] = 3
            laberinto(x, y+1, matriz)
            laberinto(x, y-1, matriz)
            laberinto(x+1, y, matriz)
            laberinto(x-1, y, matriz)
            matriz[x][y] = 1

matriz =[ [1,1,1,1,1],
          [0,0,1,0,1],
          [1,1,1,0,1],
          [1,0,0,0,0],
          [1,1,1,1,2] ]

laberinto(0, 0, matriz)