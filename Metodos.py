# print("\n---------------------------------")
# print("------> métodos en python <------".upper())
# print("---------------------------------\n")

# print("-------------------------------------------")

# print("Método N° [1]".upper())
# print("\n- len(): Longitud de una cadena (o lista)\n".upper())

# print("len() Devuelve cuántos caracteres (o elementos) hay.")

# print("\nEjemplo N° [1]")

# # Pide ingresar el nombre del usuario 
# nombre = input("Ingresa tu nombre: ".lower())

# # Da de resultado 9 (incluye el espacio)
# print(f"el nombre {nombre}, tiene: {len(nombre)} caracteres")

# print("\nEjemplo N° [2]")

# # Pide los datos al usuario almacenandolos en una lista
# palabras = [input("Ingrese una palabra: ".lower()), input("Ingrese otra palabra: ".lower()), input("Ingrese una última palabra: ".lower())]

# print("Se contará cada caracter, incluyendo los espacios ingresados")

# # Cuenta cuantas caracteres tiene cada letra
# print(f"\nLa palabra {palabras[0]} tiene {len(palabras[0])} letras o caracteres")
# print(f"La palabra {palabras[1]} tiene {len(palabras[1])} letras o caracteres")
# print(f"La palabra {palabras[2]} tiene {len(palabras[2])} letras o caracteres ")

print("------------------------------------------------")

print("Método N° [2]")
print("\n- .find(): buscar una subcadena\n".upper())

print(".find() Devuelve la posición (índice) donde aparece por primera vez uuna letra o palabra. Si no se encuentra, devuelve -1.")

print("\nEjemplo N° [1]")

frase = input("Ingresa una frase: ".lower())
letra = input("Ingrese una sola letra (ej: a): ".lower())


if letra not in frase:
    print(f"La letra '{letra}' NO está en la frase: '{frase}'")
else:
    print(f"La letra '{letra}' SI está en la frase '{frase}'")
    





