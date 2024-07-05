"""El consejo estudiantil le pide que cree un programa para elegir a su nuevo presidente.

La lista es:

Pepito, Pablito y Juanita

El programa muestra la lista de candidatos y el usuario ingresa el nombre del candidato por el cual votar. El programa debe detectar que el nombre ingresado sea valido, sin embargo, puede ser ingresado todo en minusculas o mayusculas.

EJ:

>> Votar por: Pepito | Pablito | Juanita

>> Input: pepito

>> Voto Valido"""

voto=input("votar por pepito pablito juanita : ").lower()

if voto in ("pepito pablito juanita"):
    print ("voto valido")
else:
    print("voto invalido")    