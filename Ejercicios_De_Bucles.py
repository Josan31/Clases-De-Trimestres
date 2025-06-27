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