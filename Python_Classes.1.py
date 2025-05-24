# print("========================================")
# print("============ PYTHON CLASSES ============")
# print("========================================")

# print("-------------- POTENCIACIÓN --------------")

# """ La potenciación es una operación matemática que se utiliza para multiplicar un número por si mismo varias veces. Es una forma abreviada de realizar una multiplicación repetida, donde intervienen dos elementos que son: base y exponente. La base representa el número que se va a multiplicar, mientras que el exponente indica cuantas veces se debe multiplicar. Ejemplos: 3**2 = 3*3 = 9 | 2**6 = 2*2*2*2*2*2 = 12 | 4**2 = 4*4 = 16. """

# print("----- PROPIEDADES DE LA POTENCIACIÓN -----")

# print("\n--> PRODUCTO DE POTENCIACIÓN CON LA MISMA BASE <--\n")

# """ Cuando se multiplican dos potencias con la misma base, se conserva la base y se suman los exponentes, tal que así: a**m * a**n = a**(m+n). De ser el caso que las bases sean distintas se calcula cada potencia por separado. Ejemplos: 2**4 * 2**3 = 2**7 = 128 | 3**3 * 1**3 = 27*1 = 27 """

# print("\n--> COSCIENTE DE POTENCIA DE LA MISMA BASE <--\n")

# """ Cuando se dividen dos potencias que tienen la misma base, se conserva la base y se restan los exponentes. Tal que así: a**m / a**n = a**(m-n). Por el contrario, si las bases no son iguales, NO puedes restar los exponentes, Solo se resuelven por separado. Ejemplos: 10**4 / 10**1 = 10**(-3) = 1.000 | 6**2 / 5**2 = 36 / 25 = 1.44 """

# print("\n--> POTENCIA DE UNA POTENCIA <--\n")

# """ Cuando una potencia se eleva a otra potencia, se mantienen las bases y se multiplican los exponentes. Tal que así: (a**m)**n = a**(m*n).Ejemplos: (3**2)**3 = 3**(2*3) = 3**6 = 729 | (5**2)**3 = 5**(2*3) = 5**6 = 15.625 """

# print("\n--> POTENCIA DE UN PRODUCTO <--\n")

# """ Cuando un producto se eleva a una potencia, cada factor del producto se eleva al mismo esponente. Tal que así: (a*b)**c = a**c * b**c. Ejemplo: (2*3)**4 = 2**4 * 3**4 = 16*81 = 1,296. En caso de querer hacer el procedimiento mas corto, solo multiplicas 2*3 y lo elevas a la 4 tal que así: (2*3)**4 = 6**4 = 1,296 """

# print("-----> EJERCICIOS DE POTENCIACIÓN <-----")

# print("\n[1] 2**3 * 3**4 = 8*81 = 648")
# print("\n[2] 5**5 * 5**2 = 5**7 = 78,125")
# print("\n[3] 10**1 * 10**3 = 10**4 = 10,000")
# print("\n[4] (2*1)**3 = 2**3 = 8")
# print("\n[5] (2*10)**3 = 20**3 = 8,000")
# print("\n[6] (3*4)**1 = 12**1 = 12")
# print("\n[7] 8**5 / 8**2 = 8**3 = 512")
# print("\n[8] 4**6 / 4**3 = 4**3 = 64")
# print("\n[9] 12**4 / 12**1 = 12**3 = 1,728")
# print("\n[10] (6/2)**2 = 36 / 4 = 9")
# print("\n[11] (8/4)**2 = 64 / 16 = 4")
# print("\n[12] (5/3)**3 = 125 / 27 = 4.63\n")

# print("-----> RESOLUCIÓN DE 4 EJERCICIOS EN CÓDIGO <-----")

# print("\n[1]")
# base2 = 2
# expo2 = 3
# base3 = 3
# expo3 = 4
# op1 = base2 ** expo2
# op2 = base3 ** expo3
# result1 = op1 * op2 
# print("El resultado de 2³ x 3⁴ es:",result1)

# print("\n[2]")
# factor1 = 2
# factor2 = 10
# producto = factor1 * factor2 
# result2 = producto ** 3 
# print("El resultado de (2 x 10)³ es:",result2)

# print("\n[3]")
# base8 = 8
# expo8 = 5
# expo2 = 2 
# result3 = base8 ** (expo8-expo2)
# print("El resultado de 8⁵ / 8² es:",result3)

# print("\n[4]")
# factor3 = 6
# expon2 = 2
# fraccion = factor3 / expon2
# result4 = fraccion ** 2
# print(f"El resultado de (6/2)² es: {result4} \n")

# print("-" * ancho)
# print("TIPOS DE DATOS NUMÉRICOS".center(ancho))
# print("-" * ancho)

# print("\n--> ENTEROS <--\n")
# print(
#     "Los números enteros son aquellos que NO tienen decimales, tanto positivos como negativos (además del cero). "
#     "Ejemplo: 1, 2, 525, 0, -817, -100. En python, se pueden representar mediante el tipo inst (de integer). A diferencia de otros "
#     "lenguajes de programación, los números de tipo int en python pueden ser pequeños o grandes, no tienen límite alguno.\n"
# )

# print("\n--> FLOAT <--\n")
# print(
#     "Los números reales son los que tienen decimales. En python se expresan mediante el tipo float. Ejemplo: 0.270, -12.1233, "
#     "989.8743912, 4387, -74.93.\n"
# )

# print("-" * ancho)
# print("OPERACIONES NUMÉRICAS EN PYTHON".center(ancho))
# print("-" * ancho)

