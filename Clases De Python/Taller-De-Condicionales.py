print("----- TALLER DE CONDICIONALES -----")

print("EJERCICIOS CON CONDICIONALES Y OPERACIONES MATEMÁTICAS")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [1]:\n ")

# Pide un número al usuario
num1 = float(input("Ingrese un número: "))

# Si el número es mayor a 0
if num1 > 0:
    print(f"El número {num1} es positivo.")
    
# Si el número es menor a 0
elif num1 < 0:
    print(f"El número {num1} es negativo.")
    
# Si el número es igual a 0
elif num1 == 0:
    print(f"El número {num1} es equivalente a 0.")
    
# Si no cumple las condiciones anteriores
else:
    print("Ingresa un dato incorrecto.")

print("\n------------------------------------------------------") 

print("\nEJERCICIO N° [2]:\n ")

# Pide dos números al usuario
num2 = int(input("Ingrese un número: "))
num3 = int(input("Ingrese otro número: "))

# Condiciones a partir de los números que ingrese el usuario
if num2 > num3:
    print(f"El número {num2} es mayor, mientras que el número {num3} es menor.")
elif num3 > num2:
    print(f"El número {num3} es mayor, mientras que el número {num2} es menor.")
elif num2 == num3:
    print(f"el número {num2} y el número {num3} son iguales.")
    
# Si no cumple las condiciones anteriores
else:
    print("Ingresa un dato correcto.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [3]:\n ")

num4 = int(input("Ingresa un número: "))

# Divide el número ingresado por 2
mitad = num4 // 2 

# multiplica la mitad por 2
doble = mitad * 2

if doble == num4:
    print(f"El número {num4} es par.") 

# Si el 'doble' es diferente al número ingresado
elif doble != num4:
    print(f"El número {num4} es impar.")
else:
    print("Ingresa un dato correcto.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [4]:\n ")

num5 = int(input("Ingresa un número: "))

# Si el número es mayor o igual a 10 Y es menor o iaugl a 20
if num5 >= 10 and num5 <= 20:
    print(f"El número {num5} se encuentra entre 10 y 20.")
elif num5 >=20 or num5 <=10:
    print(f"El número {num5} no está entre 10 y 20.")
    
# Si no cumple las condiciones anteriores
else:
    print("Ingresa un dato correcto.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [5]:\n ")

# Pide tres números al usuario
num6 = int(input("Ingresa un número: "))
num7 = int(input("Ingresa otro número: "))
num8 = int(input("Ingresa un último número: "))

# Hace rangos de acuerdo a los números ingresados
if num6 > num7 and num6 > num8:
    print(f"El número {num6} es mayor que {num7} y {num8}.")
elif num7 > num6 and num7 > num8:
    print(f"El número {num7} es mayor que {num6} y {num8}.")
elif num8 > num6 and num8 > num7:
    print(f"El número {num8} es mayor que {num6} y {num7}.")
elif num6 == num7 and num8 == num7:
    print(f"Los números {num6}, {num7} y {num8} son iguales.")
else:
    print("Ingresa un dato correcto.")
    
print("\n------------------------------------------------------")

print("\nEJERCICIO N° [6]:\n ")

num9 = float(input("Ingresa el precio $ del producto: "))

if num9 > 100:
    
    # Se multiplica el precio por el 10%
    descuento = num9 * 0.10
    
    # Se resta el descuento con el precio inicial
    precio_final = num9 - descuento
    
    print(f"Tu precio de {num9}$ con un 10% de decuento es {precio_final}$") 
elif num9 < 100:
    print(f"Al precio {num9} No se le aplica un descuento porque es menor a 100$.")
else: 
    print("Ingresa un dato correcto.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [7]:\n ")

edad = int(input("Ingresa tu edad: "))

# Si tiene una edad mayor de 18
if edad >=18 and edad <=122:
    print(f"Usted tiene {edad} años, si puede votar.")
    
# Si la edad es menor a 18
elif edad <=17 and edad >=0:
    print(f"Usted tiene {edad} años, por lo cual no puede votar.")
else:
    print("Ingresa un dato o edad lógica.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [8]:\n ")

# Se piden datos al usuario
precio1 = float(input("Ingresa un precio $: "))
tipo_cliente = input("Ingresa que tipo de cliente eres; 'VIP' o 'normal': ").capitalize()

# Si el usuario solo es un cliente 'normal'
if tipo_cliente == "Normal":
    print(f"Al ser cliente {tipo_cliente} no se te aplica un descuento.")

# Si el usuario solo es un cliente 'VIP'
elif tipo_cliente == "Vip":
    
    # Se multiplica el precio por el 10% 
    descuento = precio1 * 0.20
    
    # Se resta el descuento con el precio inicial
    precio_final2 = precio1 - descuento
    
    print(f"Por ser {tipo_cliente} se te aplica un descuento del 20%. Tu precio con el descuento es {precio_final2}$")
else:
    print("Escribe de forma correcta el tipo de cliente que eres.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [9]:\n ")

