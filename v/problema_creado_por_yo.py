"""tecnofast programa para mejorar la gestion en la bodega"""
#problema
"""ingresar guias de despacho    (crear lista donde se guarden esas guias de despacho)  y que el stock que valla saliendo
se valla descontando y mostrandonos y si pone (dia terminado ) se cierra el programa y muestra como quedo en stock

guias de despacho de   (las guias deben ser enumeradas con id_numero)
materiales
hormigon 
bidones con agua
"""
"""llegaron 2 camiones con hormigon 6 x camion 
llegaron materiales tales como : tornillos (1.000),madera 10x10(40),plancha volcanita (800)
llego en  el camion 40 bidones con agua"""

lista_materiales=[]
lista_guias_materiales=[]

lista_hormigon=[]
lista_guias_hormigon=[]

lista_guias_agua=[]
lista_agua=[]

while (True):
    guia_despacho=(input("que tipo de guia le llego :")).lower()
    
    if guia_despacho == "materiales":
        numero_de_guia=int(input("ignrese numero de guia:"))
        lista_guias_materiales.append(numero_de_guia)
        while (True):
            materiales=input("que materiales llegaron :")
            lista_materiales.append(materiales)
            print (lista_materiales)
            if materiales == "eso es todo":
                break
    if guia_despacho == "hormigon":    
         numero_de_guia=int(input("ignrese numero de guia:"))
         lista_guias_hormigon.append(numero_de_guia)
         while (True):
            hormigon=input("cuanto hormigon llego y sus medidas: ")
            lista_hormigon.append(hormigon)
            print (lista_hormigon)
            if  hormigon == "eso es todo":
                break
    if guia_despacho == "agua":    
        numero_de_guia=int(input("ignrese numero de guia:"))
        lista_guias_agua.append(numero_de_guia)
        while (True):
            agua=int(input("cuantos bidones con agua llegaron: "))
            lista_agua.append(agua)
            print (lista_agua)
            pregunta=(input("eso es todo ? :"))
            if  pregunta == "si":
                break
            else :
                continue
"""quero que el  usuario ingrese cuanto material/bidones/hormigon entrego en el dia y que se valla descontando"""
            