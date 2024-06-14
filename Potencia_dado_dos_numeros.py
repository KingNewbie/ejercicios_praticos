"""Implementar una función para calcular la potencia dado dos números enteros, el primero re-
presenta la base y segundo el exponente."""

n = int(input("Ingrese un número Base entero positivo : "))
m = int(input("Ingrese un número Exponente entero positivo: "))

def potencia(n, m):
    return n ** m

print(potencia(n, m))  # Output: 8

""" Explicación de la Implementación Mejorada segun CHATGPT:

La función potencia es una implementación simple que calcula la potencia de un número dado
usando el operador **. Esto es más eficiente y directo que usar la recursión para calcular la
potencia. La recursión puede ser útil para problemas más complejos, pero para este caso, la
operación aritmética directa es la mejor opción.

"""
