"""en paislandia todos pagan impuesto 
cree un programa para calcular impuestos
el programa recibe la edad
y la cantidad de ingresos del año (con decimal )

luego se calcula el impuesto segun la formula i = (5 + edad/3)
muestre el impuesto y el dinero luego de que le cobren el impuesto
d -> 100%  = tu dinero es el 100%
di= d * (1-i)"""

edad=(input("ingrese su edad:"))
ingxmes= float(input("ingrese su sueldo mensual :"))
impuesto= 5 + (edad/3)
resultado = ingxmes * (1- impuesto/100)
print ("el impuestoi es:",impuesto,"%")
print ("$",resultado)