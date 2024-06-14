"""
Implementar una función para calcular el producto de dos números enteros dados.
"""

n = int(input("Ingrese un número entero positivo: "))
m = int(input("Ingrese otro número entero positivo: "))

def producto_recursivo(n, m):
    if m == 0:
        return 0
    else:
        return n + producto_recursivo(n, m - 1)
    
print(producto_recursivo(n, m)) 

"""
Explicación de la Implementación Mejorada segun CHATGPT:

Aunque la recursión puede ser útil para ciertos problemas, para la multiplicación de dos enteros, 
es más eficiente y sencillo usar la operación aritmética directa. La implementación iterativa 
es una buena opción si deseas evitar la recursión pero sigue siendo menos eficiente que usar directamente la multiplicación.
    
n = int(input("Ingrese un número entero positivo: "))
m = int(input("Ingrese otro número entero positivo: "))

def producto(n, m):
    return n * m

print(producto(n, m))

"""
