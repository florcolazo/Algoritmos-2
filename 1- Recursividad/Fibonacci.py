#CALCULO FIBONACCI RECURSIVO

def fibonacciR(n):
    if (n == 0 or n==1):
        return n
    else:
        return fibonacciR(n-1) + fibonacciR (n-2)
    
#CALCULO FIBONACCI ITERATIVO

def fibonacciI(n):
    n0= 0
    n1 = 1
    fib = 0
    if(n ==0 or n==1):
        fib = n
    else:
        i= 2
        while (i <= n):
            fib = n0 + n1
            n0= n1
            n1 = fib
            i += 1
    return fib



print(fibonacciI(10))