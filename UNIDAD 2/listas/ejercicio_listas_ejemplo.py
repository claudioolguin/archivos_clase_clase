"""
El usuario ingresa un numero y se debe crear una lista del tamaño indicado y rellena con numeros enteros positivos pares.
"""
pares = []
numero = int(input(">> "))
contador = 0

num = 0
while (contador != numero):
    contador += 1
    num += 2
    pares.append(num)
print(pares)