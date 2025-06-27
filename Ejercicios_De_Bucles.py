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

# # Se crea una lista de frutas inciales en mayúscula
# frutas = ("manzana".upper(), "pera".upper(), "mango".upper(), "uva".upper(), "fresa".upper())

# while True:
#     frutas2 = input("Ingresa una fruta a adivinar: ").upper()
    
#     # Si la fruta ingresada por el usuario está en la tupla inicial
#     if frutas2 in frutas:
#         print("¡Acertaste una de las frutas!")
#         break
#     else:
#         print("No acertaste")

# # Mensaje para cuando finalice el bucle 
# print(f"La lista de frutas iniciales era: {frutas}. Y tú ingresaste {frutas2}, ¡Acertaste!")
# print("Fin del programa")
    
# print("----------------------------------------------------")

# print("Ejercicio N° [9]")

# # Se crea una lista con palabras iniciales y su traducción en inglés
# diccionario1 = {"camisa": "shirt", "desatornillador": "screwdriver", "cama": "bed", "ventana": "window", "flor": "flower", "arbol": "tree", "cielo": "sky", "tímido": "shy", "hola": "hi/hello"}

# while True:
#     palabra = input("Ingresa una palabra es español: ").lower()
    
#     # Si el usuario escribe fin, termina el programa
#     if palabra == "fin":
#         print("Elegiste salir del programa.")
#         break
    
#     # Si la palabra ingresada está en el diccionario
#     if palabra in diccionario1:
#         print(f"La traducción es {diccionario1[palabra]}")
        
#     # Si no, pide ingresar otra
#     else:
#         print(f"La palabra {palabra} no está. Escribe otra")
        
# print("Fin del programa")

# print("----------------------------------------------------")
    
# print("Ejercicio N° [10]")


# while True:
    
#     # Se crea el menú de inicio
#     print("\n===== MENÚ =====")
#     print("1. SUMA")
#     print("2. RESTA")
#     print("3. MULTIPLICACIÓN")
#     print("4. DIVISIÓN")
#     print("5. SALIR\n")
    
#     # Pide al usuario ingresar una opción de 1 a 5
#     opcion = input("Elige una opción (1-5): ").lower()
    
#     # Ejecuta el bloque para la opción 1
#     if opcion == "1":
#         print("Elejiste la opción 1 (SUMA)")
#         num1 = int(input("Ingresa un número: "))
#         num2 = int(input("Ingresa otro número: "))
        
#         resultado = num1 + num2
        
#         print(f"\nLa suma entre {num1} y {num2} es: {resultado}")
    
#     # Ejecuta el bloque para la opción 2
#     elif opcion == "2":
#         print("Elejiste la opción 2 (RESTA)")
#         num3 = int(input("Ingresa un número: "))
#         num4 = int(input("Ingresa otro número: "))
        
#         resultado2 = num3 - num4
        
#         print(f"\nLa resta entre {num3} y {num4} es: {resultado2}")
        
#     # Ejecuta el bloque para la opción 3
#     elif opcion == "3":
#         print("Elejiste la opción 3 (MULTIPLICACIÓN)")
#         num5 = int(input("Ingresa un número: "))
#         num6 = int(input("Ingresa otro número: "))
        
#         resultado3 = num5 * num6
        
#         print(f"\nLa multiplicación entre {num5} y {num6} es: {resultado3}")
    
#     # Ejecuta el bloque para la opción 4
#     elif opcion == "4":
#         print("Elejiste la opción 4 (DIVISIÓN)")
#         num7 = int(input("Ingresa un número: "))
#         num8 = int(input("Ingresa otro número: "))
        
#         if num8 == 0:
#             print("No se puede dividir entre 0")
#         else:
#             resultado4 = num7 / num8
#             print(f"\nLa división entre {num7} y {num8} es: {resultado4}")
    
#     # Ejecuta el bloque para la opción 5
#     elif opcion == "5":
#         print("!Hasta pronto¡")
#         break # Rompe el bucle infinito
    
#     # Si no se cumple ninguna de las opciones anteriores, el bucle sigue 
#     else:
#         print("Opción no válida, intente de nuevo")

