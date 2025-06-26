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

# print("Ejemplo N° [6]")

# # Supongamos que queremos que el usuario escriba una contraseña, y si nola escribe correctamente, el programa siga pidiéndola 

# clave = input("Escriba su contraseña: ") # Pide contraseña por primera vez

# # Mientras la contraseña esté mal
# while clave != "3123":
#     print("Contraseña incorrecta")
#     clave = input("Intenta de nuevo: ") # Vuelve a pedir la contraseña
    
# print("Acceso concedido. Bienvenido.")

# # En este ejemplo el bucle while se repite mientas la clave escritra no sea igual a "3123". Si el usuario escribe la clave correcta, el bucle se detiene y da un mensaje de bienvenida.

# print("----------------------------------------------------")

# # --- WHILE Y IF ---

# # El bucle while repite un bloque de código de mientras una condicón sea verdadera

# contador = int(input("Ingrese un número: "))

# while contador <= 20:
#     print(contador)
#     contador += 1
    
# # La instrucción if evalúa una condición. Si la condición se cumple (es verdadera), se ejecuta el bloque de código

# nombre = input("Ingrese su nombre: ")
# edad = int(input("Ingrese su edad: "))

# if edad >= 18:
#     print(f"{nombre}, tienes {edad} años. Eres mayor de edad")
# else:
#     print("No eres mayor de edad")
    
# # ¿CÓMO SE USAN JUNTOS?
# # Puedes usar if dentro de un bucle while para formar una repetición 

# continuar = input("¿Desea entrar al programa? (si/no): ")

# while continuar.strip().lower() == "si":
#     nombre1 = input("Ingrese su nombre: ")
#     edad1 = int(input("Ingrese su edad: "))
    
#     if edad1 >= 18:
#         print(f"{nombre1}, tienes {edad1} años. Eres mayor de edad")
#     else:
#         print(f"{nombre1}, tienes {edad1} años. NO eres mayor de edad")
    
#     continuar = input("¿Desea ingresar a otra persona? (si/no): ")
    
# print("Fin del programa")
    
# print("----------------------------------------------------")

print("Ejemplo N° [7]") 
print("===== cajero automático =====".upper())

# Pregunta incial 
pregunta = input("¿Desea entrar al cajero automático? (si/no): ".strip().lower())

if pregunta == "si":
    # Paso 1: Pedir los datos al usuario
    nombre2 = input("Ingrese su nombre de usuario: ")
    edad2 = int(input("Ingrese su edad: "))
    
    # Validación de edad mínima
    if edad2 < 18:
        print(f"{nombre2}, debes tener almenos 18 años para usar el cajero automático")
    else:
        clave2 = input("Escriba su contraseña: ")
  
        # Validación de clave ingresada 
        while clave2 != "123456":
            print(f"{nombre2}, Contraseña incorrecta.")
            clave2 = input(f"{nombre2}, intenta de nuevo: ")
    
        print("Acceso concedido. Bienvenido")
    
        # Paso 2: Menú de opciones 
        saldo = float(input("Ingrese su saldo actual: "))
        opciones = ""
    
        while opciones != "3":
            
            print("\n---- MENÚ ----")
            print("1. Consultar saldo.")
            print("2. Retirar dinero.")
            print("3. Salir.")
        
            opciones = input("\nSeleccione una de las opciones (1/2/3): ")
        
            if opciones == "1":
                print(f"{nombre2}, tu saldo actual es: ${saldo}")
            elif opciones == "2":
                retiro = int(input("Ingrese la cantidad a retirar: "))
            
                if retiro <= saldo:
                    saldo -= retiro  
                    print(f"Has retirado ${retiro}. Saldo restante: ${saldo}")
                else:
                    print("Fondos insuficientes.")
                
            elif opciones == "3":
                print("Gracias por usar el cajero automático.¡Hasta pronto!")
            else:
                print(f"{nombre2}, La opción ingresada no es válida. intentalo de nuevo ")
                
else:
    print("Acceso al programa cancelado. ¡Que tengas buen dia!")
