# ALGUNOS CONCEPTOS BÁSICOS CLAVE SON: 

# ¿QUÉ ES ITERAR?

# En programación, la iteración es la repetición de un segmento de código dentro de un programa. 
# Iterar, en matemáticas, también se refiere al proceso de aplicar una función repetidamente, usando el resultado anterior como entrada para la siguiente operación.

# ¿QUÉ ES WHILE?

# Es una estructura de control que repite un bloque de código mientras se cumpla una condición lógica (sea True), similar a un "if" pero que se repite en forma de bucle. 
# Una vez que se terminan de ejecutar las instrucciones dentro del bloque, el flujo vuelve arriba y verifica la condición otra vez.
# Si la condición es falsa desde el principio, el bloque no se ejecuta nunca.

# ¿QUÉ HACE WHILE TRUE?

# El bucle while True crea un ciclo infinito, es decir, un ciclo que se repite una y otra vez sin detenerse, porque la condición siempre es verdadera (True). 
# Esto es útil cuando no sabemos cuántas veces se repetirá el ciclo, y queremos que se siga ejecutando hasta que pase algo específico.
# Para poder salir de este tipo de bucle, se debe usar la instrucción 'break', que detiene el ciclo en el momento que se ejecuta, sin importar que la condición siga siendo True.

# print("------------------------------------------------------------")

# print("Ejemplo N° [1]")

# numero = int(input("Ingrese un número: "))

# # Bucle que se ejecuta mientras 'numero' sea mayor o igual a 1
# while numero >= 1: 
#     # Muestra el valor actual del 'numero'
#     print(f"Contador {numero}")
#     # Resta 1 al contador en cada vuelta (cuenta regresiva)
#     numero -= 1 
    
# print("\nEl contador ha terminado.")

# print("------------------------------------------------------------")

# print("Ejemplo N° [2]")

# # Bucle infinito: siempre se repite porque la condición "True" es siempre verdadera
# while True:
#     texto = input("Escribe algo (o escribe 'salir' para terminar): ")
    
#     # Si el usuario escribe exactamente "salir"
#     if texto == "salir":
#         break # El 'break' detiene el ciclo aunque la condición sea verdadera
#     else:      
#         # Si no escribió "salir", muestra lo que escribió
#         print(f"Escribiste la palabra o texto: {texto}")

# print("\nSaliste del bucle.")

# print("------------------------------------------------------------")

# print("Ejemplo N° [3]")

# numero_secreto = 21

# adivinanza = int(input("Adivina el número secreto entre 1 y 30: "))

# # Bucle que se repite mientras el número no sea correcto
# while adivinanza != numero_secreto:
#     print("Incorrecto. Intenta de nuevo.")
#     adivinanza = int(input("Adivina el número secreto entre 1 y 30: "))

# # Si acierta, sale del bucle y muestra este mensaje
# print("\n¡Correcto! Adivinaste el número secreto.")
 
# print("------------------------------------------------------------")

# print("Ejemplo N° [4]")

# while True:
    
#     numero2 = int(input("Ingresa la tabla de multiplicar: "))
    
#     # Reinicia el contador cada vez
#     contador = 1

#     # Imprime la tabla del número ingresado
#     while contador <= 10:
#         # Hace la operación
#         resultado = numero2 * contador
#         # Muestra el texto
#         print(f"{numero2} * {contador} = {resultado}")
#         # Agrega +1 a cada vuelta
#         contador += 1 

#     # Pregunta si quiere ingresar otra tabla
#     respuesta = input("¿Quieres ingresar otra tabla? (sí/no): ").lower()

#     # Si el usuario escribe 'no', se rompe el ciclo y termina
#     if respuesta != "sí":
#         break

# print("\nEl programa ha finalizado")

# print("------------------------------------------------------------")

# print("Ejemplo N° [5]")

# numero3 = int(input("Ingrese un número: "))

# if numero3 <= 10:
    
#     # Se repite mientras 'numero3' sea menor o igual 10 
#     while numero3 <= 10:
#         print(f"{numero3}") # muestra el valor actual de 'numero3'
        
#         # Aumenta 'numero3' en 1 para que avance al siguiente número
#         numero3 += 1 
    
# else:
#     print(f"El numero {numero3} es mayor a 3")

# print("\nFin del conteo.")
    
# print("------------------------------------------------------------")

# print("Ejemplo N° [6]")

# clave = input("Escriba su contraseña: ").lower()

# # Mientras la contraseña sea incorrecta (distinta de "3123")
# while clave != "3123":
#     # Muestra un mensaje de error
#     print("Contraseña incorrecta")
#     # Pide que intente de nuevo
#     clave = input("Intenta de nuevo: ")

# print("\nAcceso concedido. Bienvenido.")

# print("------------------------------------------------------------")

# print("Ejemplo N° [7]")

# numero4 = 1

# while numero4 <= 10:
    
#     # Se verifica si el número actual es par (al dividirlo entre 2, el residuo es 0)
#     if numero4 % 2 == 0:
#         print(f"El número {numero4} es par")
        
#     else:
#         print(f"El número {numero4} es impar") # Si no, impreme que es impar
    
#     # Se incrementa el número en 1 para evitar un bucle infinito
#     numero4 += 1

# print("\nFin del programa")

# print("------------------------------------------------------------")

# # "--- WHILE Y IF JUNTOS ---

# # WHILE: repite un bloque de código de mientras una condición sea verdadera. Ejemplo: 
# # IF: evalúa una condición. Si la condición se cumple (es verdadera), se ejecuta el bloque de código

# numero5 = int(input("Ingrese un número: "))

# if numero5 <= 20:
    
#     # Mientras el número ingresado sea menor a 20
#     while numero5 <= 20:
#         print(numero5)
#         # Le suma 1 a el número hasta llegar a 20
#         numero5 += 1 
# else:
#     print("Ingresa un número que sea menor a 20")
    
# print("\nFin del conteo.\n")

# print("---------------------------------------")

# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))

# # Si la edad es mayor a 18
# if edad >= 18:
#     print(f"{nombre}, tienes {edad} años. Eres mayor de edad")

# # De lo contrario, no es mayor de edad
# else:
#     print("No eres mayor de edad")

# print("---------------------------------------")

# continuar = input("¿Desea entrar al programa? (si/no): ")

# # Bucle que se repite mientras la respuesta sea 'si' (ignorando espacios y mayúsculas)
# while continuar.strip().lower() == "si":
    
#     nombre1 = input("Ingrese su nombre: ")
#     edad1 = int(input("Ingrese su edad: "))
    
#     # Verifica si la persona es mayor o menor de edad
#     if edad1 >= 18:
#         print(f"{nombre1}, tienes {edad1} años. Eres mayor de edad")
#     else:
#         print(f"{nombre1}, tienes {edad1} años. NO eres mayor de edad")
    
#     # Pregunta si se desea ingresar a otra persona
#     continuar = input("¿Desea ingresar a otra persona? (si/no): ")
    
# print("\nFin del programa")
    
# print("------------------------------------------------------------")


