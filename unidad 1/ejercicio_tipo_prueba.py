"""Se le ha encargado crear un programa que permita calcular el total de una venta de electrodomésticos
Para esto, el usuario ingresa el nombre del producto que desea comprar
La cantidad de dinero que tiene el usuario.
Luego ingresa el precio del producto (Sin IVA).

El programa calcula el IVA correspondiente y muestra por pantalla el precio total (con IVA) y el (IVA) . El IVA es 19%
Luego el programa pregunta la edad del usuario y se ajusta según la edad

18 o menos -- 5% de descuento
19 a 50 -- precio normal
51 a 70 -- 5% de descuento
71 o más -- 10% de descuento

Luego el programa muestra el descuento y el precio correspondiente y pregunta por el método de pago

Efectivo -- precio normal
Debito -- 5% extra
Crédito -- 8% extra
Cheque -- 6% de descuento

Una vez finalizado esto se muestra el precio total del producto.
E indica si es posible que el usuario pueda comprarlo con el dinero ingresado.
Luego el programa finaliza.
"""
producto = input("ingrese el producto que desea comprar:") 
dinero_en_bolsillo = int(input("cuanto dinero tienes:"))
calculador_precios=int(input("ingrese el precio del producto cual desea el detalle:"))
iva=calculador_precios *0.19
print (("precio con iva:"),calculador_precios)
print (("su iva es de :"),iva)
print (("su precio sin iva es de :"),calculador_precios-(iva))
precio_producto=int(input("ingrese el precio del producto: ")) 
edad = int(input("cual es tu edad:"))

if edad <=18 :
    descuento = precio_producto * 0.05
    print (("se le aplica un descuento de:"), descuento) 
    precio_final=  precio_producto - descuento 
    print (("su precio final es de :"),precio_final)
    if edad >=19 and edad <=50 :
        print ("no se le aplica descuento")
        print (("su precio final es de :"),precio_producto)
        if edad >=51 and edad <=70 :
            descuento = precio_producto * 0.05
            print (("se le aplica un descuento de:"), descuento) 
            precio_final=  precio_producto - descuento 
            print (("su precio final es de :"),precio_final)
            if edad >=71 :
                descuento = precio_producto * 0.1
                print (("se le aplica un descuento de:"),descuento) 
                precio_final=  precio_producto - descuento
                print (("su precio final es de :"),precio_final)
                metodo_pago=input ("cual es su metodo de pago:")
                if metodo_pago == "efectivo" :
                    print ("no se le aplica descuento")
                    print (("su precio final es de :"),precio_producto)
                    if metodo_pago == "debito" :
                        intereses = precio_producto * 0.05
                        print (("se le aplica un interes de: "),intereses)
                        precio_final = precio_producto + intereses 
                        print (("su precio final es de:"),precio_final)
                        if metodo_pago == "credito":
                         intereses = precio_producto * 0.08
                         print (("se le aplica un interes de: "),intereses)
                         precio_final = precio_producto + intereses 
                         print (("su precio final es de:"),precio_final)
                        if metodo_pago == "cheque":
                              descuento = precio_producto * 0.6
                              print (("se le aplica un descuento de:"),descuento) 
                              precio_final=  precio_producto - descuento
                              print (("su precio final es de :"),precio_final)
                              