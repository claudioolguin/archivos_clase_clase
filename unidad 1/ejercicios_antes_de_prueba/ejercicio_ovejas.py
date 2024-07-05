color = str(input("Ingrese color: "))
peso = float(input("Ingrese el peso: "))
tamano = float(input("Ingrese tamaño: "))
precio = 0

#peso
if (peso >= 60):
    precio += 1500
else:
    precio += 1000

#color
if (color == "negro"):
    precio += 100

if (color == "morado"):
    precio += 200


if (color == "ocre"):
    precio += 150

#tamaño
if (tamano > 60):

    precio_por_tamano = tamano * 1.5
    if (precio_por_tamano >= 300):
        precio += 300
    else:
        precio += precio_por_tamano
    
    if (tamano > 100):
        precio += 1000

print("El precio es: $%.0f" % (precio))