# # Cuando salgo del bucle saldré el mensaje
# print("Fin del programa")
        
# print("----------------------------------------------------")

# print("Ejercicio N° [11]")

# # Lista vacía inicial
# personas = {}

# while True:
#     nombre_p = input("Ingresa el nombre a registrar: ").lower()
    
#     # Finaliza el bucle si el usuario escribe salir
#     if nombre_p == "salir":
#         print("Saliste del programa con 'salir'")
#         break # rompe el bucle 
    
#     edad_p = int(input("Ingresa la edad de la persona registrada: "))
    
#     # Se gurdan las personas ingresadas y su edad a la lista vacía inicial
#     personas[nombre_p] = edad_p
    
#     # Le dice al usuario si quiere agregar otra persona 
#     continuar = input("¿Deseas ingresar otra persona? (si/no): ").lower()
    
#     if continuar == "si":
#         print("Continúa...")
#     else:
#         print("Saliste del programa con 'no'")
#         break # rompe el bucle
         
# print(f"\nEl diccionario final de personas es: {personas}")
# print("Fin del programa")

# print("----------------------------------------------------")

# print("Ejercicio N° [12]")

# colores = ["amarillo", "azul", "rojo", "verde", "negro"]

# while True:
#     color2 = input("Ingresa un color: ").lower()  # Con .lower() no importa si escribe en mayúscula
    
#     # Si el color ingresado está en la lista incial de colores
#     if color2 in colores:
#         print(f"¡Correcto! El color '{color2}' está en la lista.")
#         break # rompe el bucle
    
#     # Si el color no está, se repite el bucle 
#     else:
#         print(f"El color '{color2}' no está en la lista. Intenta otra vez.")
        
# print("Fin del programa")

# print("----------------------------------------------------")

# print("Ejercicio N° [13]")

# while True:
#     num1 = int(input("Ingresa un número: "))
#     potencia = 1 # Se crea un contador 
  
#     while potencia <= 5:
#         result = num1 ** potencia
#         print(f"\nEl número {num1} elevado a la {potencia} es: {result}")
#         potencia += 1 # En cada bucle se le sumará un 1 el contador

#     # Pregunta si desea ingresar otro dato
#     continuar2 = input("\n¿Deseas ingresar otro número? (si/no): ").lower()
    
#     # Si continúa, el bucle se repite
#     if continuar2 == "si":
#         print("Continúa...\n")
#     else:
#         print("¡Hasta pronto!")
#         break  # sale del bucle principal

# print("Fin del programa")

# print("----------------------------------------------------")

# print("Ejercicio N° [14]")

# cuadrados = []
# contador = 0

# # Mientras el contador sea menor a 5 se le sumará +1 en la siguente vuelta
# while contador < 5:
#     num2 = int(input("Ingresa un número: "))
#     cálculo = num2 ** 2
#     cuadrados.append(cálculo) # Agrego el número ingresado a listas 
    
#     print(f"El cuadrado de {num2} es {cálculo}")
#     contador += 1 # Procede con el siguiente número

# # Cuando sale del bucle 
# print(f"\nLista de cuadrados ingresados: {cuadrados}")
# print("Fin del programa")

# print("----------------------------------------------------")

# print("Ejercicio N° [15]")

# estudiantes = {}

# while True:
#     nombre_e = input("Ingresa el nombre del estudiante: ").lower()
    
#     # Si el usuario escribe fin en el nombre, finaliza el programa
#     if nombre_e == "fin":
#         print("Programa finalizado")
#         break
    
#     nota_f = float(input("Ingresa su nota final: "))
    
#     # Guarda el nombre y la nota del estudiante en el diccionario inicial
#     estudiantes[nombre_e] = nota_f
    
#     # Pregunta al usuario si desea continuar 
#     continuar3 = input("¿Desea ingresar otro estudiante? (si/no): ").lower()
    
#     if continuar3 == "si":
#         print("puede continuar")
#     else:
#         print("Programa detenido")
#         break

# print(f"la lista completa de estudiantes ingresados es: {estudiantes}")
# print("Fin del programa")
