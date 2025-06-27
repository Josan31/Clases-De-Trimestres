# print("------------------------------------------------")
# print("ejercicios con while, condicionales y estructura".upper())
# print("------------------------------------------------")

# print("----------------------------------------------------")

# print("Ejercicio N° [1]")

# print("Ingresa dos números. Si alguno es 0, el programa terminará.")
# numero1 = int(input("Ingresa un número: "))
# numero2 = int(input("Ingresa otro número: "))

# # # Mientras ambos números sean diferentes de 0, se seguirán sumando
# while numero1 != 0 and numero2 != 0:
#     resultado = numero1 + numero2 
    
#     # Se muestra el resultado al usuario
#     print(f"La suma entre los números {numero1} y {numero2} es de: {resultado}")
    
#     # Se piden nuevos números para repetir el proceso
#     numero1 = int(input("Ingresa un número: "))
#     numero2 = int(input("Ingresa otro número: "))
    
# # Cuando alguno de los dos números es 0, se termina el programa
# print("Fin del programa")

# print("----------------------------------------------------")

# print("Ejercicio N° [2]")

# # Pide contraseña por primera vez
# clave = input("Escriba su contraseña: ") 

# # Mientras la contraseña esté mal
# while clave != "python123":
#     print("Contraseña incorrecta")
    
#     # Vuelve a pedir la contraseña
#     clave = input("Intenta de nuevo: ")

# # Sale del bucle
# print("Acceso concedido. Bienvenido.")

# print("----------------------------------------------------")

# print("Ejercicio N° [3]")

# # Se crea una lista vacía para guardar lo que escriba el usuario
# productos = []

# producto = input("Ingrese un producto (escriba 'fin' para terminar): ".lower())

# # Mientras el usuario no escriba "fin", el bucle continúa
# while producto != "fin":
    
#     # Se agrega el producto a la lista vacía
#     productos.append(producto)
    
#     # Se vuelve a pedir otro producto
#     producto = input("Ingrese un producto: ".lower())

# print(f"Tu lista es: {productos}")
# print("Fin del programa")

# print("----------------------------------------------------")

# print("Ejercicio N° [4]")

# numero2 = 1

# while numero2 <= 10:
    
#     # Se verifica si el número actual es par (al dividirlo entre 2, el residuo es 0)
#     if numero2 % 2 == 0:
#         print(f"El número {numero2} es par")
        
#     else:
#         print(f"El número {numero2} es impar") # Si no, impreme que es impar
    
#     # Se incrementa el número en 1 para evitar un bucle infinito
#     numero2 += 1

# print("Fin del programa")

# print("----------------------------------------------------")

print("Ejercicio N° [5]")

# print("----------------------------------------------------")
    
# print("Ejercicio N° [6]")

# numero3 = int(input("Ingresa la tabla de multiplicar: "))

# # Se crea un contador con el número 1
# contador2 = 1

# while contador2 <= 10:
    
#     # Se calcula el resultado de multiplicar el número por el contador actual
#     resultado = numero3 * contador2
    
#     print(f"{numero3} * {contador2} = {resultado} ") # Se muestra la multiplicación actual
    
#     # Se suma 1 al contador para pasar al siguiente número (ej: de 1 a 2)
#     contador2 += 1
    
# print("El programa ha finalizado")

# print("----------------------------------------------------")

# print("Ejercicio N° [7]")

# nombre = input("Ingresa tu nombre: ")

# # Contador de intentos
# intentos = 0

# # Primer intento
# numero = int(input("Adivina el número: "))
# intentos = intentos + 1  # Aumenta el intento

# # Mientras el número ingresado no sea igual a 485 
# while numero != 485:
#     if numero < 485:
#         print(f"Al número {numero} le falta")
#     else:
#         print(f"Al número {numero} se pasa")
    
#     # Nuevo intento
#     numero = int(input("Intenta de nuevo. Ingresa un número: "))
#     intentos = intentos + 1  # Aumenta el intento

# # Mensaje final cuando adivina
# print(f"{nombre}, el número correcto era 485. ¡Adivinaste, felicidades!")
# print(f"Lo lograste en {intentos} intentos.")
# print("Fin del programa")

# print("----------------------------------------------------")

# print("Ejercicio N° [8]")

# frutas = ("manzana".upper(), "pera".upper(), "mango".upper(), "uva".upper(), "fresa".upper())

# while True:
#     frutas2 = input("Ingresa una fruta a adivinar: ").upper()
    
#     if frutas2 in frutas:
#         print("¡Acertaste una de las frutas!")
#         break
#     else:
#         print("No acertaste")

# print(f"La lista de frutas iniciales era: {frutas}. Y tú ingresaste {frutas2}, ¡Acertaste!")
# print("Fin del programa")
    
# print("----------------------------------------------------")

print("Ejercicio N° [9]")


    