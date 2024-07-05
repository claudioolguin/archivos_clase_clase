"""cree un programa que reciba numeros y los guarde en una lista 
si el usuario ingresa  salir , se detiene el ingreso

luego debe mostrar :
el numero mas grande de la lista 
el numero mas pequeño de la lista 
el promedio 
la cantidad de numeros"""
lista=[]

while (True) :
    numero=(input("ingrese numeros :"))
    if (numero == "salir"):
        break
    if (numero.isdigit()):
        lista.append(int(numero))
    else:
        print("SOLO NUMERO POR FAVOR")
#--------------------------------------------------------------------        
numero_mayor = 0
suma= 0
numero_menor = 0
largo_numero=len(lista)     

for i in range (largo_numero):
    if (i==0):
        numero_mayor=lista[i]
        numero_menor=lista[i]
    if (lista [i] > numero_mayor):
        numero_mayor= lista[i]
            
    if  (lista[i] < numero_menor):
        numero_menor =lista [i]
    
    suma += lista[i]

print ("numero mayor :",numero_mayor)
print ("numero menor :",numero_menor)                    
print ("promedio",suma/largo_numero)  
    

print ("cantidad de numeros :",largo_numero)
print (lista)
print ("la suma es de :",suma)    