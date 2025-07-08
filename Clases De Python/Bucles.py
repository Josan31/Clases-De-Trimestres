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

print("------------------------------------------------------------")

print("Ejemplo N° [3]")

num = int(input("Ingrese un número: "))

while num > 0:
    print(f"{num}")
    num -= 1
print("Terminó el conteo")

# 1: Declaramos la variable num y le pedimos al usuario que ingrese el número 
# 2: Usamos la sentencia while  para indicar que mientras num sea mayor a 0 entremos al bloque de código
# 3: Al evaluar num contra 0 nos indica que es TRUE
 
print("------------------------------------------------------------")

print("Ejemplo N° [4]")

# Pide al usuario un número 
numero2 = int(input("Ingresa la tabla de multiplicar: "))
# Se crea un contador con el número 1
contador2 = 1

while contador2 <= 10:
    
    # Se calcula el resultado de multiplicarel número por el contador actual
    resultado = numero2 * contador2
    
    print(f"{numero2} * {contador2} = {resultado} ") # Se muestra la multiplicación actual
    
    # Se suma 1 al contador para pasar al siguiente número (ej: de 1 a 2)
    contador2 += 1
    
print("El programa ha finalizado")

print("------------------------------------------------------------")

print("Ejemplo N° [5]")

num2 = int(input("Ingrese un número: "))

# Se repite mientras num2 sea menor o igual 5 
while num2 <= 5:
    print(f"{num2}") # muestra el valor actual de num2 
    
    # Aumenta num2 en 1 para que avance al siguiente número
    num2 += 1 

print("------------------------------------------------------------")

print("Ejemplo N° [6]")

# Supongamos que queremos que el usuario escriba una contraseña, y si nola escribe correctamente, el programa siga pidiéndola 

clave = input("Escriba su contraseña: ") # Pide contraseña por primera vez

# Mientras la contraseña esté mal
while clave != "3123":
    print("Contraseña incorrecta")
    clave = input("Intenta de nuevo: ") # Vuelve a pedir la contraseña
    
print("Acceso concedido. Bienvenido.")

# En este ejemplo el bucle while se repite mientas la clave escritra no sea igual a "3123". Si el usuario escribe la clave correcta, el bucle se detiene y da un mensaje de bienvenida.

print("------------------------------------------------------------")

print("Ejemplo N° [7]")

numero2 = 1

while numero2 <= 10:
    
    # Se verifica si el número actual es par (al dividirlo entre 2, el residuo es 0)
    if numero2 % 2 == 0:
        print(f"El número {numero2} es par")
        
    else:
        print(f"El número {numero2} es impar") # Si no, impreme que es impar
    
    # Se incrementa el número en 1 para evitar un bucle infinito
    numero2 += 1

print("Fin del programa")

print("------------------------------------------------------------")

# --- WHILE Y IF ---

# El bucle while repite un bloque de código de mientras una condicón sea verdadera

contador = int(input("Ingrese un número: "))

while contador <= 20:
    print(contador)
    contador += 1
    
# La instrucción if evalúa una condición. Si la condición se cumple (es verdadera), se ejecuta el bloque de código

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print(f"{nombre}, tienes {edad} años. Eres mayor de edad")
else:
    print("No eres mayor de edad")
    
# ¿CÓMO SE USAN JUNTOS?
# Puedes usar if dentro de un bucle while para formar una repetición 

continuar = input("¿Desea entrar al programa? (si/no): ")

while continuar.strip().lower() == "si":
    nombre1 = input("Ingrese su nombre: ")
    edad1 = int(input("Ingrese su edad: "))
    
    if edad1 >= 18:
        print(f"{nombre1}, tienes {edad1} años. Eres mayor de edad")
    else:
        print(f"{nombre1}, tienes {edad1} años. NO eres mayor de edad")
    
    continuar = input("¿Desea ingresar a otra persona? (si/no): ")
    
print("Fin del programa")
    
print("------------------------------------------------------------")

print("Ejemplo N° [8]") 
print("===== cajero automático =====".upper())

# El .strip() sirve para quitar los espacios al inicio y al final
# El .lower() sriev para convertir todo el texto a minúsculas
pregunta = input("¿Desea entrar al cajero automático? (si/no): ".strip().lower()) 

# si el usuario escribe si, se ejecuta el programa
if pregunta == "si":
    
    # Paso 1: Pedir los datos al usuario
    nombre2 = input("Ingrese su nombre de usuario: ")
    edad2 = int(input("Ingrese su edad: "))
    
    # Si la edad es menor a 18, no se permite continuar
    if edad2 < 18:
        print(f"{nombre2}, debes tener almenos 18 años para usar el cajero automático")
    else:
        clave2 = input("Escriba su contraseña: ")
  
        # Mientras la contraseña no sea "123456", sigue pidiendo que la escriba de nuevo 
        while clave2 != "123456":
            print(f"{nombre2}, Contraseña incorrecta.")
            clave2 = input(f"{nombre2}, intenta de nuevo: ")
    
        print("Acceso concedido. Bienvenido")
    
        # Paso 2: Menú de opciones 
        saldo = float(input("Ingrese su saldo actual: "))
        opciones = ""
        
        # Ciclo que muestra el menú hasta que el usuario elija la opción 3 (salir)
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
                
                # Si quiere retirar dinero, se verifica que tenga suficiente saldo
                if retiro <= saldo:
                    saldo -= retiro  # Se le resta el retiro al saldo
                    print(f"Has retirado ${retiro}. Saldo restante: ${saldo}")
                else:
                    print("Fondos insuficientes.")
                
            elif opciones == "3":
                print("Gracias por usar el cajero automático.¡Hasta pronto!")
            else:
                print(f"{nombre2}, La opción ingresada no es válida. intentalo de nuevo ")
             
# De lo contrario, si el usuario escribre no, el programa no incia   
else:
    print("Acceso al programa cancelado. ¡Que tengas buen dia!")

print("----------------------------------------------------")