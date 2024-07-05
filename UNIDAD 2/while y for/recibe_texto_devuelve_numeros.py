"""programa que recibe texto + numero y devuelve numeros y los suma"""

"""text = input("ingrese texto + numeros :")
texto=""
for i in text:
    if (i in "1234567890") :
        texto += i 
        print(i)"""


numero = " "
suma= 0         
palabra = input("<<")
for caracter in palabra :
    if (caracter.isdigit()):
        numero += caracter 
        suma += int(caracter)      
print (numero,"=",suma)
   