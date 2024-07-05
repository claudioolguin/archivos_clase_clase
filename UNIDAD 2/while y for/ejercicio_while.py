"""programa para invitar a amigos a una fiesta pregunta si quiere invitar a mas amigos si pone que no se detiene"""

contadora=0
while (True):
    can_invitados=input("a que amigo quieres invitar:").lower 
    contadora += 1
   
    salir= input("quiere añadir a otra persona ? <si>  <no>:")
    if (salir.lower()=="no"):
        break
print ("hay",contadora,"invitados")    
    