# print("\n" + "=" * 40)
# print(" MÉTODOS EN PYTHON ".center(40, "="))
# print("=" * 40 + "\n")

# print("----------------------------------------------------")

# print("==== MÉTODO N°1: .LEN() ====")

# print("\n- len(): Longitud de una cadena (o lista)\n".upper())

# print(".len() Devuelve cuántos caracteres (o elementos) hay.\n")

# print("----------------------------------------------------")

# print("==== EJEMPLO N°1 ====")

# # Pide ingresar el nombre del usuario 
# nombre = input("\nIngresa tu nombre: ".lower())

# # Muestra la cantidad de letras que hay en la palabra
# print(f"\nEl nombre {nombre}, tiene: {len(nombre)} caracteres")

# print("----------------------------------------------------")

# print("==== EJEMPLO N°2 ====")

# # Pide los datos al usuario almacenandolos en una lista
# palabras = [input("\nIngrese una palabra: ".lower()), input("Ingrese otra palabra: ".lower()), input("Ingrese una última palabra: ".lower())]

# # Cuenta cuantas letras tiene cada palabra
# print(f"\nLa palabra '{palabras[0]}' tiene {len(palabras[0])} letras")
# print(f"La palabra '{palabras[1]}' tiene {len(palabras[1])} letras")
# print(f"La palabra '{palabras[2]}' tiene {len(palabras[2])} letras")

# print("----------------------------------------------------")

# print("==== MÉTODO N°2: .FIND() ====")

# print("\n- .find(): buscar una subcadena\n".upper())

# print(".find() Devuelve la posición (índice) donde aparece por primera vez una letra o palabra. Si no se encuentra, devuelve -1.\n")

# print("----------------------------------------------------")

# print("==== EJEMPLO N°1 ====")

# # Pide los datos al usuario
# frase = input("\nIngresa una frase: ").lower()
# letra = input("Ingrese una sola letra (ej: a): ").lower()

# # si la letra ingresada por el usuario no está en la frase
# if letra not in frase:
#     print(f"\nLa letra '{letra}' NO está en la frase: '{frase}'. Por lo cual arroja un {frase.find(letra)} ")
    
# # Si la letra ingresada por el usuario sí está en la frase
# else:
#     posicion = frase.find(letra)
#     print(f"\nLa letra '{letra}' SI está en la frase '{frase}'")
#     print(f"Aparece por primera vez en la posición {posicion}")

# print("----------------------------------------------------")

# print("==== EJEMPLO N°2 ====")

# # Pide al usuario la frase y la palabra a buscar
# frase2 = input("\nEscribe una frase misteriosa: ").lower()
# clave = input("\nIngrese la palabra clave para buscar: ").lower()

# # Verifica si la palabra ingresada está en la frase
# pos = frase2.find(clave)

# # Si la palabra ingresada por el usuario no está en la frase
# if pos == -1:
#     print("\nLa palabra clave no fue encontrada... sigue buscando")
    
# # Si sí está, arroja un mensaje 
# else:
#     print(f"\n¡Palabra encontrada! Empieza en la posición {pos}")

# print("----------------------------------------------------")

# print("==== MÉTODO N°3: EXTRACCIÓN [ ] ====")  

# print("\n- extracción: obtener una parte de una cadena\n".upper())

# print("----------------------------------------------------")

# print("==== EJEMPLO N°1 ====")

# # Solicita una frase al usuario
# frase = input("\nEscribe una frase corta: ")

# # Muestra solo los primeros 5 letras
# print(f"\nLos primeros 5 caracteres son: '{frase[0:5]}'")

# print("----------------------------------------------------")

# print("==== EJEMPLO N°2 ====")

# palabra = input("\nEscribe una frase larga: ")

# # Extrae los caracteres desde la posición 1 hasta la 4
# print(f"\nLos caracteres del índice 1 al 4 son: '{palabra[1:5]}'")
# print(f"\nLos caracteres del índice 6 al 8 son: '{palabra[6:9]}'")

# print("----------------------------------------------------")



# print("\n- len(): Longitud de una cadena (o lista)\n".upper())
  
# print("len() Devuelve cuántos caracteres (o elementos) hay.")


