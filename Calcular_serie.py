"""
Desarrollar un algoritmo que permita calcular la siguiente serie:
h(n) = 1+1/2+1/3+...+1/n
"""

def calcular_serie(n):
    suma = 0
    for i in range(1, n+1):
        suma += 1/i
    return suma

n = int(input("Ingrese el valor de n: "))
print(f"El resultado de la serie es: {calcular_serie(n)}")

# Ejecutar el archivo Calcular_serie.py
# Ingresar el valor de n
# Obtener el resultado de la serie
# Fin
