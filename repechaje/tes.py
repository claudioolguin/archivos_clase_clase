"""Escriba un codigo que:
    1) Determine que numeros estan duplicados en la lista rand_list
    2) Logre hacer el punto '1' en 1 solo ciclo
    3) Elimine los duplicados de la lista 'rand_list' (no se debe crear otra lista)
    4) En UNA SOLA REVISION (o ciclo) a la lista 'rand_list' (con los duplicados eliminados), ordene los numeros en una nueva lista 'order_list'

"""
import random


rand_list = [random.randint(0, 20) for _ in range(50)]


guardar = set()
duplicados = set()


for num in rand_list:
    if num in guardar:
        duplicados.add(num)
    else:
        guardar.add(num)


i = 0
while i < len(rand_list):
    if rand_list[i] in duplicados:
        rand_list.pop(i)
    else:
        i += 1


random.shuffle(rand_list)


order_list = sorted(rand_list)

print("LISTA ORGINAL",rand_list)
print(("-")*100)
print(f"Números duplicados: {duplicados}")
print(f"Lista original sin duplicados (rand_list): {rand_list}")
print(f"Lista ordenada sin duplicados (order_list): {order_list}")