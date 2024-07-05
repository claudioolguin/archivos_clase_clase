"""CREE UN PROGRAMA QUE  RECIBA 3 ELEMNTOS :
DINERO A DEPOSITAR
INTERES MENSUAL
CANTIDAD DE MESES DEL DEPOSITO

EL PROGRAMA MUESTRA EL DINERO LUEGO DE QUE PASARON LOS MESES

DINERO_PORX_MES = DINERO_ACTUAL * (1+INTERESES)"""

dinero=int(input("ingrese el dinero a depositar :"))
interes_mensual=int(input("ingrese el interes deseado :"))
cantidad_meses=int(input("ingrese cantidad meses :"))

for mes in range (cantidad_meses):
    dinero = dinero * (1+interes_mensual)
    
print ("ahora tiene :",int ())
 
