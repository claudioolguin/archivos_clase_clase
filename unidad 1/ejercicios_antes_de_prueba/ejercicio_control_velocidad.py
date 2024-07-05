velocidad_registrada=int(input("velocidad registrada:"))
limite_velocidad=int(input("ingrese el limite de velocidad deseado:"))
exceso=(velocidad_registrada-limite_velocidad)/limite_velocidad*100
x=round (exceso)

print (exceso)
print (("se excedio un :"),x,"%")

if x <=15:
    multa=velocidad_registrada*10
    print ("su multa sera de :$",multa)
    if  x >=16 and x <=25:
        multa=velocidad_registrada*40
        print ("su multa sera de: $",multa)
        if x >=26 and x <=50 :
            multa=(velocidad_registrada*15)+4000
            print ("su multa es de $",multa)
            if x >50 :
                multa=(velocidad_registrada*30)+10000
            print ("su multa es de: $",multa)
                    
                
                
    
        
        