# print(
#     "\nEn programación y en matemáticas, los operadores aritméticos son aquellos que manipulan los datos de tipo numérico. Es decir, "
#     "permiten la realización de operaciones matemáticas (sumas, restas, multiplicaciones, etc).\n"
#     "El resultado de una operación aritmética es un dato aritmético, es decir, si ambos valores son números enteros, el resultado "
#     "será de tipo entero; si alguno de ellos o ambos son números con decimales, el resultado también lo será.\n"
# )
 
# ancho2 = 70
# print("=" * ancho2)
# print("  Operación   | Operador | Ejemplo")
# print("-" * ancho2)
# print("Suma          |    +     | 3 + 5 = 8")
# print("Resta         |    -     | 4 - 1 = 3")
# print("Multiplicación|    *     | 3 * 6 = 18")
# print("Potenciación  |   **     | 3 ** 2 = 9")
# print("División      |    /     | 13.0 / 2.0 = 6.5")
# print("Div. Entera   |   //     | 13.0 // 2.0 = 6.0")
# print("Módulo        |    %     | 7.0 % 5 = 2.0")
# print("=" * ancho2)

# La funcion input() convierte la entrada en una cadena, aunque escribamos un numero
# Ejemplo: nombre=int(input(¿que edad tienes?))

# base1 = int(input("Ingrese una base: "))
# expo1 = int(input("Ingrese su exponente: "))
# print("Esta operacion se multiplicara por: ")
# base2 = int(input("Ingrese una base: "))
# expo2 = int(input("Ingrese su exponente: "))
# result = base1 ** expo1 * base2 ** expo2
# print(f"El resultado de la operacion es: {result}")

# factor1= int(input("Ingrese una factor: "))
# factor2 = int(input("Ingrese un segundo factor: "))
# exponente = int(input("Ingrese un exponente por que el seran elevados los dos numeros: "))
# operacion = factor1 * factor2
# result = operacion ** exponente
# print(f"El resultado de la operacion {factor1} y {factor2} elevados a la {exponente} es: {result} ")

# bas1 = int(input("Ingrese una base: "))
# exp1 = int(input("Ingrese un exponente: "))
# exp4 = int(input("Ingrese otro exponente: "))
# oper = bas1 ** ()

# print("IDENTACION")
# texto = "python"
# print(texto[0:2])

# print("ASIGNACION MULTIPLE")
# a, b, c, = 12, 4, 2
# print(a)
# print(b)
# print(c)

# w=r=t= 2

# x = 8
# x += 2
# print(x)

# suma y asigna
# a = "Todos "
# a += "Los "
# a += "Dias."
# print(a)

# resta y asigna
# b = 8
# b -= 1
# print(b)

# CONCATENACION
# texto1 = "Hola"
# texto2 = "Mundo."
# result = texto1 + " " + texto2
# print(result)

# mensaje = "Hola Mundo"
# buscar = mensaje.find("Mundo")
# print(buscar)
# busqueda2 = mensaje[0:6]
# print(busqueda2)

# cad1 = "buenos"
# cad2 = "Buenos"
# cad3 = "dias"
# print(cad1 == cad2)
# print(cad1 == cad3)

# print(EJERCICIO 1)

# cadena = "El conocimiento es poder."
# print(cadena.find("conocimiento"))
# print(cadena.find("poder"))

# print(EJERCICIO 2)

# cadena2 = "La práctica hace al maestro."
# print(cadena2.find("práctica"))
# print(cadena2.find("maestro"))

# print(EJERCICIO 3)

# ingresar = input("Escriba una frase: ")
# ingresar2 = input("Ingresa la palabra que quieras buscar en la frase: ")
# print(ingresar.find(ingresar2))

# texto1 = "Puede que la tarea que me he impuesto de escribir una historia completa del pueblo romano desde el comienzo mismo de su existencia me recompense por el trabajo invertido en ella, no lo sé con certeza, ni creo que pueda aventurarlo. Porque veo que esta es una práctica común y antiguamente establecida, cada nuevo escritor está siempre persuadido de que ni lograrán mayor certidumbre en las materias de su narración, ni superarán la rudeza de la antigüedad en la excelencia de su estilo."

# print(texto1.find("común"))
# print(texto1.find("Porque"))
# print(texto1.find("rudeza"))

# print(texto1[232:432])

# texto2 = "En el principio sólo existía el Caos. El Cielo y la Tierra formaban una masa confusa, en la que el todo y la nada se entremezclaban como la suciedad en el agua. Por doquier reinaba una espesa niebla que jamás logró ver ojo humano y a la que Pan-Ku consiguió dispersar con su portentosa fuerza. Lo puro quedó entonces separado de lo impuro y apareció la suprema bondad, que esparce sus bendiciones sobre toda criatura. Su mundo es el de la luz. Quien a él se acerca descubre el camino que conduce al reino del bien. Mas el que quiera penetrar en el secreto del principio de cuanto existe debe leer La crónica de los orígenes"

# print(texto2.find("masa"))
# print(texto2.find("Su"))
# print(texto2.find("orígenes"))
# print(texto1[418:615])

# nombre = input("porfavor, ingrese el nombre del estudiante: ")
# nota1 = float(input("Ingrese una nota: "))
# nota2 = float(input("Ingrese una segunda nota: "))
# nota3 = float(input("Ingrese una tercera nota: "))
# operacion = (nota1 * 0.2) + (nota2 * 0.3) + (nota3 * 0.5)
# print(f"el resultado del estudiante {nombre} fue: {operacion}%")
# if operacion >= 3.5:
#     print(f"El estudiante {nombre} pasó la prueba.")
# else: 
#     print(f"El estudiante {nombre} Reprobó.")



