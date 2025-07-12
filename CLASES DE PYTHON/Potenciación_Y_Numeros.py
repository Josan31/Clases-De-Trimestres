# CONCEPTOS A TENER EN CUENTA:

# print("-------------- POTENCIACIÓN --------------")


# La potenciación es una forma abreviada de multiplicar un número por sí mismo varias veces.
# Intervienen dos elementos: base (número que se multiplica) y exponente (veces que se repite la multiplicación).
# Ejemplos: 3**2 = 3*3 = 9 | 2**6 = 2*2*2*2*2*2 = 64 | 4**2 = 4*4 = 16


# print("----- PROPIEDADES DE LA POTENCIACIÓN -----")


# print("\n--> PRODUCTO DE POTENCIACIÓN CON LA MISMA BASE <--\n")


# Si se multiplican potencias con la misma base, se conserva la base y se suman los exponentes:
# a**m * a**n = a**(m+n)
# Si las bases son distintas, se calcula cada una por separado.
# Ejemplos: 2**4 * 2**3 = 2**7 = 128 | 3**3 * 1**3 = 27 * 1 = 27

# print("\n--> COSCIENTE DE POTENCIA DE LA MISMA BASE <--\n")


# Al dividir potencias con la misma base, se conserva la base y se restan los exponentes:
# a**m / a**n = a**(m-n)
# Si las bases son diferentes, se resuelve cada potencia por separado.
# Ejemplos: 10**4 / 10**1 = 10**3 = 1000 | 6**2 / 5**2 = 36 / 25 = 1.44

# print("\n--> POTENCIA DE UNA POTENCIA <--\n")


# Cuando una potencia se eleva a otra, se multiplican los exponentes:
# (a**m)**n = a**(m*n)
# Ejemplos: (3**2)**3 = 3**6 = 729 | (5**2)**3 = 5**6 = 15,625

# print("\n--> POTENCIA DE UN PRODUCTO <--\n")


# Al elevar un producto a una potencia, cada factor se eleva por separado:
# (a*b)**c = a**c * b**c
# Ejemplo: (2*3)**4 = 2**4 * 3**4 = 16 * 81 = 1,296
# También puede resolverse directo: (2*3)**4 = 6**4 = 1,296

print("\n-----> EJERCICIOS DE POTENCIACIÓN <-----\n")

# Ejemplos de producto de potencias:
print("[1] 2**3 * 3**4 = 8 * 81 = 648")
print("[2] 5**5 * 5**2 = 5**7 = 78,125")
print("[3] 10**1 * 10**3 = 10**4 = 10,000")

# Ejemplos de potencia de un producto:
print("[4] (2 * 1)**3 = 2**3 = 8")
print("[5] (2 * 10)**3 = 20**3 = 8,000")
print("[6] (3 * 4)**1 = 12**1 = 12")

# Ejemplos de cociente de potencias con misma base:
print("[7] 8**5 / 8**2 = 8**3 = 512")
print("[8] 4**6 / 4**3 = 4**3 = 64")
print("[9] 12**4 / 12**1 = 12**3 = 1,728")

# Ejemplos de potencia de un cociente:
print("[10] (6 / 2)**2 = 3**2 = 9")
print("[11] (8 / 4)**2 = 2**2 = 4")
print("[12] (5 / 3)**3 = (1.666...)**3 ≈ 4.63")

print("\n-----> RESOLUCIÓN DE 4 EJERCICIOS EN CÓDIGO <-----\n")

print("\n[1]")

# Se define la base y el exponente para 2³
base2 = 2
expo2 = 3

# Se define la base y el exponente para 3⁴
base3 = 3
expo3 = 4

# Se calcula 2³ = 8
op1 = base2 ** expo2

# Se calcula 3⁴ = 81
op2 = base3 ** expo3

# Se multiplican los resultados: 8 * 81 = 648
result1 = op1 * op2 

print("El resultado de 2³ x 3⁴ es:", result1)

print("\n[2]")

# Se definen dos factores para multiplicar: 2 y 10
factor1 = 2
factor2 = 10

# Se multiplica primero: 2 * 10 = 20
producto = factor1 * factor2 

# Luego se eleva al cubo: 20³ = 8000
result2 = producto ** 3 

print("El resultado de (2 x 10)³ es:", result2)

print("\n[3]")

# Se define la base 8 y dos exponentes
base8 = 8
expo8 = 5
expo2 = 2 

