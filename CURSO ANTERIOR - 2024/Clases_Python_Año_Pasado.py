print("-------------------------------------------------------------------------------------------------")
print("INICIO")

#Creacion de variables
Nombre = "José Sánchez"
Institución = "\nsena"
Ciudad = "\npalmira"
Año = 2024

#Se le asigna texto a esas variables
print("\nMi nombre es:",Nombre)
print("\nMi institución es:",Institución)
print("\nMi ciudad es:",Ciudad)
print("\nEl año de mi proyecto es:",Año)

print("-------------------------------------------------------------------------------------------------")
print("SUMA(+)")

#CREAMOS VARIABLES
numero_1 = 34
numero_2 = 27

resultado = (numero_1 + numero_2) #Se hace la suma de las variables creando una nueva

#Se ejecuta con un print
print("\nEl resultado de la primera suma es:",resultado)

#CREAMOS VARIABLES
number_1 = 3897
number_2 = 547
number_3 = 2871

Final_result = (number_1 + number_2 + number_3) #Se hace la suma de las variables creando una nueva

#Se ejecuta con un print
print("\nEl resultado de la segunda suma es:",Final_result)

#CREAMOS VARIABLES
Number_1 = 61
Number_2 = 7315

total = (Number_1 + Number_2)

print("\nEl resultado de la tercera suma es:",total)

numero = int(input("Introduce el primer numero: "))
numero1 = int(input("Introduce el segundo numero: "))

suma = numero + numero1
print("La suma de", numero, "y", numero1, "es", suma)

print("-------------------------------------------------------------------------------------------------")
print("RESTA(-)")

#CREAMOS VARIABLES
numero1 = 8854
numero2 = 1756

total = (numero1 - numero2)

print("\nEl resultado de la primera resta es:",total)

#CREAMOS VARIABLES
numero_1 = 795478
numero_2 = 654321

resultado = (numero_1 - numero_2)

print("\nEl resultado de la segunda resta es:",resultado)

total_final = (total - resultado)

print("\nEl resultado entre los dos resultados de las restas es:",total_final)

print("-------------------------------------------------------------------------------------------------")
print("DIVISION(/)")

#CREAMOS VARIABLES
number1 = 872934
number2 = 643218

result = (number1 / number2)

print("\nEl resultado de la primera division es:",result)

#CREAMOS VARIABLES
number3 = 957277
number4 = 254328

total_final = (number3 / number4)

print("\nEl resultado de la segunda divion es:",total_final)

#Se crea otra variable para dividir los dos resultados de las operaciones
total = (result / total_final)

print("\nEl resultado entre los dos resultados de las divisiones es:",total)

print("-------------------------------------------------------------------------------------------------")
print("DIVISION ENTERA(//)")

#CREAMOS VARIABLES
number1 = 872934
number2 = 643218

