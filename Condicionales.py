# CONCEPTOS A TENER EN CUENTA:

# ¿QUÉ ES EL FLUJO? 
# El flujo es una forma de entender la sucesion de las instrucciones de un programa, estas instrucciones se ejecutan una depues de otra de forma ordenada y suelen tener el objetivo final de manipular informacion.

# ¿QUÉ ES UN DIAGRAMA DE FLUJO?
# Expresan nuestros algoritmos en forma de diagrama mediante una representación gráfica basada en figuras geométricas que varían según la estructura del código.

# CONDICIONALES 
# Se utilizan los operadores relacionales (==, !, >, <, etc.) y para evaluar más de una condicón simultáneamente se utilizan los operadores lógicos (not, and, or). las condiconales se definen mediante el uso de tres palabras claves reservadas: if, elif, else.

# print("----------------------------------------------------")

# print("Ejemplo N° [1]")

# # solicito nombre y edad al usuario
# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))

# # verifica si el usuario es mayor o igual a 18
# if edad >=18:
#     print(f"{nombre}, Tienes {edad} años. Eres mayor de edad.")
    
# # verifica  si la edad está entre 1 y 17 años
# elif edad >0 and edad <18:
#     print(f"{nombre}, Tienes {edad} años. Eres menor de edad.")
    
# # si la edad es 0 o negativa, se considera un dato inválido
# else:
#     print("Dato incorrecto: la edad no puede ser negativa o cero")
    
# print("----------------------------------------------------")

# print("Ejemplo N° [2]")

# # solicito tres números reales al usuario
# a = float(input("Ingresa un numero: "))
# b = float(input("Ingresa otro número: "))
# c = float(input("Ingresa un último número: "))

# # verifica si 'a' es mayor que 'b' y 'c' es mayor que 'a'
# if a > b and c > a:
#     print(f"{a} es mayor que {b} y {c} mayor que {a}.")
# else: 
#     print("Una de las condiciones es falsa")
    
# print("----------------------------------------------------")

# print("Ejemplo N° [3]")

# # solicito al usuario un número decimal 
# numero = float(input("Ingrese un número: "))

# # verifica si el número ingresado es mayor a 36
# if numero > 36:
#     print(f"El número {numero} es grande.")
# else:
#     print(f"El número {numero} es pequeño.")
    
# print("----------------------------------------------------")

# print("Ejemplo N° [4]")

# # solicito al usuario un número entero
# x = int(input("Ingrese un número: "))

# # verifica si el número es mayor a 10
# if x >10:
#     print("El número está por encima de 10")
    
#     # dentro de ese grupo, verifica si además es mayor a 20
#     if x >20:
#         print("El número está por encima de 20")
        
#         # verifica si además es mayor a 30
#         if x >30:
#             print("El número está por encima de 30")
            
#             # si también es mayor a 40
#             if x >40:
#                 print("Y también está por encíma de 40")         
# else:
#     print(f"El número {x} está debajo de 10")
    
# print("----------------------------------------------------")

# print("Ejemplo N° [5]")

# # solicito dos números enteros al usuario
# num1 = int(input("Ingrese un número: "))
# num2 = int(input("Ingrese otro número: "))

# # valida que ninguno de los números sea cero
# if num1 == 0 or num2 == 0:
#     print("No se permiten ceros. Reinicie el programa e intentelo de nuevo")
# else:
#     # calcula el producto de los dos números
#     result = num1 * num2
#     print(f"El resultado es: {result}")

# # evalúa si el resultado es mayor o menor a 1000
# if result > 5000:
#     print(f"el resultado {result} es bastante grande")
# else:
#     print(f"El resultado {result} es relativamente pequeño")

print("----------------------------------------------------")

print("Ejemplo N° [6]")

# solicito dos números enteros al usuario
nume = int(input("Ingrese un número: "))
nume2 = int(input("Ingrese otro número: "))

result1 = nume / nume2


if result1 <=99:
    print(f"El resultado {result1} es menor o igual a 99")
elif result1 >=100:
    print(f"El resultado {result1} es mayor o igual a 100")
elif result1 >=1000:
    print(f"El resultado {result1} es mayor a 1000")
elif result1 >=100000:
    print(f"El resultado {result1} es mayor o igual a 100000")
else:
    print("El número ingresado no es válido o coherente.")
    
print("----------------------------------------------------")
print("Ejemplo N° [7]")
fecha = int(input("Ingrese su año de naciminento: "))

if fecha >=1920 and fecha <=1940:
    print("perteneces a la generación Silenciosa")
elif fecha >=1946 and fecha <=1964:
    print("Perteneces a la generación Baby Boomer")
elif fecha >=1965 and fecha <=1979:
    print("Perteneces a la generación X")
elif fecha >=1980 and fecha <=2000:
    print("Perteneces a la generación Y")
elif fecha >=2001 and fecha <=2010:
    print("Perteneces a la generación Z")
else:
    print("Ingresa un año correcto o coherente")
print("----------------------------------------------------")
print("Ejemplo N° [8]: PROGRAMA DE CRÉDITO BANCARIO.")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad >=18:
    print("Eres mayor de edad, puedes pedir tu crédito bancario.")
elif edad <=17:
    print("No eres mayor de edad.")
else:
    print("Ingresa un dato correcto o coherente.")
print("----------------------------------------------------")
# print("Ejemplo N° [9]: PROGRAMA DE SALA DE JUEGOS.")

# edad = int(input("Ingrese la edad: "))
# if edad ==0 and edad <=4:
#     print("Entra gratis.")
# elif edad ==5 and edad <=18:
#     print("Paga 5 Euros.")
# elif edad >=19:
#     print("Paga 18 Euros.")
# else:
#     print("Ingresaste un dato incorrecto.")






