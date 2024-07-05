#encontrar letra n
#cualquier palabra se empiza a contar desde el 0  ej. hola  h = 0  O = 1   L = 2   A = 3
palabra=input("ingrese palabra :")
N=int(input("que letra de la palabra quere encontrar"))
cont = 0 
letter = ""
for letra in palabra :
    if (cont == N):
        letter = letra
        break
    cont +=1
print (letter)
