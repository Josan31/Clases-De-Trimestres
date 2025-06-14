# contador = 1
# while contador <= 100:
#     print("contador", contador)
#     contador -= 1

print("--------------------------------")

while True:
    texto = input("Escribe algo (o escribe salir para terminar): ")
    if texto == "salir":
        break
    print(f"Escribiste {texto}")
# break detiene inmediatamente un ciclo (while o for), aunque la condición del ciclo siga siendo verdadera