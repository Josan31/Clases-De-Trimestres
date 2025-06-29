# print("\n" + "=" * 40)
# print(" MÉTODOS EN PYTHON ".center(40, "="))
# print("=" * 40 + "\n")

# print("-" * 50)

# print("==== MÉTODO N°1: .LEN() ====")

# print("\n- len(): Longitud de una cadena (o lista)\n".upper())

# print(".len() Devuelve cuántos caracteres (o elementos) hay.")

# print("-" * 50)

# print("==== EJEMPLO N°1 ====")

# # Pide ingresar el nombre del usuario 
# nombre = input("\nIngresa tu nombre: ".lower())

# # Da de resultado la cantidad de elementos que tiene el nombre
# print(f"\nEl nombre {nombre}, tiene: {len(nombre)} caracteres")

# print("-" * 50)

# print("==== EJEMPLO N°2 ====")

# # Pide los datos al usuario almacenandolos en una lista
# palabras = [input("\nIngrese una palabra: ".lower()), input("Ingrese otra palabra: ".lower()), input("Ingrese una última palabra: ".lower())]

# # Cuenta cuantas letras tiene cada palabra
# print(f"\nLa palabra '{palabras[0]}' tiene {len(palabras[0])} letras")
# print(f"La palabra '{palabras[1]}' tiene {len(palabras[1])} letras")
# print(f"La palabra '{palabras[2]}' tiene {len(palabras[2])} letras")

print("=" * 60)

print("Método N° [2]".upper())
print("\n- .find(): buscar una subcadena\n".upper())

print(".find() Devuelve la posición (índice) donde aparece por primera vez una letra o palabra. Si no se encuentra, devuelve -1.")

print("-------------------------------------------")

print("\nEjemplo N° [1]".upper())

# Pide los datos al usuario
frase = input("Ingresa una frase: ").lower()
letra = input("Ingrese una sola letra (ej: a): ").lower()

# si la letra ingresada por el usuario no está en la frase
if letra not in frase:
    print(f"\nLa letra '{letra}' NO está en la frase: '{frase}'. Por lo cual arroja un {frase.find(letra)} ")
    
# Si la letra ingresada por el usuario sí está en la frase
else:
    posicion = frase.find(letra)
    print(f"La letra '{letra}' SI está en la frase '{frase}'")
    print(f"Aparece por primera vez en la posición {posicion}")

print("-------------------------------------------")

print("\nEjemplo N° [2]".upper())

# Pide al usuario la frase y la palabra a buscar
frase2 = input("Escribe una frase misteriosa (sin dejar espacios entre ellas): ").lower()
clave = input("Ingrese la palabra clave para buscar: ").lower()

# Verifica si la palabra ingresada está en la frase
pos = frase2.find(clave)

# Si la palabra ingresada por el usuario no está en la frase
if pos == -1:
    print("La palabra clave no fue encontrada... sigue buscando")
    
# Si sí está, arroja un mensaje 
else:
    print(f"¡Palabra encontrada! Empieza en la posición {pos}")

# print("=======================================================")

# print("Método N° [3]".upper())   

# print("\n- len(): Longitud de una cadena (o lista)\n".upper())
  
# print("len() Devuelve cuántos caracteres (o elementos) hay.")


