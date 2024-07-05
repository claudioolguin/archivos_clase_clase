"""Cree un programa que reciba un dia de la semana como texto, 
la edad del usuario y el dinero que trae e indique Donde puede ir de fiesta.

Bellavista: Mayor de Edad, cualquier dia de la semana, 1000 o más

Barrio Italia: Mayor de Edad, jueves a domingo, 4000 o más

Valparaiso: Mayor de Edad, fin de semana, cualquier cantidad de dinero

AfterOfice: 25 o más, jueves a sabado, 6000 o más

HappyLand: 13 o más, toda la semana, 1000 o más"""

dia_semana=input("ingrese dia de salida:")
edad=int(input("ingrese su edad :"))
dinero=int(input("cuanta plata teni:"))

if edad >=18 and dinero >=1000:
    print("puede ir a bellavista")
    
if edad >=18 and dia_semana in ("jueves viernes sabado domingo") and dinero >=4000:
    print ("puede ir a barrio italia")
    
if edad >=18 and dia_semana in ("sabado domingo"):
   print("puede ir a valparaiso")
   
if edad >=25 and dia_semana in ("jueves viernes sabado") and dinero >=6000:
    print("puede ir a afterofice") 

if edad >=13 and dinero >=1000:
    print("puede ir al happyland")    
else :
    print("no podi salir ")    