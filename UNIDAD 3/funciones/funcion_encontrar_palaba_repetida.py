
def frecuencia_palabra (palabra:str,texto:str) ->int:
    contador=0
    lista_palabras=texto.split(" ")#split divide string
    for elemennto in lista_palabras :
        if(palabra == elemennto):
            contador +=1
    return contador

print(frecuencia_palabra(input("palabra: "),(input("texto: "))))        
