# Una lista es una estructura de datos que se utiliza para almacenar múltiples datos en una sola variable.
# Es uno de los tipos de datos más utilizados en Python, ya que es mutable,
# lo que significa que puedes cambiar sus elementos después de haberla creado (usando []).

# CARACTERÍSTICAS DE LAS LISTAS:

# 1. ORDENADAS: Mantienen el orden en que fueron añadidos los elementos.
# 2. MUTABLES: Puedes modificar, agregar o eliminar elementos después de crear la lista.
# 3. PUEDEN CONTENER DISTINTOS TIPOS DE DATOS: Números, cadenas de texto, booleanos, otras listas, etc.
# 4. PERMITEN ELEMENTOS DUPLICADOS: Puedes tener valores repetidos dentro de una lista. Ejemplo:
#    ejemplo = [1, 2, 2, "hola", "hola"]

# print("------------------- EJEMPLOS -------------------")

# print("Ejemplo N° [1]")

# # Lista de números
# lista1 = [1, 2, 3, 4, 5, 6]

# # Muestra el primer valor de la lista (índice 0)
# print("Primer valor de la lista1 es :", lista1[0])  
# print("El último valor de la lista1 es:", lista1[5])

# print("------------------------------------------")

# print("Ejemplo N° [2]")

# # Lista mixta con números y texto
# Cadena = [1, 2, 3, 5, "hola", -1, "claro"]

# # Imprime el valor en la posición -3 (cuenta desde el final)
# print("Elemento en posición -3 de la lista:", Cadena[-3])  

# print("------------------------------------------")

# # ¿QUÉ ES .APPEND?

# # Explicación en forma de código:

# print("Ejemplo N° [3]")

# # Este método se usa para agregar un elemento al final de una lista
# # Sintaxis: lista.append(elemento)

# # Ejemplo:

# lista2 = []  # Lista vacía

# lista2.append("Python")  # Agregamos un elemento
# lista2.append("123")  # Otro más

# print("Lista después de usar .append:", lista2)

# print("------------------------------------------")

# print("Ejemplo N° [4]")

# print("Diferencia entre .append y operador +\n")

# # .append() modifica la lista original
# lista_a = [1, 2, 3]

# lista_a.append(4)

# print("Usando .append:", lista_a)  # Resultado: [1, 2, 3, 4]

# # + crea una nueva lista combinada, sin modificar la original
# lista_b = [5, 6]
# lista_c = lista_a + lista_b

# print("Usando + (lista_a + lista_b):", lista_c)  # Resultado: [1, 2, 3, 4, 5, 6]

# print("Lista original lista_a no cambia:", lista_a)  # Sigue siendo: [1, 2, 3, 4]

# print("------------------------------------------")

# print("Ejemplo N° [5]")

# materia = ["sociales", "algebra", "trigonometría"]

# # Se reemplaza el valor en la posición 2 (índice 2)
# materia[2] = "Robotica"

# # Muestra la lista modificada
# print(materia)

# print("------------------------------------------")

# print("Ejemplo N° [6]")

# # Se crea una lista con dos números ingresados por el usuario
# numeros = [
#     int(input("Ingrese un número a sumar: ")),
#     int(input("Ingrese otro número a sumar: "))
# ]

# # Se suman los dos valores de la lista
# suma = numeros[0] + numeros[1]

# # Muestra el resultado
# print("Ejemplo N° [2]")
# print(f"El resultado es: {suma}")

# print("------------------- EJERCICIOS -------------------")

# print("Ejercicios N° [1]")

# numeros2 = [1, 2, 3, 2]

# # Elimina el primer 2 
# numeros2.remove(2)

# # Elimina el siguiente 2 
# numeros2.remove(2)

# # Muestra la lista final después de eliminar ambos 2
# print(f"El resultado final es: {numeros2}")  

# numeros3 = [1, 2, 3, 2]

# # Reemplaza el valor en la posición 3 por un 4
# numeros3[3] = 4  # La lista ahora es [1, 2, 3, 4]

