# print("----- TALLER DE CONDICIONALES -----")

# print("EJERCICIOS CON CONDICIONALES Y OPERACIONES MATEMÁTICAS")

# print("------------------------------------------------------")
# print("EJERCICIO N° [1]:")
# num1 = float(input("Ingrese un número: "))
# if num1 ==0:
#     print("Este número es 0")
# elif num1 >=0:
#     print("Este número es positivo.")
# elif num1 <=0:
#     print("Este número es negativo.")
# else:
#     print("Dato incorrecto o letra.")
# print("------------------------------------------------------")
# print("EJERCICIO N° [2]:")
# num2 = int(input("Ingrese un número: "))
# num3 = int(input("Ingrese un segundo número: "))
# if num2 > num3:
#     print(f"El número {num2} es mayor, mientras que el número {num3} es menor ")
# elif num3 > num2:
#     print(f"El número {num3} es mayor, mientras que el número {num2} es menor ")
# elif num2 == num3:
#     print(f"el número {num2} y el número {num3} son iguales ")
# else:
#     print("Ingresa un dato correcto.")
# print("------------------------------------------------------")
# print("EJERCICIO N° [3]:")
# num4 = int(input("Ingresa un número: "))
# mitad = num4 // 2 
# doble = mitad * 2
# if doble == num4:
#     print("El número es par") 
# elif doble != num4:
#     print("El número es impar")
# else:
#     print("Ingresa un dato correcto")
# print("------------------------------------------------------")
# print("EJERCICIO N° [4]:")
# num5 = int(input("Ingresa un número: "))
# if num5 >= 10 and num5 <= 20:
#     print("El número se encuentra entre 10 y 20")
# elif num5 >=20 or num5 <=10:
#     print("El número no está entre 10 y 20")
# else:
#     print("Ingresa un dato correcto")
# print("------------------------------------------------------")
# print("EJERCICIO N° [5]:")
# num6 = int(input("Ingresa un número: "))
# num7 = int(input("Ingresa otro número: "))
# num8 = int(input("Ingresa un último número: "))
# if num6 > num7 and num6 > num8:
#     print(f"El número {num6} es el mayor de todos.")
# elif num7 > num6 and num7 > num8:
#     print(f"El número {num7} es el mayor de todos.")
# elif num8 > num6 and num8 > num7:
#     print(f"El número {num8} es el mayor de todos.")
# elif num6 == num7 and num8 == num7:
#     print("Todos los números son iguales")
# else:
#     print("Ingresa un dato correcto")
# print("------------------------------------------------------")
# print("EJERCICIO N° [6]:")
# num9 = float(input("Ingresa el precio $ del producto: "))
# if num9 > 100:
#     descuento = num9 * 0.10
#     precio_final = num9 - descuento
#     print(f"Tu precio con un 10% de decuento es {precio_final}$") 
# elif num9 < 100:
#     print("No se aplica un descuento")
# else: 
#     print("Ingresa un dato correcto")
# print("------------------------------------------------------")
# print("EJERCICIO N° [7]:")
# edad = int(input("Ingresa tu edad: "))
# if edad >=18 and edad <=120:
#     print("Usted puede votar")
# elif edad <=17 and edad >=0:
#     print("Usted no puede votar")
# else:
#     print("Ingresa un dato o edad lógica")
# print("------------------------------------------------------")
# print("EJERCICIO N° [8]:")
# precio1 = float(input("Ingresa un precio $: "))
# tipo_cliente = input("Ingresa que tipo de cliente eres; VIP o normal: ")
# if tipo_cliente == "normal":
#     print("No se te aplica un descuento")
# elif tipo_cliente == "VIP":
#     descuento = precio1 * 0.20
#     precio_final2 = precio1 - descuento
#     print(f"Por ser VIP se te aplica un descuento del 20%. Tu precio con el descuento es {precio_final2}$")
# else:
#     print("Escribe de forma correcta el tipo de cliente que eres o dato incorrecto")
# print("------------------------------------------------------")
# print("EJERCICIO N° [9]:")
# num10 = int(input("Ingresa un número: "))
# if num10 % 5 == 0 and num10 % 3 == 0:
#     print("Es múltiplo de 5 y 3")
# else:
#     print("No es múltiplo de ambos")
# print("------------------------------------------------------")
# print("EJERCICIO N° [10]:")
# numero1 = int(input("Ingresa un número: "))
# divisor1 = int(input("Ingresa un divisor: "))
# divisor2 = int(input("Ingresa otro divisor: "))

# if numero1 % divisor1 and numero1 % divisor2 ==0:
#     print(f"El número {numero1} es divisible entre {divisor1} y {divisor2}")
# else:
#     print(f"El número {numero1} No es divisible entre {divisor1} y {divisor2}")

