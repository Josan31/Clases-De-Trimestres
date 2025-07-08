print("===== CAJERO AUTOMÁTICO =====")

# Pregunta si el usuario desea entrar al cajero
pregunta = input("¿Desea entrar al cajero automático? (si/no): ").strip().lower() # Se eliminan espacios y se convierte a minúsculas 

if pregunta == "si":

    # Paso 1: Solicitar datos del usuario
    nombre2 = input("Ingrese su nombre de usuario: ")
    edad2 = int(input("Ingrese su edad: "))
    
    # Verifica si el usuario es mayor de edad
    if edad2 < 18:
        print(f"{nombre2}, debes tener al menos 18 años para usar el cajero automático.")
    else:
        # Pide la contraseña
        clave2 = input("Escriba su contraseña: ")
  
        # Repite mientras la contraseña sea incorrecta
        while clave2 != "123456":
            print(f"{nombre2}, contraseña incorrecta.")
            clave2 = input(f"{nombre2}, intenta de nuevo: ")
    
        # Acceso concedido si la contraseña es correcta
        print("Acceso concedido. Bienvenido")
    
        # Paso 2: Menú de opciones
        saldo = float(input("Ingrese su saldo actual: "))
        opciones = ""
        
        # Menú que se repite hasta que el usuario elija salir
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
                
                # Verifica si hay suficiente saldo
                if retiro <= saldo:
                    saldo -= retiro
                    print(f"Has retirado ${retiro}. Saldo restante: ${saldo}")
                else:
                    print("Fondos insuficientes.")
                
            elif opciones == "3":
                print("Gracias por usar el cajero automático. ¡Hasta pronto!")
            
            else:
                print(f"{nombre2}, la opción ingresada no es válida. Inténtalo de nuevo.")
             
# Si el usuario responde "no" desde el inicio
else:
    print("Acceso al programa cancelado. ¡Que tengas buen día!")