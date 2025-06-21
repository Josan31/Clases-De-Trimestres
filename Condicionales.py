# ¿QUÉ ES EL FLUJO? 
# El flujo es una forma de entender la sucesion de las instrucciones de un programa, estas instrucciones se ejecutan una depues de otra de forma ordenada y suelen tener el objetivo final de manipular informacion.
print("--------------------------------------------------------------------------------")
# ¿QUÉ ES UN DIAGRAMA DE FLUJO?
# Expresan nuestros algoritmos en forma de diagrama mediante una representación gráfica basada en figuras geométricas que varían segun la estructura del código.
print("--------------------------------------------------------------------------------")
# CONDICIONALES 
# Se utilizan los operadores relacionales (==, !, >, <, etc.) y para evaluar más de una condicón simultáneamente se utilizan los operadores lógicos (not, and, or). las condiconales se deifnnen mediante el uso de tres palabras claves reservadas: if, elif, else.
print("-----------------------------------------")
print("Ejemplo N° [1]")

# solicito el nombre al usuario
nombre = int(input("Ingrese su nombre: "))

# solicito la edad al usuario
edad = int(input("Ingrese su edad: "))

# esta condicion se ejecuta si el usuario tiene más de 18 años
if edad >=18:
    print(f"{nombre}, Tienes {edad} años. Eres mayor de edad.")
# si el usuario tiene una edad mayor a 0 y es menor de 18
elif edad <18 and edad >0:
    print(f"{nombre}, Tienes {edad} años. Eres menor de edad.")
# si el dato que el usuario ingrese es incorrecto
else:
    print("Dato incorrecto")
print("-----------------------------------------")
print("Ejemplo N° [2]")

a = float(input("Ingresa un numero: "))
b = float(input("Ingresa otro número: "))
c = float(input("Ingresa un último número: "))
if a > b and c > a:
    print(f"Ambas condiciones son verdaderas")
else: 
    print("Una de las condiciones es falsa")
print("-----------------------------------------")
print("Ejemplo N° [3]")
numero = float(input("Ingrese un número: "))
if numero > 36:
    print("El numero es grande.")
else:
    print("El número es pequeño.")
print("-----------------------------------------")
print("Ejemplo N° [4]")
x = int(input("Ingrese un número: "))
if x >10:
    print("El número está por encima de 10")
    if x >20:
        print("El número está por encima de 20")
        if x >30:
            print("Y tambien por encima de 30")
else:
    print("Está debajo de 10")
print("-----------------------------------------")
print("Ejemplo N° [5]")
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
result = num1 * num2
print(f"El resultado es: {result}")
print("-----------------------------------------")
print("Ejemplo N° [6]")
if result <=99:
    print("El resultado es menor o igual a 99")
elif result >=100:
    print("El resultado es mayor o igual a 100")
elif result >=1000:
    print("El resultado es mayor a 1000")
elif result >=100000:
    print("El resultado es mayor o igual a 100000")
else:
    print("El número ingresado no es válido o coherente.")
print("-----------------------------------------")
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
print("-----------------------------------------")
print("Ejemplo N° [8]: PROGRAMA DE CRÉDITO BANCARIO.")

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad >=18:
    print("Eres mayor de edad, puedes pedir tu crédito bancario.")
elif edad <=17:
    print("No eres mayor de edad.")
else:
    print("Ingresa un dato correcto o coherente.")
print("-----------------------------------------")
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






