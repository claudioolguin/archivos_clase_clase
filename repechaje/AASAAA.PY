"""Escriba un codigo que:
    1) Determine que numeros estan duplicados en la lista rand_list✔️
    2) Logre hacer el punto '1' en 1 solo ciclo✔️
    3) Elimine los duplicados de la lista 'rand_list' (no se debe crear otra lista)
    4) En UNA SOLA REVISION (o ciclo) a la lista 'rand_list' (con los duplicados eliminados), ordene los numeros en una nueva lista 'order_list'

"""

guardar = set()
duplicados = set()
recorre = 0

import random
rand_list=[]
    
    
for i in range(50):
        rand_list.append(random.randint(0,20))
print (rand_list)
print(("-")*100)
#-------- NUMEROS DUPLICADOS EN UN SOLO CICLO ----------------------
while recorre < len(rand_list):
    num = rand_list[recorre]
    if num in guardar:
        duplicados.add(num)
        rand_list.pop(recorre)
    else:
        guardar.add(num)
        recorre += 1
order_list = sorted(rand_list)
#---------------------------------------------------------


print("Números duplicados:", duplicados)
print(("-")*100)
print("Lista original sin duplicados:", rand_list)
print(("-")*100)
print("Lista ordenada:", order_list)


[10, 6, 2, 8, 9, 15, 4, 2, 3, 0, 13, 14, 20, 5, 19, 18, 3, 2, 1, 7, 17, 16, 4, 6, 19, 19, 7,
 20, 20, 3, 6, 7, 18, 7, 9, 18, 19, 5, 5, 15, 8, 8, 20, 12, 18, 15, 10, 9, 1, 11]