num10 = int(input("Ingresa un número: "))

# El operador % (módulo) obtiene el residuo de una división
# Si el residuo es 0, significa que el número es divisible sin dejar decimales

if num10 % 5 == 0 and num10 % 3 == 0:
    print(f"El número {num10} es múltiplo de 5 y 3.")
else:
    # Si no cumple ambas condiciones
    print(f"El número {num10} no es múltiplo de ambos.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [10]:\n ")

numero1 = int(input("Ingresa un número: "))
divisor1 = int(input("Ingresa un divisor: "))
divisor2 = int(input("Ingresa otro divisor: "))

# La operación % (módulo) devuelve el residuo de una división
# Si el residuo es 0, significa que la división es exacta (es divisible)

if numero1 % divisor1 == 0 and numero1 % divisor2 ==0:
    # Si el número es divisible por los dos divisores al mismo tiempo
    print(f"El número {numero1} es divisible entre {divisor1} y {divisor2}")
else:
    # Si no es divisible entre los dos a la vez (aunque tal vez sí con uno solo)
    print(f"El número {numero1} No es divisible entre {divisor1} y {divisor2}")

print("\n-------------------------------------------------------\n")

print("EJERCICIOS CON LISTAS (CON CONDICIONALES)")

print("\n-------------------------------------------------------")

print("\nEJERCICIO N° [11]:\n ")

# Se crea una lista con 5 números ingresados por el usuario
lista1 = [
    int(input("Ingresa un número: ")),
    int(input("Ingresa un segundo número: ")),
    int(input("Ingresa un tercer número: ")),  
    int(input("Ingresa un cuarto número: ")),
    int(input("Ingresa un quinto número: "))
]

# Se evalúa si el tercer número es mayor, menor o igual a 10
if lista1[2] > 10:
    print(f"El tercer número {lista1[2]} de la lista es mayor a 10.")
elif lista1[2] < 10:
    print(f"El tercer número {lista1[2]} de la lista es menor a 10.")
elif lista1[2] == 10:
    print(f"El tercer número {lista1[2]} de la lista es igual a 10.")
else:
    print("Ingresa un dato correcto.")
    
print("\n------------------------------------------------------")

print("\nEJERCICIO N° [12]:\n ")

# Se crea una lista con 4 números ingresados por el usuario
lista2 = [
    int(input("Ingresa un número: ")),
    int(input("Ingresa otro número: ")),
    int(input("Ingresa un tercer número: ")),
    int(input("Ingresa un último número: "))
]

# Se revisa si el número 7 está en alguna posición de la lista
# Solo se evalúa posición por posición con condicionales
if lista2[0] == 7:
    print("El número 7 se encuentra en la lista.")
elif lista2[1] == 7:
    print("El número 7 se encuentra en la lista.")
elif lista2[2] == 7:
    print("El número 7 se encuentra en la lista.")
elif lista2[3] == 7:
    print("El número 7 se encuentra en la lista.")
else: 
    print("El número 7 no está en la lista.")

print("\n------------------------------------------------------")

# Se crea una lista con 4 números ingresados por el usuario
lista3 = [
    int(input("Ingresa un número: ")),
    int(input("Ingresa otro número: ")),
    int(input("Ingresa un tercer número: ")),
    int(input("Ingresa un último número: "))
]

# Se suman los dos primeros números de la lista
suma = lista3[0] + lista3[1]

# Se evalúa si la suma es mayor, menor o igual a 10
if suma > 10: 
    print(f"La suma entre los números {lista3[0]} y {lista3[1]} es alta.")
elif suma < 10:
    print(f"La suma entre los números {lista3[0]} y {lista3[1]} es baja.")
elif suma == 10:
    print("La suma es igual a 10.")
else:
    print("Dato incorrecto.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [14]:\n ")

lista4 = [input("Ingresa un nombre: ").capitalize(), input("Ingresa otro nombre: ").capitalize(), input("Ingresa un tercer nombre: ").capitalize(), input("Ingresa un último nombre: ").capitalize()]
print(f"Tu lista es: {lista4}")
print(f"El último nombre es {lista4[-1]}")

if lista4[-1] == "Marta":
    print("Nombre correcto, acceso autorizado.")
elif lista4[-1] != "Marta":
    print("Nombre diferente, acceso denegado.")
else:
    print("Dato incorrecto.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [15]:\n ")

lista5 = [input("Ingresa el primer color: ").capitalize(), input("Ingresa el segundo color: ").capitalize(), input("Ingresa el tercer color: ").capitalize()]

if lista5[1] == "Azul":
    lista5[1] = input(f"El segundo color es {lista5[1]}, ingrese el color deseado para reemplazar por el azul: ")
    print(lista5)
elif lista5[1] != "azul":
    print(f"El segundo color no es azul, es {lista5[1]}, por lo cual no requiere cambios.")
else:
    print("Ingresa un dato correcto.")
    
print("\n------------------------------------------------------\n")

print("EJERCICIOS CON TUPLAS (CON CONDICIONALES)")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [16]:\n ")

