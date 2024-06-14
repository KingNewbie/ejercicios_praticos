"""
Implementar una función que calcule la suma de todos los números enteros comprendidos
entre cero y un número entero positivo dado.
"""
n= int(input("Ingrese un número entero positivo: "))

def suma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + suma_recursiva(n - 1)
    
print(suma_recursiva(n)) # 15


"""
Explicación de la Implementación Mejorada segun CHATGPT:

    1.- Entrada del Usuario: Se solicita al usuario que ingrese un número entero positivo.
    2.- Función de Suma Directa: Utiliza la fórmula matemática para calcular la suma de los
      primeros nn números enteros.
    3.- Impresión del Resultado: Muestra el resultado al usuario.

Esta implementación es mucho más eficiente y rápida, especialmente para números grandes, ya que no implica recursión ni bucles.

def suma_directa(n):
    return n * (n + 1) // 2

print(suma_directa(n))  # 15
"""