# Solicitar al usuario que ingrese un número como una cadena
numero = input("Por favor ingresa un número como cadena: ")

# Convertir el número a string y obtener su longitud
longitud = len(numero)

# Inicializar la cadena resultante
resultado = ""

# Iterar sobre el número de atrás hacia adelante
for i in range(longitud - 1, -1, -1):
    # Agregar cada dígito al resultado
    resultado = numero[i] + resultado
    # Agregar una coma después de cada tercer dígito (excepto para el primer dígito)
    if (longitud - i) % 3 == 0 and i != 0:
        resultado = "," + resultado

# Imprimir el resultado
print("El número con la separación correspondiente es:", resultado)