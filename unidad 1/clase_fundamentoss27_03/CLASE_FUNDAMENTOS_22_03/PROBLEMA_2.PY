"""En Paislandia es epoca de pagar impuestos, pero hay reglas para pagar impuestos.
1. Ser mayor de edad y menor de 60 años
2. Tener ingresos sobre los ♠500

Y ademas, el impuesto se asigna segun ingreso:
mayor a 500 y hasta 1000 = 5
1001 hasta 3000 = 8%
3001 en adelante = 12%

BONUS: Nadie puede pagar más de ♠3000 de impuesto
BONUS 2: Quienes tengan menos de 500 de ingreso, reciben ♠(edad*10) de vuelta
"""
edad=int(input("ingrese su edad:"))
ingreso=int(input("ingrese su sueldo:"))

if edad >18 and edad <60 :
    if ingreso >500 and ingreso <1000:
        impuesto=ingreso * 0.05
        print ("tu impuesto es de :",impuesto)
    if ingreso >1001 and ingreso <3000:
         impuesto= ingreso * 0.08
         print ("tu impuesto es de :",impuesto)    
    if  ingreso >3001 :
         impuesto= ingreso * 0.12
         print ("tu impuesto es de :",impuesto)  
elif ingreso < 500 :
    sueldorecalculado = edad*10
    print ("su sueldo recalculado es de :",sueldorecalculado)
    sueldorecalculado* 0.05 
    print(sueldorecalculado) 
 
    