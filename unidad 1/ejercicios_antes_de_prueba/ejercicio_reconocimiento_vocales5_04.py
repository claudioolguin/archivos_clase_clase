"""cree un programa que reciba un caracter e indique si es o no es una vocal
el programa solo puede recibir 1 caracter a la vez . si recibe mas de un caracter . debe mostrar eorror"""

caracter=str(input("escriba una letra:"))

if caracter == "a" or caracter== "e" or caracter=="i"or caracter=="o" or caracter == "u"  :
    print("es una vocal")
else:
    print("error")