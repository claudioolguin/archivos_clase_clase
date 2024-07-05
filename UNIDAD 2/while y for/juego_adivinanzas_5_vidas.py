"""
Crea un programa donde tendrás la variable numero_secreto, la cual toma un valor aleatorio entre 1 y 20. Después pide a tu usuario que indique un número para intentar adivinarlo: en caso de acertar indícale cual era el número secreto y cuantos intentos le tomó; en caso contrario indícale si el número ingresado es mayor o menor al número secreto.
El usuario tiene 5 'vidas'. Cada vez que falla pierde una vida. Si acierta, puede preguntar por otro numero. Pero las vidas no se reinician.
El usuario puede escribir 'salir' para dejar de jugar o cuando pierde todas las vidas.

Al final se muestra el puntaje.

Se suma 1 punto por cada adivinanza correcta.
"""

import random



intentos = 0

vidas = 5
puntaje = 0

while (vidas > 0):
    numero_secreto = random.randint(1,20)

    while(True):
        print(numero_secreto)
        print("Adivina el numero!")
        adivinanza = input(">> ")
        if (adivinanza.lower() == "salir"):
            break
        if (adivinanza.isdigit()):
            adivinanza = int(adivinanza)
        else:
            print("Solo numeros o 'salir'")
            continue

        if (adivinanza == numero_secreto):
            print("El numero era:",numero_secreto,"!!!")
            print("Tomo",intentos,"intentos")
            puntaje += 1
            break
        else:
            print("ERROR")
            if (numero_secreto > adivinanza):
                print("El numero es más grande")
            if (numero_secreto < adivinanza):
                print("El numero es menor")
            print("Pierde una vida")
            vidas -= 1
            if (vidas <= 0):
                break
            continue

    print("Puntaje:",puntaje)
    print("Vidas restantes:",vidas)
    
print()
print("GAME OVER")
print("Puntaje:",puntaje)