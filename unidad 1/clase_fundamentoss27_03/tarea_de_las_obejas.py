peso=int(input("ingrese el peso de la oveja:"))
color=input("ingrese el color de la oveja:")
tamaño=int(input("ingrese el tamaño de la oveja:"))

if peso >= 60 :
    precio = 1500
else :
    precio = 1000
if color == "negro":
    precio_color= 100
if color == "morado":
    precio_color =200
if color == "ocre":
    precio_color= 150
    precio_tamaño= 1.5* tamaño
if tamaño > 100:
    precio_tamaño=1000

precio_total= precio_tamaño + precio_color + precio
    
print ("el precio de la oveja es ",precio,"el precio de la oveja es ",precio_color,"el precio de la oveja es ",precio_tamaño) 
print ("el precio total es de ",precio_total)              
