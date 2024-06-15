"""
Dada una secuencia de caracteres, obtener dicha secuencia invertida
"""

def invertir_secuencia(secuencia):
    """
    Invierte la secuencia de caracteres
    """
    return secuencia[::-1]  

def main():
    secuencia = input("Ingrese una secuencia de caracteres: ")
    print(f"La secuencia invertida es: {invertir_secuencia(secuencia)}")

if __name__ == "__main__":
    main()

# Ingrese una secuencia de caracteres: Hola Mundo
# La secuencia invertida es: odnuM aloH