# print("EJERCICIOS CON LISTAS (CON CONDICIONALES)")
# print("------------------------------------------------------")
# print("EJERCICIO N° [11]:")
# lista1 = [int(input("Ingresa un número: ")), int(input("Ingresa un segundo número: ")), int(input("Ingresa un tercer número: ")), int(input("Ingresa un cuarto número: ")), int(input("Ingresa un quinto número: "))]
# if lista1[2] > 10:
#     print(f"El tercer número {lista1[2]} es mayor a 10")
# elif lista1[2] < 10:
#     print(f"El tercer número {lista1[2]} es menor o igual a 10")
# elif lista1[2] == 10:
#     print(f"El tercer número {lista1[2]} es igual a 10")
# else:
#     print("Dato incorrecto")
# print("------------------------------------------------------")
# print("EJERCICIO N° [12]:")
# lista2 = [3, 5, 7, 9]
# if lista2[2]:
#     print("El número 7 se encuentra en la lista")
# else: 
#     print("El número 7 no está en la lista")
# print("------------------------------------------------------")
# # print("EJERCICIO N° [13]:")
# lista3 = [4, 6, 2, 8]
# suma = lista3[0] + lista3[1]
# if suma >10:
#     print("Suma alta")
# elif suma <10:
#     print("Suma baja")
# elif suma ==10:
#     print("La suma es igual a 10")
# else:
#     print("Dato incorrecto")
# print("------------------------------------------------------")
# print("EJERCICIO N° [14]:")
# lista4 = ["Ana", "Luis", "Pedro", "Marta"]
# print(f"El último nombre es {lista4[-1]}")

# if lista4[-1] == "Marta":
#     print("Nombre correcto")
# elif lista4[-1] != "Marta":
#     print("Nombre diferente")
# else:
#     print("Dato incorrecto")
# print("------------------------------------------------------")
# print("EJERCICIO N° [15]:")
# lista5 = [input("Ingresa el primer color: ").lower(), input("Ingresa el segundo color: ").lower(), input("Ingresa el tercer color: ").lower()]

# if lista5[1] == "azul":
#     lista5[1] = input("Ingrese el color deseado para reemplazar por el azul: ")
#     print(lista5)
# elif lista5[1] != "azul":
#     print("El segundo color no es azul, no requiere cambios")
# else:
#     print("Ingresa un dato correcto")
# print("------------------------------------------------------")

# print("EJERCICIOS CON TUPLAS (CON CONDICIONALES)")

# print("------------------------------------------------------")
# print("EJERCICIO N° [16]:")
# tupla1 = (5, 8, 12, 20)
# if tupla1[0] < tupla1[3]:
#     print("Orden ascente")
# elif tupla1[0] > tupla1[3]:
#     print("Orden descente")
# else:
#     print("Dato incorrecto o incoherente")
# print("------------------------------------------------------")
# print("EJERCICIO N° [17]:")
# tupla2 = (25, 32, 28)
# if tupla2[1] >30:
#     print("Edad mayor a 30")
# elif tupla2[1] <=30:
#     print("Edad menor o igual a 30")
# else:
#     print("ingresa un dato correcto")
# print("------------------------------------------------------")
# print("EJERCICIO N° [18]:")
# tupla3 = (int(input("Ingrese un número: ")), int(input("Ingrese otro número: ")), int(input("Ingrese un último número: ")),)
# lista1 = list(tupla3)
# print(lista1)
# if lista1[1] == 2:
#     lista1[1] = 10
# else:
#     print("el segundo número no es un 2 por lo cual no se hace cambio")
# tupla1 = tuple(lista1)
# print(tupla1)
# print("------------------------------------------------------")
# print("EJERCICIO N° [19]:")
# tupla5 = (int(input("Ingrese un número: ")), int(input("Ingrese otro número: ")))
# lista2 = list(tupla5)
# if lista2[1] > 5:
#     print("Coordenada alta")
# elif lista2[1] == 5:
#     print("El número es igual a 5")
# elif lista2[1] != 5:
#     print("Coordenada baja")
# else:
#     print("Dato incorrecto")
# print("------------------------------------------------------")
# print("EJERCICIO N° [20]:")
# tupla6 = (3, 4) 
# tupla7 = (3, 5)

# if tupla6 == tupla7:
#     print("Las tuplas son iguales")
# elif tupla6 != tupla7:
#     print("Las tuplas son distintas")
# else:
#     print("Error")    
# print("------------------------------------------------------")

# print("EJERCICIOS CON DICCIONARIOS (CON CONDICIONALES)")


print("EJERCICIO N° [21]:")