tupla1 = (int(input("Ingresa un número: ")), int(input("Ingresa un segundo número: ")), int(input("Ingresa un tercer número: ")), int(input("Ingresa un cuarto número: ")))
if tupla1[0] < tupla1[3]:
    print(f"El valor {tupla1[0]} es menor que {tupla1[3]}, Orden ascente.")
elif tupla1[0] > tupla1[3]:
    print(f"El valor {tupla1[0]} es mayor que {tupla1[3]}, Orden descente.")
else:
    print("Dato incorrecto o incoherente.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [17]:\n ")

tupla2 = (int(input("Ingresa un número: ")), int(input("Ingresa un segundo número: ")), int(input("Ingresa un último número: ")))
if tupla2[1] >30:
    print(f"El segundo valor: {tupla2[1]}, es mayor a 30. Por lo cual, tu edad es mayor a 30.")
elif tupla2[1] <=30:
    print(f"El segundo valor: {tupla2[1]}, es menor o igual a 30. Por lo cual, tu edad es menor a 30.")
else:
    print("ingresa un dato correcto.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [18]:\n ")

tupla3 = (int(input("Ingrese un número: ")), int(input("Ingrese otro número: ")), int(input("Ingrese un último número: ")))
lista1 = list(tupla3)
print(lista1)
if lista1[1] == 2:
    lista1[1] = 10
    print(f"Como el segundo número de la lista es igual a 2, se reemplazara por un 10.")
else:
    print("el segundo número no es un 2 por lo cual no se hace cambio.")
tupla2 = tuple(lista1)
print(tupla2)

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [19]:\n ")

tupla5 = (int(input("Ingrese un número: ")), int(input("Ingrese otro número: ")))
lista2 = list(tupla5)
if lista2[1] > 5:
    print(f"El segundo valor es: {lista2[1]}. Este es  mayor a 5. Coordenada alta.")
elif lista2[1] == 5:
    print(f"El segundo valor es: {lista2[1]}. Este es igual a 5.")
elif lista2[1] != 5:
    print(f"El segundo valor es: {lista2[1]}. Este es  menor a 5. Coordenada baja.")
else:
    print("Dato incorrecto.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [20]:\n ")

tupla6 = (int(input("Ingrese un número: ")), int(input("Ingrese otro número: "))) 
print("-------------------")
tupla7 = (int(input("Ingrese un número: ")), int(input("Ingrese otro número: ")))

if tupla6 == tupla7:
    print(f"Los datos de las tuplas {tupla6} y {tupla7} son iguales.")
elif tupla6 != tupla7:
    print(f"Los datos de las tuplas {tupla6} y {tupla7} son distintas.")
else:
    print("Dato inocrrecto.")    

print("\n------------------------------------------------------\n")

print("EJERCICIOS CON DICCIONARIOS (CON CONDICIONALES)")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [21]:\n ")

dic1 = {"Nombre": input("Ingresa tu nombre: ").capitalize(), "Edad": int(input("Ingresa tu edad: "))}
if dic1["Edad"] >= 18:
    print(f"{dic1["Nombre"]}, Tu edad es de {dic1["Edad"]} años. Eres adulto.")
elif dic1["Edad"] <18:
    print(f"{dic1["Nombre"]}, Tu edad es de {dic1["Edad"]} años. Eres menor de edad.")
else:
    print("Dato incorrecto.")
    
print("\n------------------------------------------------------")

print("\nEJERCICIO N° [22]:\n ")

dic2 = {"Nombre": input("Ingrese su nombre: ").capitalize(), "Edad": int(input("Ingrese su edad: "))}
if dic2["Edad"] >= 18:
    dic2["Edad"] = 21
    print(f"Eres mayor de edad, asi que tu edad ahora es 21.")
print(f"los datos son: {dic2}.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [23]:\n ")

dic2 = {"Nombre": input("Ingresa tu nombre: ").capitalize()}
if "Ciudad" not in dic2:
    dic2["Ciudad"] = "Bogota"
print(f"Los datos finales son: {dic2}.")

print("\n------------------------------------------------------")

print("\nEJERCICIO N° [24]:\n ")

dic3 = {"Producto": input("Ingrese su producto: ").capitalize(), "Precio":  float(input("Ingresa el precio: "))}
if "Precio" in dic3:
    print(f"El precio es: {dic3["Precio"]}$.")
else:
    dic3["Precio"] = "No hay precio."
    print("No se encontró un precio, se asignó: No hay precio.")
print(f"Los datos del producto son: {dic3}")
    
print("\n------------------------------------------------------")

print("\nEJERCICIO N° [25]:\n ")

dic4 = {"Pan": float(input("Ingrese el precio: ")), "Leche":  float(input("Ingresa el precio: "))}
if "Pan" in dic4:
    print(f"El precio del pan es {dic4["Pan"]}$")
else:
    print("Producto no disponible.")
    
print("\n------------------------------------------------------")

print("FIN DEL PROGRAMA.")