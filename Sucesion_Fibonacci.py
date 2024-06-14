"""
Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un
número dado. La sucesión de Fibonacci es una serie de números en la que el siguiente número
se obtiene sumando los dos números anteriores. Los primeros dos números de la serie son 0 y 1.
"""
n = int(input("ingrese un numero:"))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))


# Plataforma: Python 3.9.7
# SO: Linux Mint 20.2
# Fecha: 14/06/24

"""
                       ##### OPTIMIZACION SEGUN CHATGPT #####
                       
"Una forma de optimizar la implementación es utilizando la técnica de memorización,
donde los resultados de las llamadas anteriores se almacenan en un diccionario para evitar
cálculos redundantes. Aquí hay una implementación optimizada de la función de Fibonacci
utilizando memorización:"

n = int(input("Ingrese un número: "))

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(n))

"""
