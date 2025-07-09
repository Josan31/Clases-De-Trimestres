print("------> TUPLAS <------")

# Las tuplas se declara muy parecida a una lista, con la unica diferencia que utiliza paréntesis en lugar de corchetes. Ejemplo: 

mi_tupla = (1,2,3,4,5)
otra_tupla = ("hola", "como", "estas", "?")
print(mi_tupla, otra_tupla)

# Al igual que las listas, las tuplas no tienen la restricción sobre el tipo de datos de los items. 
# Podemos tener una tupla que contenga números, variables, strings, o incluso otras listas. 
# otra cosa en que las tuplas se parecen a las listas, es que ambos casos se puede concatenar. 
# NOTA: EN LAS TUPLAS NO SE PUEDE USAR EL MÉTODO APPEND

print("[1]\n")

# Las LISTAS son MUTABLES (se pueden cambiar), pero las TUPLAS son INMUTABLES (no se pueden modificar)

mi_tupla = (1, 2, 3, 4, 5)

# Esto generará error porque no se puede modificar una tupla
mi_tupla[2] = 5

print("------------------------------------------------")

print("[2]\n")

# len() permite saber cuántos elementos tiene una tupla

num = (1, 2, 3, 4)
op = len(num)
print(op)

print("------------------------------------------------")

print("[3]\n")

# count() cuenta cuántas veces aparece un valor en la tupla

numeros = (1, 2, 1, 3, 1, 4, 1)
op2 = numeros.count(1)
print(op2)

print("------------------------------------------------")

print("[4]\n")

# index() busca la posición (índice) del primer valor que coincida

numero = (1, 2, 1, 3, 1, 4, 1, 5)
op3 = numero.index(5)
print(op3)

print("------------------------------------------------")

print("[5]\n")

# Convertir una tupla a lista con list()

mi_tupla1 = (1, 2, 3)
mi_lista1 = list(mi_tupla1)
print(mi_lista1)


print("------------------------------------------------")

print("[6]\n")

# Convertir una lista a tupla con tuple()
mi_lista2 = [4, 5, 6]
mi_tupla = tuple(mi_lista2)
print(mi_tupla)

print("------------------------------------------------")

# 1. Se crea una tupla con 5 números
Tupla = (1, 2, 3, 4, 5)
print(Tupla)

# 2. Se accede al segundo elemento (índice 1)
print(Tupla[1])

# 3. Se imprime la cantidad de elementos en la tupla
print(len(Tupla))

# 4. Se obtiene el índice donde está el número 4
print(Tupla.index(4))

# 5. Se cuenta cuántas veces aparece el número 2
print(Tupla.count(2))

# 6. Se crea una tupla con diferentes tipos de datos
Tupla2 = ("Hola", 100, 12.4, 0.001)
print(Tupla2)

# 7. Se crea otra tupla que incluye un valor de Tupla2
op3 = (12, 3, Tupla2[0], 6, 7)

# Se imprime el tercer elemento de op3 (que es "Hola")
print(op3[2])

print("------------------- EJERCICIOS DE TUPLAS -------------------")

print("\n[1]")

# Se imprime el primer y último valor de la tupla
Tuple_entero = (1, 2, 3, 4, 5)
print(Tuple_entero[0], Tuple_entero[4])

print("\n[2]")

# Lista de decimales. Se imprime el primer y último valor
Tuple_entero2 = [1.1, 2.05, 3.12, 4.4, 5.12]
print(Tuple_entero2[0], Tuple_entero2[4])

print("\n[3]")

# Desempaquetado de tupla en 3 variables
Tuple1 = ("Hello", "World", "One")
vab1, vab2, vab3 = Tuple1
print(vab1, vab2, vab3)

print("\n[4]")

# Suma de todos los valores de una lista
lista1 = [1, 2, 3, 4, 5]
op3 = lista1[0] + lista1[1] + lista1[2] + lista1[3] + lista1[4]
print(f"El resultado de la suma de todos los números es: {op3}")

print("\n[5]")

# Cálculo del promedio de una tupla de decimales
tuple2 = (1.01, 16.02, 2.03, 23.04, 7.05)
op4 = (tuple2[0] + tuple2[1] + tuple2[2] + tuple2[3] + tuple2[4]) / 5
print(f"El promedio de los números de la tuple es de: {op4}")

print("\n[6]")

# Desempaquetado de lista en variables
lista2 = [1, 2, 3, 4]
va1, va2, va3, va4 = lista2
print(va1, va2, va3, va4)

print("\n[7]")

# Multiplicación entre los valores de una tupla
tuple3 = (34, 78)
op7 = tuple3[0] * tuple3[1]
print(f"El resultado de la multiplicación es de: {op7}")

print("\n[8]")

# Se añade un número a la lista
lista3 = [1, 2, 3]
agregar = lista3.append(16)

# Se imprime el primer y el nuevo último valor
print(lista3[0], lista3[3])

print("\n[9]")

# Suma de los dos primeros elementos de una tupla
tuple4 = (12, 26, 23, 34)
op8 = tuple4[0] + tuple4[1]
print(f"La suma entre los dos primeros números es de: {op8}")

print("\n[10]")

# División entre el primer y el último número de una lista
lista4 = [20, 2, 3, 4, 5]
print(lista4[0] / lista4[4])




