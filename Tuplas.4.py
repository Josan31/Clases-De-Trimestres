# # print("------ TUPLAS  Y LISTAS ------")
# # Las tuplas se declara muy parecida a una lista, con la unica diferencia que utiliza paréntesis en lugar de corchetes. Ejemplo: 

# mi_tupla = (1,2,3,4,5)
# otra_tupla = ("hola", "como", "estas", "?")
# print(mi_tupla, otra_tupla)

# # Al igual que las listas, las tuplas no tienen la restricción sobre el tipo de datos de los items. Podemos tener una tupla que contenga números, variables, strings, o incluso otras listas. otra cosa en que las tuplas se parecen a las listas, es que ambos casos se puede concatenar. NOTA: EN LAS TUPLAS NO SE PUEDE USAR EL MÉTODO APPEND

# print("------------------------------------------------")

# # Las LISTAS SON MUTABLES, en cambio las TUPLAS SON INMUTABLES
# mi_tupla = (1,2,3,4,5)
# mi_tupla[2] = 5

# print("------------------------------------------------")

# # Las tuplas pueden usar la función LEN
# num = (1,2,3,4)
# op = len(num)
# print(op)

# print("------------------------------------------------")

# # Las tuplas pueden usar la función COUNT
# numeros = (1,2,1,3,1,4,1)
# # Nos dice cuantas veces se repite un número o dato.
# op2 = numeros.count(1)
# print(op2)

# print("------------------------------------------------")

# # Las tuplas pueden utlizar la función INDEX
# numero = (1,2,1,3,1,4,1,5)
# op3 = numero.index(5)
# print(op3)

# print("------------------------------------------------")

# # Para convertir una tupla a lista usamos la función LIST
# mi_tupla1 = (1,2,3)
# mi_lista1 = list(mi_tupla1)
# print(mi_lista1)

# print("------------------------------------------------")

# # Para convertir una lista a tupla usamos la función TUPLE
# mi_lista2 = [4,5,6]
# mi_tupla = tuple(mi_lista2)
# print(mi_tupla)

# print("------------------------------------------------")

# # 1
# Tupla = (1,2,3,4,5)
# print(Tupla)

# # 2
# print(Tupla[1])

# # 3
# print(len(Tupla))

# # 4 
# print(Tupla.index(4))

# # 5
# print(Tupla.count(2))

# # 6 
# Tupla2 = ("Hola", 100, 12.4, 0.001)
# print(Tupla2)

# # 7
# op3 = (12,3,Tupla2[0],6,7,)
# print(op3[2])

# print("------------------- EJERCICIOS DE TUPLAS -------------------")

# print("\n[1]")
# Tuple_entero = (1,2,3,4,5)
# print(Tuple_entero[0],Tuple_entero[4])

# print("\n[2]")
# Tuple_entero2 = [1.1, 2.05, 3.12, 4.4, 5.12]
# print(Tuple_entero2[0],Tuple_entero2[4])

# print("\n[3]")
# Tuple1 = ("Hello", "World", "One")
# vab1,vab2,vab3 = Tuple1
# print(vab1,vab2,vab3)

# print("\n[4]")
# lista1 = [1,2,3,4,5]
# op3 = lista1[0] + lista1[1] + lista1[2] + lista1[3] + lista1[4]
# print(f"El resultado de la suma de todos los números es: {op3}")

# print("\n[5]")
# tuple2 = (1.01, 16.02, 2.03, 23.04, 7.05)
# op4 = (tuple2[0] + tuple2[1] + tuple2[2] + tuple2[3] + tuple2[4]) / 5 
# print(f"El promedio de los números de la tuple es de: {op4}")

# print("\n[6]")
# lista2 = [1,2,3,4]
# va1,va2,va3,va4 = lista2
# print(va1,va2,va3,va4)

# print("\n[7]")
# tuple3 = (34, 78)
# op7 = tuple3[0] * tuple3[1]
# print(f"El resultado de la multiplicación es de: {op7}")

# print("\n[8]")
# lista3 = [1,2,3]
# agregar = lista3.append(16)
# print(lista3[0], lista3[3])

# print("\n[9]")
# tuple4 = (12,26,23,34)
# op8 = tuple4[0] + tuple4[1]
# print(f"La suma entre los dos primeros números es de: {op8}")

# print("\n[10]")
# lista4 = [20,2,3,4,5]
# print(lista4[0]/lista4[4])




