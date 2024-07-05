"""el usuario quiere una disco llamada 
NOT PEPITOS
la disco tiene 2 reglas
-solo mayores de edad
-no pueden entrar los pepitos"""

edad= int(input("ingrese edad:"))
nombre= input("nombre:")

if ((edad >=18 )and (nombre != "pepito")):
    print("disco disco fiesta")
else:
    print ("noot disco")
