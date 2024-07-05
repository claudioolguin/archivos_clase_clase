"""
Escriba un codigo que:
    1) Determine que numeros estan duplicados en la lista rand_list
    2) Logre hacer el punto '1' en 1 solo ciclo
    3) Elimine los duplicados de la lista 'rand_list' (no se debe crear otra lista)
    4) En UNA SOLA REVISION (o ciclo) a la lista 'rand_list' (con los duplicados eliminados), 
    ordene los numeros en una nueva lista 'order_list'

"""

import random

# Generamos la lista rand_list con números aleatorios entre 0 y 20
random_list = [random.randint(0, 20) for _ in range(50)]
print("Lista original:", random_list)
print(("-")*100)


# Inicializamos sets para rastrear elementos únicos y duplicados
seen = set()
duplicates = set()

# Recorremos la lista para encontrar duplicados y eliminar los duplicados en el mismo ciclo
i = 0
while i < len(random_list):
    if random_list[i] in seen:
        duplicates.add(random_list[i])
        random_list.pop(i)  # Eliminamos el elemento duplicado
    else:
        seen.add(random_list[i])
        i += 1  # Solo incrementamos el índice si no eliminamos el elemento

print("Números duplicados:", duplicates)
print(("-")*100)
print("Lista sin duplicados:", random_list)
print(("-")*100)
# Ordenamos los elementos en una nueva lista order_list en una sola revisión
order_list = []
while random_list:
    min_val = min(random_list)
    order_list.append(min_val)
    random_list.remove(min_val)

print("Lista ordenada:", order_list)
