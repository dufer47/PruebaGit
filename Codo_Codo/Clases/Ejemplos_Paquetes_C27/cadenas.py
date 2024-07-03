# Este es un modulo que contiene funciones para cadenas

# Devuelve una cadena invertida:
def invertir_cadena(cadena):
    cadena_invertida=""
    for letra in cadena:
        cadena_invertida=letra+cadena_invertida
    return cadena_invertida

# Devuelve "Hola Mundo"
def hola_mundo():
    return "Hola Mundo"

print(invertir_cadena("pepe"))