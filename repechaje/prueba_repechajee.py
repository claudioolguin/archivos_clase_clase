import random
rand_list=[]
    
    
# Generamos la lista rand_list con números aleatorios entre 0 y 20
for i in range(50):
        rand_list.append(random.randint(0,20))
print(("-")*100)        
print (rand_list)
print(("-")*100)



#sets para rastrear elementos únicos y duplicados
ordenado = set()
duplicado = set()

# Recorre la lista para encontrar duplicados y eliminar los duplicados en el mismo ciclo
var = 0
while var < len(rand_list):
    if rand_list[var] in ordenado:
        duplicado.add(rand_list[var])
        rand_list.pop(var)  # Eliminamos el elemento duplicado
    else:
        ordenado.add(rand_list[var])
        var += 1  # Solo incrementamos el índice si no eliminamos el elemento

# Convierte el set de duplicados a una lista y la ordenamos
duplicado = sorted(list(duplicado))

# Ordena la lista original sin duplicados
rand_list.sort()

print("Números duplicados:", duplicado)
print(("-")*100)
print("Lista sin duplicados y ordenada:", rand_list)
print(("-")*100)




