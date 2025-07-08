# DICCIONARIOS 

# Un diccionario en python es una estructura de datos que permite almacenar valores claves, 
# es muy util cuando queremos agregar o asociar una clave con un dato.

# CARACTERÍSTICAS

# 1. Las claves que agreguemos en los diccionarios deben ser unicas.
# 2. las claves pueden ser de tipo inmutable y pueden ser tipo string, enteros, tuplas.
# 3. Los valores que pueden llevar un diccionario son: otros diccionarios, listas, cadenas de carácteres entre otros.
# 4. Los diccionarios se colocan entre llaves.

# print("------------------- EJERCICIOS -------------------")

# mascota = input("Ingrese el nombre de la mascota: ")
# tipo_a = input("Ingrese el tipo de animal: ")
# edad = int(input("Ingrese la edad de la mascota: "))
# dueño = input("Ingrese el nombre del dueño: ")
# Ciudad = input("Ingrese la cidad donde está ubicado: ")

# Mascota = {
#     "Nombre": mascota,
#     "Tipo": tipo_a,
#     "edad": edad,
#     "dueño": dueño,
#     "ciudad": Ciudad,
# }

# print("Los datos guardados son: ", Mascota)

# print("--------------------------------------------------")

# # Diccionario con información de un estudiante
# estudiante = {
#     "nombre": "Sofía",
#     "edad": 16,
#     "notas": [4.5, 3.8, 5.0]
# }

# # Mostrar toda la información
# print("Información del estudiante:")
# print(estudiante)

# # Mostrar nombre y edad por separado
# print(f"Nombre: {estudiante['nombre']}")
# print(f"Edad: {estudiante['edad']} años")

# # Mostrar la segunda nota
# print(f"Segunda nota: {estudiante['notas'][1]}")

# print("--------------------------------------------------")

# # Primer diccionario
# dictionary = {
#     "a": 1,
#     "e": 2
# }

# print()
# print(dictionary)
# print(f"Clave a: {dictionary['a']}")
# print(f"Clave e: {dictionary['e']}")

# # Segundo diccionario con lista y diccionario dentro
# dictionary = {
#     "numbers": [18, 20, 28],
#     "groups": {"a": 1, "b": 2}
# }

# print(dictionary)
# print(f"Clave 'numbers': {dictionary['numbers']}")
# print(f"Clave 'groups': {dictionary['groups']}")

# # Acceso a valores dentro de la lista y del diccionario interno
# print(f"Segundo número en 'numbers': {dictionary['numbers'][1]}")
# print(f"Valor de la clave 'b' en 'groups': {dictionary['groups']['b']}")

# # Acceso a una clave que no existe, usando try-except
# try:
#     print(f"Clave 'z': {dictionary['z']}")
# except KeyError:
#     print("La clave 'z' no existe en el diccionario.")

# print("--------------------------------------------------")

# print("Pequeño programa Taller 1.")

# nom_product = input("por favor, ingrese el nombre del producto: ")
# precio = float(input("Por favor, ingrese el precio unitario: "))
# unidad = int(input("Ingrese la cantidad comprada: "))

# tupla1 = (nom_product, precio)
# lista1 = [tupla1, unidad]

# diccionario1 = {"producto: ": lista1}
# print(f"el costo total de la cantidad del producto {nom_product} es: {unidad * precio}")

# print("--------------------------------------------------")

# print("Pequeño programa Taller 2.")

# product1 = [(input("Ingrese el nombre del producto: "), float(input("Ingrese el precio del producto: ")), int(input("ingrese la cantidad a comprar: ")))]

# product2 = [(input("Ingrese el nombre del producto: "), float(input("Ingrese el precio del producto: ")), int(input("ingrese la cantidad a comprar: ")))]

# product3 = [(input("Ingrese el nombre del producto: "), float(input("Ingrese el precio del producto: ")), int(input("ingrese la cantidad a comprar: ")))]

# diccionario2 = {"producto 1: ": product1, "producto 2: ": product2, "producto 3: ": product3}

# print(f"El total del producto {product1[0]} es: {product1[1] * product1[2]}")

# print("--------------------------------------------------")

# print("Pequeño programa Taller 3.")

# name = input("Hola, ingrese su nombre: ")

# asignatura1 = (input("Ingrese el nombre de su primer asignatura: "), float(input("Ingrese la primera nota de esta materia: ")), float(input("Ingrese la segunda nota de esta materia: ")))

# asignatura2 = (input("Ingrese el nombre de su segunda asignatura: "), float(input("Ingrese la primera nota de esta materia: ")), float(input("Ingrese la segunda nota de esta materia: ")))

# asignatura3 = (input("Ingrese el nombre de su tercera asignatura: "), float(input("Ingrese la primera nota de esta materia: ")), float(input("Ingrese la segunda nota de esta materia: ")))

# lista_1 = [asignatura1,(asignatura1[1] + asignatura1[2]) / 2, asignatura2,(asignatura2[1] + asignatura2[2]) / 2, asignatura3,(asignatura3[1] + asignatura3[2]) / 2]

# diccionario1 = {"nombre": name, "materias": asignatura1[0] and asignatura2[0] and asignatura3[0]}

# print(f"Tu promedio es: {lista_1}")

# print("--------------------------------------------------")

# print("Isn't finished yet")