# Se restan los exponentes (porque la base es la misma): 8**(5-2) = 8³ = 512
result3 = base8 ** (expo8 - expo2)

print("El resultado de 8⁵ / 8² es:", result3)

print("\n[4]")

# Se definen dos números para hacer la división: 6 / 2 = 3
factor3 = 6
expon2 = 2

# Se divide primero
fraccion = factor3 / expon2

# Luego se eleva al cuadrado: 3² = 9
result4 = fraccion ** 2

print(f"El resultado de (6/2)² es: {result4} \n")

print("------ TIPOS DE DATOS NUMÉRICOS ------\n")

print("\n--> ENTEROS <--\n")
print(
    "Los números enteros son aquellos que NO tienen decimales.\n"
    "Pueden ser positivos, negativos o cero.\n"
    "Ejemplos: 1, 2, 525, 0, -817, -100.\n\n"
    "En Python, se representan con el tipo 'int' (de integer).\n"
    "A diferencia de otros lenguajes, los enteros en Python no tienen un límite fijo:\n"
    "pueden ser tan grandes como sea necesario.\n"
)

print("\n--> FLOAT <--\n")
print(
    "Los números reales o decimales se representan en Python con el tipo 'float'.\n"
    "Ejemplos: 0.270, -12.1233, 989.8743912, -74.93.\n"
)

print("\n------ OPERACIONES NUMÉRICAS EN PYTHON ------\n")

print(
    "Los operadores aritméticos permiten realizar operaciones matemáticas como:\n"
    "- Suma (+)\n"
    "- Resta (-)\n"
    "- Multiplicación (*)\n"
    "- División (/)\n"
    "- Potenciación (**), entre otros.\n\n"
    "Reglas generales en Python:\n"
    "→ Si ambos valores son enteros (int), el resultado será entero (cuando aplica).\n"
    "→ Si uno de los valores es decimal (float), el resultado será float.\n"
)


# ancho2 define el ancho de la tabla
ancho2 = 70

print("=" * ancho2)
print("  Operación        | Operador |    Ejemplo")
print("-" * ancho2)
print(" Suma              |    +     |   3 + 5 = 8")
print(" Resta             |    -     |   4 - 1 = 3")
print(" Multiplicación    |    *     |   3 * 6 = 18")
print(" Potenciación      |   **     |   3 ** 2 = 9")
print(" División          |    /     |   13 / 2 = 6.5")
print(" División Entera   |   //     |   13 // 2 = 6")
print(" Módulo (residuo)  |    %     |   7 % 5 = 2")
print("=" * ancho2)


# La función input() recibe datos del usuario como texto (cadena),
# por eso, si queremos operar con números, debemos convertirlos con int() o float().

# === EJEMPLO 1: Multiplicación de dos potencias ===

# Solicita la primera base y su exponente
base1 = int(input("Ingrese la primera base: "))
expo1 = int(input("Ingrese el exponente de la primera base: "))

print("Esta operación se multiplicará por otra potencia.")

# Solicita la segunda base y su exponente
base2 = int(input("Ingrese la segunda base: "))
expo2 = int(input("Ingrese el exponente de la segunda base: "))

# Calcula el resultado de las dos potencias multiplicadas
resultado1 = (base1 ** expo1) * (base2 ** expo2)

print(f"El resultado de {base1}^{expo1} * {base2}^{expo2} es: {resultado1}")

# === EJEMPLO 2: Producto de dos factores elevados a una potencia ===

factor1 = int(input("\nIngrese un primer factor: "))
factor2 = int(input("Ingrese un segundo factor: "))
exponente = int(input("¿A qué exponente se elevará el producto de los factores?: "))

# Multiplica los factores y eleva el resultado al exponente
producto = factor1 * factor2
resultado2 = producto ** exponente

print(f"El resultado de ({factor1} x {factor2})^{exponente} es: {resultado2}")

# === EJEMPLO 3: Potencia de una potencia (pendiente de terminar) ===

# Solicita la base y dos exponentes para una potencia elevada a otra
base3 = int(input("\nIngrese una base: "))
expo3 = int(input("Ingrese el primer exponente: "))
expo4 = int(input("Ingrese el segundo exponente: "))

# Aplica la propiedad de potencia de una potencia: (a^m)^n = a^(m*n)
resultado3 = base3 ** (expo3 * expo4)

print(f"El resultado de ({base3}^{expo3})^{expo4} es: {resultado3}")

print("---------------------------------------------------------\n")

# ---------------------- IDENTACIÓN ----------------------

