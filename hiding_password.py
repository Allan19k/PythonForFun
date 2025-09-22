import getpass

# pedirle al usuario que ingrese su usuario y contraseña
username = input("Ingrese su nombre de usuario: ")
# usar getpass para ocultar la entrada de la contraseña
password = getpass.getpass("Ingrese su contraseña: ") # la entrada no se mostrará en la consola

# mostrar el nombre de usuario y la contraseña ingresados
print("\nLogging in...")
print(f"Nombre de usuario: {username}")
print(f"Contraseña: [No se puede mostrar por su seguridad :)]")  # Mostrar un mensaje en lugar de la contraseña real