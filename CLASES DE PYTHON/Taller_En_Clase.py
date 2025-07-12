print("---------------- TALLER EN CLASE ----------------")

print("\n[1]")

# Solicita dos números al usuario 
num1 = int(input("Por favor, ingrese un número: "))
num2 = int(input("Por favor, ingrese un segundo número: "))
op = num1 + num2

# Muestra su suma
print(f"La suma de {num1} y {num2} es de: {op}")

# ------------------------

print("\n[2]")

# Solicita dos números al usuario
num3 = int(input("Por favor, ingrese un número: "))
num4 = int(input("Por favor, ingrese un segundo número: "))
op2 = num3 - num4 

# Muestra su resta
print(f"La resta entre {num3} y {num4} es de: {op2}")

# ------------------------

print("\n[3]")

# Pide dos números al usuario.
num5 = int(input("Por favor, ingrese un número: "))
num6 = int(input("Por favor, ingrese un segundo número: "))
op3 = num5 * num6

# Muestra su multiplicación
print(f"La multiplicación entre {num5} y {num6} es de: {op3}")

# ------------------------

print("\n[4]")

# Pide dos números al usuario
num7 = int(input("Por favor, ingrese un número: "))
num8 = int(input("Por favor, ingrese un segundo número: "))
op4 = num7 / num8

# Muestra su división
print(f"La división entre {num7} y {num8} es de: {op4}")

# ------------------------

print("\n[5]")

# Solicita nombre y apellido 
name1 = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")

# Muestra una bienvenida
print(f"¡Hola {name1} {last_name} bienvenido!")

# ------------------------

print("\n[6]")

name2 = input("Ingrese su nombre: ")

# Muestra la primera letra del nombre ingresado.
primera = name2[0]

print(f"{name2} la primera letra de su nombre es: {primera}")

# ------------------------

print("\n[7]")

palabra1 = input("Ingrese una palabra: ")

# Muestra la última letra de una palabra.
ultima = palabra1[-1]

print(f"La última letra de la palabra {palabra1} es: {ultima}")

# ------------------------

print("\n[8]")

base = int(input("Ingrese una base: "))
altura = int(input("Ingrese la altura: "))

# Calcula el área de un rectángulo con base y altura dadas.
op5 = base * altura

print(f"El área del rectángulo es: {op5}")

# ------------------------

print("\n[9]")

edad = int(input("Ingrese su edad: "))

# Calcula el año de nacimiento a partir de la edad.
op6 = 2025 - edad

print(f"Naciste en el año {op6}. Actualmente tienes {edad}")

# ------------------------

print("\n[10]")

# Forma un correo con nombre de usuario y dominio.
usuario = input("Ingrese su nombre de usuario: ")
dominio = input("Ingrese un dominio: ")

print(f"{usuario}@{dominio}")

# ------------------------

print("\n[11]")

name3 = input("Ingrese su nombre: ")

# Muestra la cantidad de letras que tiene tu nombre.
op6 = len(name3)

print(f"{name3} tu nombre tiene {op6} letras")

# ------------------------

print("\n[12]")

palabra2 = input("Ingrese una palabra: ")
palabra3 = input("Ingrese otra palabra: ")

# Une dos palabras ingresadas por el usuario.
print("La unión de las dos palabras queda:", palabra2 + palabra3)

# ------------------------

print("\n[13]")

palabra4 = input("Ingrese una palabra: ")

# Muestra la segunda letra de una palabra.
segundaL = palabra4[1]

print(f"La segunda letra de la palabra {palabra4} es: {segundaL}")

# ------------------------

print("\n[14]")

palabra5 = input("Ingrese una palabra: ")

# Muestra las tres primeras letras de una palabra.
segundaL2 = palabra5[0:3]

print(f"Las tres primeras letras de la palabra {palabra5} son: {segundaL2}")

# ------------------------

print("\n[15]")

palabra6 = input("Ingrese una palabra: ")

# Invierte la palabra 
op7 = palabra6[::-1]

# Muestra la palabra escrita al revés.
print(f"Las letras inversas de la palabra {palabra6} son: {op7}")

# ------------------------

print("\n[16]")

