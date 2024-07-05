"""Escriba el código para el juego "cadena de palabras"

El programa debe recibir strings, debe (asegurar que no tengan numero)

El jugador solo puede ingresar un string que empiece con la ultima letra del ultimo string, de lo contrario, el jugador pierde.

Considere que la primera palabra es "juego"."""

primer_ciclo= True

while (True):
    palabra =input("ingresar cadena de texto:").lower()
    if (palabra in "1234567890"):
        print ("solo texto")
        continue
    if (primer_ciclo):
        primer_ciclo= False
    else:
        if (palabra[0]!= ultima_letra):
            print("mal")
            break
    for i in range(len(palabra)):
        ultima_letra=palabra[i]        