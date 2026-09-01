clave_secreta = "python123"
intentos = 3

while intentos > 0:
    clave = input("Introduce la contraseña: ")

    if clave == clave_secreta:
        print("¡Acceso concedido!")
        break
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Intentos restantes: {intentos}")

if intentos == 0:
    print("Sistema bloqueado.")