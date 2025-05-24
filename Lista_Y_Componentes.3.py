# Una lista es una estrutura de datos que se utiliza para almacenar multiples datos en una sola variable. Es uno de los tipos de datos más utilizados en python ya quie es mutable, lo que significa que puede cambiar sus selementos despues de haberlos creado ([]).

# Características principales de las listas: 

# 1. ORDENADAS: Ordena los elementos y mantienen el orden en que fueron añadidos
# 2. MUTABLES:
# 3. pueden contener distitntos tipos de datos: números, cadenas, otras listas etc.
# 4. permite elementos duplicados. ejemplo:

# listas = []
# lista1 = [1,2,3,4,5,6]
# lista2 = ["Hola", "mundo", -1, "Colombia"]
# print(lista1[0])

# Cadena = [1,2,3,5, "hola", -1, "claro"]
# print(Cadena[-3])

# ¿Qué es .append?
# Este método se usa para agregar un elemento al final de una lista

# lista.append(elemento)
# - lista = el nombre de tu lista
# - elemento = el valor que deseas agregar

# No es lo mismo usar el .append que usar el más (+) aunque ambos pueden usarse para trabajar con listas sus funciones no son las mismas + operador de concatenación 

# El (+) no modifica la lista de origen 
# el .append si perimite la modificacion de una lista agregando un elemento

# print("------------------- EJERCICIOS -------------------")

# materia = ["sociales", "algebra", "trigonometría"]
# materia[2] = "Robotica"
# print(materia)

# print("------------------------------------------------")

# numeros = [int(input("Ingrese un numero a sumar: ")), int(input("Ingrese otro numero a sumar: "))]
# suma = numeros[0] + numeros[1]
# print(f"el resultado es: {suma}")

# print("------------------------------------------------")

# num = [1,2,3,2]                
# num.remove(2)              
# num.remove(2)
# print(num)

# num = [1,2,3,2]
# num[3]=4
# num.remove(4)
# print(num)

# print("------------------------------------------------")

# con1 = int(input("Ingrese un numero de su primer contacto: "))
# con2 = int(input("Ingrese un numero de su segundo contacto: "))
# con3 = int(input("Ingrese un numero de su tercer contacto: "))
# lista = ["-", con1, con2, con3]
# soli = int(input("Ingrese el número de contacto que desea escojer: "))
# print(lista[soli])

# print("------------------------------------------------")

# productos = []
# productos.append(input("Ingrese un producto: "))
# productos.append(input("Ingrese otro producto: "))
# productos.append(input("Ingrese un último producto: "))
# print(f"la lista de los productos es: {productos}")

# print("------------------------------------------------")

# articulo = []
# articulo.append(float(input("Ingrese un artículo: ")))
# articulo.append(float(input("Ingrese un segundo artículo: ")))
# articulo.append(float(input("Ingrese un último artículo: ")))
# op = articulo.append[0] + articulo[1] + articulo[2] 
# print(f"La suma de los precios es: {articulo}")

# print("------------------------------------------------")

# numeros = []
# numeros.append(int(input("Ingrese un número: ")))
# numeros.append(int(input("Ingrese un segundo número: ")))
# numeros.append(int(input("Ingrese un tercer número: ")))
# numeros.append(int(input("Ingrese un cuarto número: ")))
# print(f"el numero mayor fue {max(numeros)}, el menor fue {min(numeros)}")

# # print("------------------------------------------------")

# empleado = ["Carla", "JOSÉ", "Alenjandro", "luis", "Carla", "Ana", "Florencia", "Gerardo", "Guzman", "JOSÉ", "gustavo", "Gabriela"]
# print(empleado)
# empleado.append("JULIANA")
# total = len(empleado)
# print(f"la cantidad de elementos en la lista es: {total}")
# print(f"El menor nombre organizado alfabéticamente es {min(empleado)} y el mayor nombre organizado alfabéticamente es {max(empleado)}")

# print("------------------- PROGRAMA DE 50 LÍNEAS DE CÓDIGO -------------------")

# print("PROGRAMA DE TUPLAS, LISTAS, Y OPERACIONES.")

# num1 = int(input("Número 1: "))
# num2 = int(input("Número 2: "))
# num3 = int(input("Número 3: "))
# num4 = int(input("Número 4: "))
# num5 = int(input("Número 5: "))
# num6 = int(input("Número 6: "))
# num7 = int(input("Número 7: "))
# num8 = int(input("Número 8: "))
# num9 = int(input("Número 9: "))
# num10 = int(input("Número 10: "))

# lista_1 = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]

# Tupla1 = (num1, num1**2)
# Tupla2 = (num2, num2**2)
# Tupla3 = (num3, num3**2)
# Tupla4 = (num4, num4**2)
# Tupla5 = (num5, num5**2)
# Tupla6 = (num6, num6**2)
# Tupla7 = (num7, num7**2)
# Tupla8 = (num8, num8**2)
# Tupla9 = (num9, num9**2)
# Tupla10 = (num10, num10**2)

# lista_2 = (Tupla1,Tupla2,Tupla3,Tupla4,Tupla5,Tupla6,Tupla7,Tupla8,Tupla9,Tupla10)

# suma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
# print(f"El resultado entre la suma es: {suma}")

# promedio = suma // 10
# print(f"El promedio de la suma es: {promedio}")

# doble = suma**2
# print(f"El doble de la suma es: {doble}")

# mitad = promedio // 2
# print(f"La mitad del promedio es: {mitad}")

# lista_ult = [
#     num1 - num2,
#     num3 * num4,
#     num5 ** num6,
#     num7 / num8,
#     num9 + num10,
# ]
# print(lista_ult)


