"""una ampolleta inteligente tiene 3 interruptores a b c 
las condiciones para que la ampolleta este encendida son

1. a debe estar encendido no importa el estado de b o c
2. b y c son iguales
3.b  esta encendido

si se cumple alguna de estas condiciones la ampolleta se enciende 
de lo contrario la ampolleta esta apagada
cree un programa que reciba los estados de a b c e indique el estado de la ampolleta"""

letraA=(input("como esta la ampolleta A? off/on:"))
letraB=(input("como esta la ampolleta B? off/on:"))
letraC=(input("como esta la ampolleta C? off/on:"))

if letraC== "on"and letraA==letraB=="off":
    print("apolleta apagada")
else:
    print("ampolleta encendida")
  
        
    