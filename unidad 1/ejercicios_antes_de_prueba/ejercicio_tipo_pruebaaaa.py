
color_manzana=input("ingrese color de manzana :").lower()
peso=int(input("ingrese el peso en gramos:"))
radio=int(input("ingrese el radio en centimetro:"))
densidad=int(input("ingrese la densidad por milimetrros:"))
cantidad_gusanos=int(input("ingrese cantidad de gusanos:"))

if color_manzana =="verde"and peso>=12 and densidad<=15 and cantidad_gusanos == 0 :
    print ("puede ser recogida")
else:
     print("no puede ser recogida") 
if color_manzana == "roja"  and radio <=13 and cantidad_gusanos == 0 and densidad >=10 :
     print ("puede ser recogida")
else:
    print("no puede ser recogida") 
if color_manzana =="morada" and peso <=14 and radio ==16 and densidad >=12 and cantidad_gusanos ==0:
      print ("puede ser recogida")
else:
    print("no puede ser recogida")     