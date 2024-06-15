"""
Desarrollar una función que permita convertir un número romano en un número decimal.
"""

def romano_a_decimal(n):
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    # Verificar si todos los caracteres en n son válidos
    for char in n:
        if char not in romanos:
            raise ValueError(f"Carácter no válido en el número romano: {char}")
    
    decimal = 0
    for i in range(len(n)):
        if i > 0 and romanos[n[i]] > romanos[n[i-1]]:
            decimal += romanos[n[i]] - 2 * romanos[n[i-1]]
        else:
            decimal += romanos[n[i]]
    return decimal

n = input("Ingrese un número romano: ").upper()
try:
    resultado = romano_a_decimal(n)
    print(f"El valor decimal de {n} es {resultado}")
except ValueError as e:
    print(e)