print("IDENTACION")

texto = "python"

# Muestra los primeros dos caracteres
print(texto[0:2])  

# ------------------- ASIGNACIÓN MÚLTIPLE -------------------

print("ASIGNACION MULTIPLE")

a, b, c = 12, 4, 2
print(a)
print(b)
print(c)

# Asignación a varias variables con el mismo valor
w = r = t = 2
print(w)

# ------------------- OPERADOR += -------------------

x = 8
x += 2  # Equivale a x = x + 2

print(x)

# ------------------- SUMA Y ASIGNA (+= con texto) -------------------

a = "Todos "
a += "Los "
a += "Dias."

print(a)

# ------------------- RESTA Y ASIGNA -------------------

b = 8
b -= 1

print(b)

# ------------------- CONCATENACIÓN -------------------

texto1 = "Hola"
texto2 = "Mundo."
resultado = texto1 + " " + texto2
print(resultado)

# ------------------- MÉTODO FIND -------------------

mensaje = "Hola Mundo"
buscar = mensaje.find("Mundo")
print(buscar)  # Índice donde comienza "Mundo"
busqueda2 = mensaje[0:6]
print(busqueda2)

# ------------------- COMPARACIÓN DE CADENAS -------------------

cad1 = "buenos"
cad2 = "Buenos"
cad3 = "dias"
print(cad1 == cad2)  # False, por la mayúscula
print(cad1 == cad3)  # False, son distintas

# ------------------- EJERCICIOS DE .find() -------------------

print("Ejercicio N° [1]")
cadena = "El conocimiento es poder."
print(cadena.find("conocimiento"))  # 3
print(cadena.find("poder"))         # 21

print("Ejercicio N° [2]")
cadena2 = "La práctica hace al maestro."
print(cadena2.find("práctica"))  # 3
print(cadena2.find("maestro"))   # 21

print("Ejercicio N° [3]")
ingresar = input("Escriba una frase: ")
ingresar2 = input("Ingresa la palabra que quieras buscar en la frase: ")
print(ingresar.find(ingresar2))

# ------------------- TEXTO LARGO + BÚSQUEDAS -------------------
texto1 = (
    "Puede que la tarea que me he impuesto de escribir una historia completa del pueblo romano desde el comienzo mismo de su existencia me recompense por el trabajo invertido en ella, no lo sé con certeza, ni creo que pueda aventurarlo. Porque veo que esta es una práctica común y antiguamente establecida, cada nuevo escritor está siempre persuadido de que ni lograrán mayor certidumbre en las materias de su narración, ni superarán la rudeza de la antigüedad en la excelencia de su estilo."
)

print(texto1.find("común"))
print(texto1.find("Porque"))
print(texto1.find("rudeza"))

# Muestra parte del texto del índice 232 al 432
print(texto1[232:432])

texto2 = (
    "En el principio sólo existía el Caos. El Cielo y la Tierra formaban una masa confusa, "
    "en la que el todo y la nada se entremezclaban como la suciedad en el agua. Por doquier reinaba una espesa niebla "
    "que jamás logró ver ojo humano y a la que Pan-Ku consiguió dispersar con su portentosa fuerza. Lo puro quedó entonces "
    "separado de lo impuro y apareció la suprema bondad, que esparce sus bendiciones sobre toda criatura. Su mundo es el de la luz. "
    "Quien a él se acerca descubre el camino que conduce al reino del bien. Mas el que quiera penetrar en el secreto del principio "
    "de cuanto existe debe leer La crónica de los orígenes"
)

print(texto2.find("masa"))
print(texto2.find("Su"))
print(texto2.find("orígenes"))

# Muestra parte del texto1 desde el índice 418 al 615
print(texto1[418:615])

# ------------------- PROMEDIO DE NOTAS -------------------

nombre = input("Por favor, ingrese el nombre del estudiante: ")

nota1 = float(input("Ingrese una nota: "))
nota2 = float(input("Ingrese una segunda nota: "))
nota3 = float(input("Ingrese una tercera nota: "))

# Se calcula el promedio (20%, 30%, 50%)
operacion = (nota1 * 0.2) + (nota2 * 0.3) + (nota3 * 0.5)

print(f"El resultado del estudiante {nombre} fue: {operacion}%")

# Condición para saber si aprueba
if operacion >= 3.5:
    print(f"El estudiante {nombre} pasó la prueba.")
else:
    print(f"El estudiante {nombre} reprobó.")