nu1 = int(input("Ingrese un número: "))
nu2 = int(input("Ingrese otro número: "))

# Realiza las 4 operaciones básicas con dos números.
suma = nu1 + nu2
resta = nu1 - nu2
multi = nu1 * nu2
division = nu1 / nu2

print(f"La suma fue {suma}, la resta fue {resta}, la multiplicación fue {multi}, y la división fue {division}")

# ------------------------

print("\n[17]")

nu3 = int(input("Ingrese un número: "))

# Calcula el doble de un número.
doble = nu3 * 2

print(f"El doble de {nu3} es {doble}")

# ------------------------

print("\n[18]")

nu4 = int(input("Ingrese un número: "))

# Calcula la mitad entera de un número.
mitad = nu4 // 2

print(f"La mitad de {nu4} es {mitad}")

# ------------------------

print("\n[19]")

frase = input("Ingrese una frase: ")

# Arroja la cantidad de caracteres 
op8 = len(frase)

# Muestra cuántos caracteres tiene una frase.
print(f"Tu frase tiene {op8} letras")

# ------------------------

print("\n[20]")

palabra5 = input("Ingrese una palabra: ")

# Imprime una palabra tres veces seguidas.
print(palabra5 * 3)

# ------------------------

print("\n[21]")

name4 = input("Ingrese su nombre: ")

# Muestra las 2 primeras y 2 últimas letras del nombre.
op9 = name4[0:2]
op10 = name4[-2:]

print(f"Las dos primeras letras son {op9} y las dos últimas son {op10}")

# ------------------------

print("\n[22]")

frase = input("Ingrese una frase: ")

# Muestra la letra que está en la mitad de una frase.
op1 = len(frase)
op2 = op1 // 2
op3 = frase[op2]

print(f"La letra del medio de la frase '{frase}' es '{op3}'")

# ------------------------

print("\n[23]")

frase2 = input("Ingrese una frase: ")

# Muestra los primeros 10 caracteres de una frase.
op4 = frase2[0:10]

print(f"Los 10 primeros caracteres de la frase son: {op4}")

# ------------------------

print("\n[24]")

nume = int(input("Ingrese un número: "))

# Calcula el cuadrado de un número.
op5 = nume ** 2

print(f"El número {nume} al cuadrado es: {op5}")

# ------------------------

print("\n[25]")

nume1 = int(input("Ingrese un número: "))
nume2 = int(input("Ingrese otro número: "))

# Verifica si el primer número es mayor que el segundo
if nume1 > nume2:
    print(f"El numero {nume1} es mayor que {nume2}")
    
# Verifica si el primer número es menor que el segundo
elif nume2 > nume1:
    print(f"El numero {nume2} es mayor que {nume1}")
    
# Si no es ninguna de las otras dos, significa que los números son iguales
else:
    print("Los dos números son iguales")

# ------------------------

print("\n[26]")

edad = int(input("Ingrese su edad: "))

# Estima cuántos días ha vivido una persona.
op6 = edad * 365

print(f"Has vivido aproximadamente {op6} días")

# ------------------------

print("\n[27]")

frase3 = input("Escribe la palabra 'perro': ")

# Muestra la palabra "perro" separada por letras.
op7 = "\np\n e\n r\n r\n o"

print(f"La palabra por letras es: {op7}")

# ------------------------

print("\n[28]")

frase4 = input("Ingrese una frase: ")

# Indica si una frase tiene más de 5 caracteres.
op8 = len(frase4)

if op8 > 5:
    print(f"La frase {frase4} tiene mas de 5 letras ")
else:
    print("La frase no tiene mas de 5 letras o caracter incorrecto")
    
# ------------------------

print("\n[29]")

numero1 = int(input("Ingrese un número: "))

# Multiplica un número por 10.
op9 = numero1 * 10

print(f"El número {numero1} multiplicado por 10 es {op9}")

# ------------------------

print("\n[30]")

# Convierte una palabra a mayúsculas y minúsculas.
mayus = input("Escribe una palabra: ")
print(f"En mayúsculas: {mayus.upper()}")  # Convierte a MAYÚSCULAS
print(f"En minúsculas: {mayus.lower()}")  # Convierte a minúsculas
