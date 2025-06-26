# ¿QUÉ ES ITERAR?
# En progrmación la iteración es la repetición de una segmento de código dentro de una programa de computadora.
# Iterar en matemática, se refiere al proceso de iteración de una función, aplicando la función repetidamente, usando la salida de una iteración como la entrada a la siguiente.

# ¿QUÉ ES WHILE?
# Se basa en repetir un bloque de código a partir de evaluar una condición lógica siempre que esta sea TRUE (al igual que la sentencia if). Este tipo de flujo se llama bucle porque después de ejecutar todas las intrucciones internas, vulve ariba para repetir. SI la condición es falsa la primera vez que se pasa el bucle, las sentencias del bucle no se ejecutan nunca.

# print("----------------------------------------------------")

# print("Ejemplo N° [1]")

# contador = int(input("Ingrese un número: "))
# # mientras contador sea mayor o igual a 1, se hará una cuenta regresiva hasta el número 1
# while contador >= 1:
#     print(f"Contador {contador}")
#     contador -= 1
# print("Terminó el contador")

# print("----------------------------------------------------")

# print("Ejemplo N° [2]")

# while True:
#     texto = input("Escribe algo (o escribe salir para terminar): ")
#     if texto == "salir":
#         break # break detiene inmediatamente un ciclo (while o for), aunque la condición del ciclo siga siendo verdadera
#     else:      
#         print(f"Escribiste la palabra o texto: {texto}")

# # Esto se ejecuta después del break
# print("Saliste del bucle o del programa")

# ¿QUÉ HACE WHILE TRUE?
# significa que el bucle nunca termina por sí solo, porque la condición TRUE siempre es verdadera. Para salir del bucle, debes usar la instrucción break

# print("----------------------------------------------------")

# print("Ejemplo N° [3]")

# num = int(input("Ingrese un número: "))

# while num > 0:
#     print(f"{num}")
#     num -= 1
# print("Terminó el conteo")

# 1: Declaramos la variable num y le pedimos al usuario que ingrese el número 
# 2: Usamos la sentencia while  para indicar que mientras num sea mayor a 0 entremos al bloque de código
# 3: Al evaluar num contra 0 nos indica que es TRUE
 
# print("----------------------------------------------------")

# print("Ejemplo N° [4]")

# # Pide al usuario un número 
# numero = int(input("Ingresa la tabla de multiplicar: "))
# # Se crea un contador con el número 1
# contador2 = 1

# while contador2 <= 10:
    
#     # Se calcula el resultado de multiplicarel número por el contador actual
#     resultado = numero * contador2
    
#     print(f"{numero} * {contador2} = {resultado} ") # Se muestra la multiplicación actual
    
#     # Se suma 1 al contador para pasar al siguiente número (ej: de 1 a 2)
#     contador2 += 1
    
# print("El programa ha finalizado")

# print("----------------------------------------------------")

# print("Ejemplo N° [5]")

# num2 = int(input("Ingrese un número: "))

# # Se repite mientras num2 sea menor o igual 5 
# while num2 <= 5:
#     print(f"{num2}") # muestra el valor actual de num2 
    
#     # Aumenta num2 en 1 para que avance al siguiente número
#     num2 += 1 

# print("----------------------------------------------------")

print("Ejemplo N° [6]")

# Supongamos que queremos que el usuario escriba una contraseña, y si nola escribe correctamente, el programa siga pidiéndola 

clave = input("Escriba su contraseña: ")

while clave != "Python123":
    print("Contraseña incorrecta")

