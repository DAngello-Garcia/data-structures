# Los elementos de una lista se almacenan en posiciones de memoria contiguas
list_1 = [1, 4, 9, 16, 25]

# Acceder a valores
print(list_1[0])

# Modificar valores
list_1[2] = 18

# Eliminar valores
del list_1[1]

# Método len() para conocer el tamaño de una lista
print(len(list_1))

# Recorrer una lista
for i in range(len(list_1)):
    print(list_1[i])

# Agregar elementos al final de una lista
list_1.append('nuevo elemento')

# List comprehension o comprensión de listas: crear una nueva lista a partir de una ya existente
list_2 = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = [i for i in list_2 if 'a' in i]
print(new_list)