# # Elimina el número 4 de la lista
# numeros3.remove(4)

# # Muestra la lista final después de la modificación
# print(numeros3)

print("------------------------------------------------")

print("Ejercicios N° [2]")

contacto1 = int(input("Ingrese un número de su primer contacto: "))
contacto2 = int(input("Ingrese un número de su segundo contacto: "))
contacto3 = int(input("Ingrese un número de su tercer contacto: "))

# Crea una lista con un guion en la posición 0 para que los índices coincidan con 1, 2, 3
lista = ["-", contacto1, contacto2, contacto3]

# Pide al usuario que elija un número del 1 al 3 para ver uno de los contactos
soli = int(input("Ingrese el número de contacto que desea escoger (1-3): "))

# Muestra el contacto seleccionado
print(f"El número del contacto {soli} es: {lista[soli]}")

print("------------------------------------------------")

productos = []
productos.append(input("Ingrese un producto: "))
productos.append(input("Ingrese otro producto: "))
productos.append(input("Ingrese un último producto: "))
print(f"la lista de los productos es: {productos}")

print("------------------------------------------------")

articulo = []
articulo.append(float(input("Ingrese un artículo: ")))
articulo.append(float(input("Ingrese un segundo artículo: ")))
articulo.append(float(input("Ingrese un último artículo: ")))
op = articulo.append[0] + articulo[1] + articulo[2] 
print(f"La suma de los precios es: {articulo}")

print("------------------------------------------------")

numeros = []
numeros.append(int(input("Ingrese un número: ")))
numeros.append(int(input("Ingrese un segundo número: ")))
numeros.append(int(input("Ingrese un tercer número: ")))
numeros.append(int(input("Ingrese un cuarto número: ")))
print(f"el numero mayor fue {max(numeros)}, el menor fue {min(numeros)}")

# print("------------------------------------------------")

empleado = ["Carla", "JOSÉ", "Alenjandro", "luis", "Carla", "Ana", "Florencia", "Gerardo", "Guzman", "JOSÉ", "gustavo", "Gabriela"]
print(empleado)
empleado.append("JULIANA")
total = len(empleado)
print(f"la cantidad de elementos en la lista es: {total}")
print(f"El menor nombre organizado alfabéticamente es {min(empleado)} y el mayor nombre organizado alfabéticamente es {max(empleado)}")

print("------------------- PROGRAMA DE 50 LÍNEAS DE CÓDIGO -------------------")

print("PROGRAMA DE TUPLAS, LISTAS, Y OPERACIONES.")

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))
num4 = int(input("Número 4: "))
num5 = int(input("Número 5: "))
num6 = int(input("Número 6: "))
num7 = int(input("Número 7: "))
num8 = int(input("Número 8: "))
num9 = int(input("Número 9: "))
num10 = int(input("Número 10: "))

lista_1 = [num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]

Tupla1 = (num1, num1**2)
Tupla2 = (num2, num2**2)
Tupla3 = (num3, num3**2)
Tupla4 = (num4, num4**2)
Tupla5 = (num5, num5**2)
Tupla6 = (num6, num6**2)
Tupla7 = (num7, num7**2)
Tupla8 = (num8, num8**2)
Tupla9 = (num9, num9**2)
Tupla10 = (num10, num10**2)

lista_2 = (Tupla1,Tupla2,Tupla3,Tupla4,Tupla5,Tupla6,Tupla7,Tupla8,Tupla9,Tupla10)

suma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
print(f"El resultado entre la suma es: {suma}")

promedio = suma // 10
print(f"El promedio de la suma es: {promedio}")

doble = suma**2
print(f"El doble de la suma es: {doble}")

mitad = promedio // 2
print(f"La mitad del promedio es: {mitad}")

lista_ult = [
    num1 - num2,
    num3 * num4,
    num5 ** num6,
    num7 / num8,
    num9 + num10,
]
print(lista_ult)


