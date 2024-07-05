"""cree un programa que calcule el area de figuras geometricas. 
el usuario ingresa la figura a calcular y el programa muestra el area de la figura 
laas figuras son:
H = altura A = altura
R = radio
b = base 
D = diametro
triangulpo : b + h * 1/2
rectangulo: a * b
circulo : r * r * pi (3.14)

el programa debe detectar areas no validas"""
figura= input("elige la figura:")
if figura == "triangulo ":
    b = int(input("ingresa la base del triangulo: "))
    a = int(input("ingresa la altura del triangulo: "))
    triangulo= a * b * 1/2
    print (triangulo)
elif figura == "rectangulo" :
    b = int(input("ingresa la base del rectangulo: "))
    a = int(input("ingresa la altura del rectangulo: "))
    rectangulo= a * b
    print ("el area del rectangulo es : ", rectangulo)
elif figura == "circulo":
    r = int(input("ingrese el radio del circulo : "))
    d = int(input("ingresa el diametro del circulo: "))
    circulo= r * d * 3,14
    print (circulo)


