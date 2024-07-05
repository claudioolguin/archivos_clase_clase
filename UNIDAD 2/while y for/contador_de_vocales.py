"""el usuario ingresa una palabra cuente cuantas vocales hay en la palabra"""
contador=0
palabra=input ("  ingrese letra:  ").lower()
for letra in palabra :
    if (letra in "aeiou"):
        contador +=1 
print ("vocales:",contador)