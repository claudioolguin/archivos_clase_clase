"""
Escriba un codigo que:
    1) Determine que numeros estan duplicados en la lista rand_list
    2) Logre hacer el punto '1' en 1 solo ciclo
    3) Elimine los duplicados de la lista 'rand_list' (no se debe crear otra lista)
    4) En UNA SOLA REVISION (o ciclo) a la lista 'rand_list' (con los duplicados eliminados), ordene los numeros en una nueva lista 'order_list'

"""

import random
rand_list=[]
for i in range(50):
    rand_list.append(random.randint(0,20))
print("LISTA ORIGINAL -->",rand_list)
print(("-")*100)



guardar = set()
duplicados = set()
i = 0
while i < len(rand_list):
    if rand_list[i] in guardar:
        duplicados.add(rand_list[i])
        rand_list.pop(i)  # Eliminamos el elemento duplicado
    else:
        guardar.add(rand_list[i])
        i += 1  # Solo incrementamos el índice si no eliminamos el elemento

print("duplicados:", rand_list)
print(("-")*100)
print("Números duplicados:", duplicados)


[0, 7, 2, 0, 5, 18, 14, 18, 20, 8, 0, 9, 1, 19, 16, 16, 13, 20, 17, 
 18, 14, 8, 12, 0, 19, 19, 5, 4, 8, 18, 10, 20, 11,
 14, 14, 20, 2, 11, 14, 12, 6, 4, 17, 3, 2, 8, 20, 19, 12, 0]