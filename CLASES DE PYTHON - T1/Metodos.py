print("\n" + "=" * 40)
print(" MÉTODOS EN PYTHON ".center(40, "="))
print("=" * 40 + "\n")

print("---------------------------------------------------------------")

print("==== MÉTODO N°1: .len() ====")

print("\n- len(): Longitud de una cadena (o lista)")
print("Este método devuelve cuántos caracteres (o elementos) hay.\n")

print("==== EJEMPLO N°1 ====")

nombre = input("Ingresa tu nombre: ")

# Muestra la cantidad de letras que tiene el nombre
print(f"El nombre '{nombre}' tiene {len(nombre)} caracteres.")

print("\n==== EJEMPLO N°2 ====")

# Pide 3 palabras al usuario y las guarda en una lista
palabras = [
    input("Ingrese una palabra: "),
    input("Ingrese otra palabra: "),
    input("Ingrese una última palabra: ")
]

# Muestra cuántas letras tiene cada palabra
print(f"\nLa palabra '{palabras[0]}' tiene {len(palabras[0])} letras.")
print(f"La palabra '{palabras[1]}' tiene {len(palabras[1])} letras.")
print(f"La palabra '{palabras[2]}' tiene {len(palabras[2])} letras.")

print("---------------------------------------------------------------")

print("==== MÉTODO N°2: .find() ====")

print("\n- .find(): Buscar una subcadena")
print(".find() devuelve el índice donde aparece por primera vez una letra o palabra.")
print("Si no se encuentra, devuelve -1.\n")

print("==== EJEMPLO N°1 ====\n")

frase = input("Ingresa una frase: ").lower()
letra = input("Ingrese una sola letra (ej: a): ").lower()

# Busca la posición de la letra con .find()
posicion = frase.find(letra)

# Verifica si la letra fue encontrada
if posicion == -1:
    print(f"\nLa letra '{letra}' NO está en la frase.")
    print(f"Resultado: {posicion}")  # Mostrará -1
else:
    print(f"\nLa letra '{letra}' SÍ está en la frase.")
    print(f"Aparece por primera vez en la posición: {posicion}")

print("\n==== EJEMPLO N°2 ====\n")

# Se pide una segunda frase y una palabra clave
frase2 = input("Escribe una frase misteriosa: ").lower()
clave = input("Ingrese la palabra clave para buscar: ").lower()

# Busca la posición de la palabra clave
pos = frase2.find(clave)

# Verifica si la palabra fue encontrada
if pos == -1:
    print("\nLa palabra clave no fue encontrada... sigue buscando.")
else:
    print(f"\n¡Palabra encontrada! Empieza en la posición: {pos}")

print("---------------------------------------------------------------")

print("==== MÉTODO N°3: Extracción [ ] ====")

print("\n- EXTRACCIÓN: Obtener una parte de una cadena usando índices.\n")

print("==== EJEMPLO N°1 ====")

frase = input("\nEscribe una frase corta: ")

# Muestra los primeros 5 caracteres (desde índice 0 hasta 4)
print(f"\nLos primeros 5 caracteres son: '{frase[0:5]}'")

print("\n==== EJEMPLO N°2 ====")

# Pide otra frase (puede ser más larga)
palabra = input("\nEscribe una frase larga: ")

# Extrae y muestra los caracteres desde el índice 1 hasta el 4 (no incluye el 5)
print(f"\nLos caracteres del índice 1 al 4 son: '{palabra[1:5]}'")

# Extrae desde el índice 6 hasta el 8 (no incluye el 9)
print(f"Los caracteres del índice 6 al 8 son: '{palabra[6:9]}'")

print("---------------------------------------------------------------")

print("==== MÉTODO N°4: Concatenación '+' ====")

print("\n- CONCATENACIÓN: Unir cadenas de texto con el símbolo '+'.\n")
print("Permite combinar dos o más cadenas en una sola.")

print("\n==== EJEMPLO N°1 ====")

nombre = input("\nEscribe tu nombre: ")
apellido = input("Escribe tu apellido: ")

# Une el nombre con el apellido, separados por un espacio
nombre_completo = nombre + " " + apellido

# Muestra el resultado
print(f"\nTu nombre completo es: {nombre_completo}")

print("\n==== EJEMPLO N°2 ====")

# Define varias partes de un mensaje
parte1 = "Hola"
parte2 = ", "
parte3 = "bienvenido"
parte4 = " a Python."

# Une todas las partes para formar una sola cadena
mensaje = parte1 + parte2 + parte3 + parte4

# Muestra el mensaje final
print(f"\nMensaje final: {mensaje}")

print("---------------------------------------------------------------")

print("==== MÉTODO N°5: .lower() ====")

# Explicación del método
print("\n- .lower(): Convierte todo el texto a minúsculas.\n")
print("Útil para normalizar textos antes de compararlos.")

print("\n==== EJEMPLO N°1 ====")

texto = input("\nEscribe una frase con MAYÚSCULAS: ")

# Convierte la frase a minúsculas
print(f"\nFrase en minúsculas: {texto.lower()}")

print("---------------------------------------------------------------")

print("==== MÉTODO N°6: .upper() ====")

# Explicación del método
print("\n- .upper(): Convierte todo el texto a MAYÚSCULAS.\n")
print("Útil para resaltar palabras o comparar en mayúsculas.")

print("\n==== EJEMPLO N°1 ====")

texto = input("\nEscribe una frase con minúsculas: ")

# Convierte la frase a mayúsculas
print(f"\nFrase en mayúsculas: {texto.upper()}")

print("---------------------------------------------------------------")