result = (number1 // number2) #Se hace la divison de las variables creando una nueva

#Se ejecuta con un print
print("\nEl resultado de la primera division es:",result)

#CREAMOS VARIABLES
number3 = 957277
number4 = 254328

total_final = (number3 // number4) #Se hace la divison de las variables creando una nueva

#Se ejecuta con un print
print("\nEl resultado de la segunda divion es:",total_final)

#Se crea otra variable para dividir los dos resultados de las operaciones
total = (result // total_final)

#Se ejecuta con un print
print("\nEl resultado entre los dos resultados de las divisiones es:",total)

print("-------------------------------------------------------------------------------------------------")
print("MULTIPLICACIÓN(*)")

#CREAMOS VARIABLES
numero1 = 34578
numero2 = 2569
numero3 = 7108

#Se hace la multiplicación de las variables creando una nueva
final_result1 = (numero1 * numero2 * numero3)

#Se ejecuta con un print
print("\nEl resultado de la primera operacion es:",final_result1)

#CREAMOS VARIABLES
numb1 = 625476
numb2 = 32571
numb3 = 54321
numb4 = 8761

#Se hace la multiplicación de las variables creando una nueva
final_result2 = (numb1 * numb2 * numb3 * numb4)

#Se ejecuta con un print
print("\nEl resultado de la segunda operacion es:",final_result2)

#Se crea otra variable para multiplicar los dos resultados de las operaciones
total = (final_result1 * final_result2)

print("\nEl total final de los dos resultados de las multiplicaciones es:",total) 

print("-------------------------------------------------------------------------------------------------")
print("EXPONENTES(**)")

#CREAMOS VARIABLES
number_1 = 25**10
number_2 = 34**5
number_3 = 80**9

#Ponemos texto a las variables con su respectiva ecuación
result1 = (number_1)
print("\nEl primer resultado es:",result1)
result2 = (number_2)
print("\nEl segundo resultado es:",result2)
result3 = (number_3)
print("\nEl tercer resultado es:",result3)
    
print("-------------------------------------------------------------------------------------------------")
print("CONCATENACION Y EXTRACCIÓN")

mens1 = "El dia #24 de diciembre "
mens1 += "es un dia muy especial "
mens1 += "porque hay reuniones familiares "
mens1 += "y me traen muchos regalos "

#mostramos el mensaje completo
print("\nMensaje completo:")
print(mens1)


#buscamos la posicion de la palabra "dia"
inicio_mens1 = mens1.find("dia")
print("\nPosicion de la palabra 'dia':", inicio_mens1)

#buscamos la posicion de la palabra "regalos" 
busqueda_mens1 = mens1.find("regalos")
print("\nPosición de la palabra 'regalos':", busqueda_mens1)

#extraccion desde "dia" hasta "regalos"
extraccion_mens1 = mens1[inicio_mens1:busqueda_mens1 + len("regalos")]
print("\nTexto extraído (desde 'día' hasta 'regalos'):", extraccion_mens1)

mens1 = "Adicional America ganara, "
mens2 = "comprare mucha ropa "
mens3 = "y sera excelente "

print( mens1 + mens2 + mens3 )

print("-------------------------------------------------------------------------------------------------")
print("BUSQUEDA Y EXTRACCIÓN")

#BUSQUEDA DE LA PALABRA "HOLA" EN "HOLA MUNDO"
mensaje1 = "hola mundo"
busqueda_mensaje1 = mensaje1.find("hola") #busca "hola" en "hola mundo"

print("\nLa palabra 'hola' se encuentra en el índice:0")

#EXTRACCION DE UNA SUBCADENA DESDE EL INDICE 2 HASTA EL 7
men1 = "hola mundo"
extraccion_men1 = men1[2:7]

print("\nLa cadena extraida es:", extraccion_men1)

print("-------------------------------------------------------------------------------------------------")
print("(TIPOS DE DATOS)")

DIA_TEMA_VISTO = "2024-11-28"
print("\nLa fecha especifica es:", DIA_TEMA_VISTO)

print("\n1.NUMERICOS")
#Se usan para almacenar valores  numericos
print("\nENTEROS(int)")
W = -5
X = 18
Y = 7
Z = 16

numbe1 = 150
numbe2 = 34

print("\nel numero",numbe1,"es tipo:",numbe1,type(numbe1))

print("\nel numero",numbe2,"es tipo:",numbe2,type(numbe2))


print("\nNUMEROS FLOTANTES (float)")
numbe = 150.875743
numbe_1 = 34.3425267

print("\nel numero",numbe,"es tipo:",numbe,type(numbe))

print("\nel numero",numbe_1,"es tipo:",numbe_1,type(numbe_1))


print("\nTIPO BOOLEANO (False or True)")
number1 = 150.875743
number2 = 4

comparacion = numbe1 == numbe2
print("\nLa comparacion es:",comparacion)  

print("-------------------------------------------------------------------------------------------------")
print("(ENTRADA DE DATOS)")

#Creamos las variables
Nombre = input("Porfavor ingrese su nombre: ")
Apellido = input("Porfavor ingrese su apellido: ")
Ciudad = input("Porfavor ingrese su ciudad donde vive: ")
Edad = int(input("porfavor ingrese su edad: "))
Año = int(input("Porfavor ingrese el año actual: "))

#Se ejecutan las variables
print("\nEl nombre registrado fue:",Nombre)
print("\nEl nombre registrado fue:",Apellido)
print("\nLa ciudad que fue registrada fue:",Ciudad)
print("\nLa edad registrada fue:",Edad)
print("\nEl año registrado fue:",Año)

#Para multiplicar datos
# Solicitar los números a multiplicar, permitiendo decimales
Numero1 = float(input("\nIngrese el primer número a multiplicar: "))
Numero2 = float(input("Ingrese el segundo número a multiplicar: "))

Resul_t = Numero1 * Numero2

print(Nombre,Apellido,"Su resultado de la multiplicacion fue: ",Resul_t)

#Calcular el promedio de materias
Matematicas = float(input("\nPorfavor ingresar su calificacion de Matematicas: "))
Español = float(input("Porfavor ingresar su calificacion de Español: "))
Quimica = float(input("Porfavor ingresar su calificacion de Quimica: "))
Sociales = float(input("Porfavor ingresar su calificacion de Sociales: "))
lectura_Critica = float(input("Porfavor ingresar su calificacion de lectura_Critica: "))

sumatoria = (Matematicas + Español + Quimica + Sociales + lectura_Critica)
Operacion = 5
promedio = (sumatoria / Operacion)

Result = f"\nEl promedio de {Nombre} {Apellido} \nFue de: {promedio}"
print(Result)

print("-------------------------------------------------------------------------------------------------")
print("(CAJERO AUTOMÁTICO EJERCICIO)")

def cajero_automatico():
    saldo = 1000
    print("Bienvenido al Cajero Automático")
    
    while True:
        print("\n--- Menú ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
        
        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue
        
        if opcion == 1:
            print(f"Tu saldo actual es: ${saldo}")
        elif opcion == 2:
            try:
                deposito = float(input("¿Cuánto deseas depositar?: "))
                if deposito <= 0:
                    print("El monto debe ser positivo.")
                else:
                    saldo += deposito
                    print(f"Has depositado ${deposito}. Tu nuevo saldo es: ${saldo}")
            except ValueError:
                print("Por favor, introduce un monto válido.")
        elif opcion == 3:
            try:
                retiro = float(input("¿Cuánto deseas retirar?: "))
                if retiro <= 0:
                    print("El monto debe ser positivo.")
                elif retiro > saldo:
                    print("No tienes saldo suficiente.")
                else:
                    saldo -= retiro
                    print(f"Has retirado ${retiro}. Tu nuevo saldo es: ${saldo}")
            except ValueError:
                print("Por favor, introduce un monto válido.")
        elif opcion == 4:
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break  # Aquí el bucle termina
        else:
            print("Opción no válida. Intenta de nuevo.")

# Llamada a la función
cajero_automatico()

print("programa terminado correctamente")

print("---QUIZ PYTHON---")
nombre = input("Por favor, ingrese su nombre: ")

print(f"Hola {nombre}, bienvenido al quiz de Python")

edad = int(input("¿Cuál es tu edad? "))

if edad >= 18:
    print("Eres mayor de edad, puedes proseguir")
else:
    print("Eres menor de edad, lo sentimos")

numero = int(input("Por favor, ingresa un numero entero positivo: "))

for i in range(1, numero + 1):
    print(i) 

print("-------------------------------------------------------------------------------------------------")

DIA_TEMA_VISTO = "2024-12-5"
print("\nLa fecha especifica es:",DIA_TEMA_VISTO)


num = int(input("\nColoque el año a convertir en dias: "))

resultado = num * 365

print("\nEl año ingresado fue",num,"y en dias son: ",resultado)

print(
         *******************************
         ***SISTEMA DE MULTIPLICACIÓN***
         *******************************  )

Nombre = input("\nPor favor, ingrese su nombre: ")

Numero1 = int(input("\nIngrese el primer número: "))
Numero2 = int(input("Ingrese el segundo número: "))

result = Numero1 * Numero2

operacion = result + 350

print(Nombre,"\nSu resultado de la operacion fue de: ",operacion)

print(
         ********************************
         ******CALCULOS MATEMATICOS******
         ********************************  )


Nombre = input("\nPor favor, ingrese su nombre: ")

Numero1 = int(input("\nIngrese el primer a multiplicar es: "))
Numero2 = int(input("\nIngrese el segundo a multiplicar es: "))
Numero3 = int(input("\nIngrese el tercer a multiplicar es número: "))

resultado = Numero1 * Numero2 * Numero3

division = resultado // 275

resta  = division - 320

suma = resta + 5

print(Nombre,"Su resultado de la operacion fue de: ",resultado)

print(
         *********************************
         *****SISTEMA DE CALIFICACIÓN*****
         *********************************


2.5 perdio el año
3.0 paso pero asistir una semana de recuperacion
3.5 pasaste
4.5 felicitaciones  )


Nombre = input("\nPor favor, ingrese su nombre: ")

Matematicas = float(input("\nPor favor, ingresar su calificacion de Matematicas: "))
Español = float(input("Por favor, ingresar su calificacion de Español: "))
Quimica = float(input("Por favor, ingresar su calificacion de Quimica: "))

sumatoria = (Matematicas + Español + Quimica)
Operacion = 3
promedio = (sumatoria / Operacion)

print(Nombre,"Su resultado de la su calificacion fue de: ",promedio)

print("-------------------------------------------------------------------------------------------------")

edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad, puedes proseguir")
else:
    print("Eres menor de edad, lo sentimos")

contraseña = input("Por favor, ingrese su contraseña: "))
if contraseña == ("ABCT12"):
    print("La contraseña es correcta, bienvenido")
                 
else:
    print("Tu contraseña es incorrecta intentalo de nuevo")


print(
         *****************************************
         *********SISTEMA DE CALIFICACIÓN*********
         *****************************************    )


Nombre = input("\nPor favor, ingrese su nombre: ")

Matematicas = float(input("\nPor favor, ingresar su calificacion de Matematicas: "))
Español = float(input("Por favor, ingresar su calificacion de Español: "))
Quimica = float(input("Por favor, ingresar su calificacion de Quimica: "))

sumatoria = (Matematicas + Español + Quimica)
Operacion = 3
promedio = (sumatoria // Operacion)

if promedio >= 3.0:
    print("El estudiante",Nombre,"Aprobo con un puntaje de: ",promedio)

else:
    print("El estudiante",Nombre,"Reprobo con un puntaje de: ",promedio)

print("_" * 70)
print(
         ******************************************
         *********SENTENCIAS CONDICIONALES*********
         ******************************************     )
print("_" * 70)

# Solicitar el nombre del usuario
nombre = input("\nPor favor, ingrese su nombre: ")

# Solicitar la edad y categorizarla
edad = int(input("Por favor, ingresa tu edad: "))

if edad < 12:
    print(nombre, "es niño")
elif edad < 18:
    print(nombre, "es adolescente")
elif edad <= 60:
    print(nombre, "es adulto")
else:
    print(nombre, "es adulto mayor")

# Convertir números en letras
num = int(input("\nColoca el número a convertir en letras (1-8): "))

if num == 1:
    print("Uno")
elif num == 2:
    print("Dos")
elif num == 3:
    print("Tres")
elif num == 4:
    print("Cuatro")
elif num == 5:
    print("Cinco")
elif num == 6:
    print("Seis")
elif num == 7:
    print("Siete")
elif num == 8:
    print("Ocho")
else:
    print("Este número no es correcto.")

# Convertir una vocal a mayúscula
vocal = input("\nPor favor, ingrese una vocal a convertir a mayúscula: ").lower()

if vocal == "a":
    print("A")
elif vocal == "e":
    print("E")
elif vocal == "i":
    print("I")
elif vocal == "o":
    print("O")
elif vocal == "u":
    print("U")
else:
    print("Esta vocal no existe o no es correcta.")

# Verificar si un número es positivo, negativo o cero
numero = int(input("\nPor favor, ingrese un número para verificar si es positivo, negativo o cero: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

print("_" * 70)

numero1 = int(input("\nPor favor, ingrese un número: "))
numero2 = int(input("\nPor favor, ingrese otro número: "))

if numero1%2==0 and numero2%2==0:
    print("Ambos numeros son pares")
elif numero1%2==0 and numero2%2!=0:
    print(f"{numero1} es par")
elif numero1%2!=0 and numero2%2==0:
    print(f"{numero2} es par")
else:
    print("Ambos numeros son impares")


num1 = int(input("\nPor favor, ingrese un número: "))
num2 = int(input("\nPor favor, ingrese otro número: "))
num3 = int(input("\nPor favor, ingrese un último número: "))

if num1>=num2 and num1>=num3:
    print(f"{num1} es el número mayor")
elif num2>=num1 and num2>=num3:
    print(f"{num2} es el número mayor")
elif num3>=num1 and num3>=num2:
    print(f"{num3} es el número mayor")
elif num1==num2==num3:
    print("Todos los numeros son iguales")
else:
    print("porfavor ingresa numeros positivos")

print("_" * 70)

print(""
         *************************************
         **********SISTEMA DE CAMBIO**********
         *************************************

1. Saludar
2. Fecha actual
3. numero de el 1 al 10
4. Despedir
"")

nombre = input("Por favor, ingresa tu nombre")
numero_1 = int(input("\nPor favor, ingrese una opcion: "))

if numero_1 == 1:
    print(f"Hola {nombre} Bienvenido, gracias por usar mi programa")
elif numero_1 == 2:
    print(f"{nombre}La fecha actual es 2024-12-10")
elif numero_1 == 3:
    print(f"{nombre} los numeros son: 1,2,3,4,5,6,7,8,9,10")
elif numero_1 == 4:
    print(f"{nombre} Gracias por usar mi programa, hasta luego")
else:
    print(f"{nombre } Por favor, ingresa una opción correcta")
    
print("_" * 70)

print(
         ***************************************
         ********** SISTEMA DE CAMBIO **********
         ***************************************

1. Convertir Dolar a Pesos Colombianos 
2. Convertir Euros a Pesos Colombianos 
3. Convertir Yenes a Pesos Colombianos
4. Busqueda
5. Extracción
6. Asignación
7. Comparación
8. Float
9. Calificación de notas
10. Convertir dias a años
11. Poner la primera version de python

12345)

print("_" * 70)

contraseña = int(input("Por favor, ingrese una contraseña: "))
if contraseña == ("12345"):
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")

convertir = input("\nPor favor, ingrese una opción: ")

print("_" * 70)

convertir = int(input("\nPor favor, ingrese una opción: "))

if convertir == 1:
    print("""
             -----------------------------------------------------------------------------
             ------------------------- $ DOLAR A PESOS COLOMBIANOS $ ---------------------
             -----------------------------------------------------------------------------
                                                                                            """)
    
    numero_1 = int(input("Por favor, ingrese la cantidad de dolares: "))
    operacion = numero_1 * 4397
    print(f"La cantidad de Dolares a Pesos Colombianos es de: {operacion}")
    
elif convertir == 2:
    print("""
             -----------------------------------------------------------------------------
             ------------------------- $ EUROS A PESOS COLOMBIANOS $ ---------------------
             -----------------------------------------------------------------------------
                                                                                            """)
    
    numero_2 = int(input("Por favor, ingrese la cantidad de Euros: "))
    operacion_1 = numero_2 * 4600
    print(f"La cantidad de Euros a Pesos Colombianos es de: {operacion_1}")
    
elif convertir == 3:
    print("""
             -----------------------------------------------------------------------------
             ------------------------- $ YENES A PESOS COLOMBIANOS $ ---------------------
             -----------------------------------------------------------------------------
                                                                                           """)
    
    numero_3 = int(input("Por favor, ingrese la cantidad de Euros: "))
    operacion_2 = numero_3 * 28.79
    print(f"La cantidad de Yenes a Pesos Colombianos es de: {operacion_2}")
    
elif convertir == 4:
    print("""
             --------------------------------------------------------
             ------------------------- BUSQUEDA ---------------------
             --------------------------------------------------------
                                                                                           """)
    
    text1 = ("Hola Colombia, este es un pais grande en naturaleza.")
    print(text1)
    busqueda = text1.find("Colombia")
    print(f"el valor es: {busqueda}")
    
elif convertir == 5:
    print("""
             --------------------------------------------------------------
             ------------------------- EXTRACCIÓN -------------------------
             --------------------------------------------------------------
                                                                                           """)
    
    text1 = ("Hola Colombia, este es un pais grande en naturaleza.")
    busqueda = text1[5:37]
    print(busqueda)
    
elif convertir == 6:
    print("""
             -------------------------------------------------------------------------
             ------------------------- SISTEMA DE ASIGNACIÓN -------------------------
             -------------------------------------------------------------------------
                                                                                           """)
    
    marca = ("Tesla")
    marca += (" Toyota")
    print(marca)
    
elif convertir == 7:
    print("""
             -------------------------------------------------------------------------
             ------------------------- SISTEMA DE COMPARACIÓN -------------------------
             -------------------------------------------------------------------------
                                                                                           """)
    
    
    numer1 = int(input("Por favor, ingresa el primer número: "))
    numer2 = int(input("Por favor, ingresa el segundo número: "))
    
    if numer1 == numer2:
        print(f"Los números {numer1} y {numer2} son iguales.")
    else:
        print(f"Los números {numer1} y {numer2} son diferentes.")
        
    

elif convertir == 8:
    print("""
             ---------------------------------------------------------------------
             ------------------------- NÚMEROS FLOTANTES -------------------------
             ---------------------------------------------------------------------
                                                                                           """)
    
    numer = float(input("\nPor favor, ingrese un número decimal: "))
    print(numer, type(numer))
    
elif convertir == 9:
    print("""
             ------------------------------------------------------------------------
             ------------------------- SISTEMA DE CALIFICACIÓN  ---------------------
             ------------------------------------------------------------------------
                                                                                           """)
    
    nombre = input("\nPor favor, ingrese su nombre: ")
    apellido = input("\nPor favor, ingrese su apellido: ")
    
    Matematicas = float(input("\nPor favor, ingresar su calificacion de Matematicas: "))
    Español = float(input("Por favor, ingresar su calificacion de Español: "))
    Quimica = float(input("Por favor, ingresar su calificacion de Quimica: "))

    sumatoria = (Matematicas + Español + Quimica)
    Operacion = 3
    promedio = (sumatoria // Operacion)

elif convertir == 10:
    print("""
             ----------------------------------------------------------------------
             ------------------------- CONVERTIR AÑOS A DIAS  ---------------------
             ----------------------------------------------------------------------
                                                                                           """)

    numb = int(input("\nColoque el año a convertir en dias: "))
    resultado = numb * 365
    print(f"\nEl año ingresado fue {numb} y en dias son {resultado}")
   
elif convertir == 11:
    print("""
             -------------------------------------------------------------------
             ------------------------- HISTORIA DE PYTHON  ---------------------
             -------------------------------------------------------------------
                                                                                 """)

    version_1 = float(input("\nPor favor, ingrese la primera versión de python: "))

    if version_1 == ("0.9.0"):
        print("La versión es correcta")
    else:
        ("La versión no es correcta")

    

