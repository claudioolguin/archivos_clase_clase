"""crear una funcion que reciba string y devuelva un diccionario que contenga la frecuencia
(ANTIDAD DE VECES QUE SE REPITE LAS LETRAS DENTRO DEL DICCIONARIO)
"""
def contarletras(palabra:str) -> str:
    
    dictfrec={}
    for letra in palabra :
            if (letra in dictfrec.keys()):# aqui se guarda la letra en el diccionario
                dictfrec[letra]+=1
            else:x 
                dictfrec[letra]=1
    return  dictfrec

#------------------------------------------------------------------------------------------------------------           

palabra=contarletras(input("ingrese texto:"))
print(palabra)            
        
        


