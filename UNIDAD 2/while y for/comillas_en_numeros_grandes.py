"""cree un programa que reciba un numero  (como string) y coloque la separacion 
segun corresponda. usando  " ,"  """
"""ej.

>>1234 = 1,234
>>123456 = 123,456
>> 1234567 = 1,234,567"""

"""def separar_numeros(numero):
    # Convertir el número a string y obtener su longitud
    numero = str(numero)
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
    
    return resultado

# Ejemplos de uso
numero1 = "1234"
numero2 = "123456"
numero3 = "1234567"

print(separar_numeros(numero1))  # Output: 1,234
print(separar_numeros(numero2))  # Output: 123,456
print(separar_numeros(numero3))  # Output: 1,234,567"""

cadena =input("ingrese su nombre :")
longitud_cadena = len(cadena)
print("La longitud de la cadena es:", longitud_cadena)  # Output: 10