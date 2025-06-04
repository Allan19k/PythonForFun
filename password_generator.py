# 🐍 Generador de contraseñas seguras y balanceadas 
# 60% letras (mayúsculas y minúsculas) y 40% mezcla de dígitos y símbolos

import string
import random

# 🔤 Caracteres disponibles
letras_mayus = list(string.ascii_uppercase) # Mayúsculas
letras_minus = list(string.ascii_lowercase) # Minúsculas
digitos = list(string.digits) # Dígitos del 0 al 9
simbolos = list(string.punctuation) # Símbolos especiales

# 📥 Pedir longitud de la contraseña al usuario
while True:
    longitud_input = input("Ingrese la longitud de la contraseña (mínimo 8 caracteres): ")
    try:
        longitud = int(longitud_input)
        if longitud < 8:
            print("⚠️ La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo.")
        else:
            break
    except ValueError:
        print("❌ Entrada inválida. Por favor, ingrese un número entero.")

# 🔢 Calcular proporciones
# 60% letras → se dividen entre mayúsculas y minúsculas
# 40% otros (dígitos y símbolos)
cant_letras = round(longitud * 0.3)  # 30% para mayúsculas, 30% para minúsculas
cant_otros = round(longitud * 0.2)   # 20% para dígitos, 20% para símbolos

# 🧱 Crear la contraseña
password = []

# Mezclar listas para evitar patrones
random.shuffle(letras_mayus)
random.shuffle(letras_minus)
random.shuffle(digitos)
random.shuffle(simbolos)

# Agregar letras (mayúsculas y minúsculas)
for i in range(cant_letras):
    password.append(letras_mayus[i])
    password.append(letras_minus[i])

# Agregar otros caracteres (dígitos y símbolos)
for i in range(cant_otros):
    password.append(digitos[i])
    password.append(simbolos[i])

# 🔀 Mezclar el resultado final para más seguridad
random.shuffle(password)

# 📎 Convertir la lista a cadena
password_final = ''.join(password)

# 📤 Mostrar la contraseña
print("\n🔐 Contraseña generada:")
print(password_final)
print("💡 ¡Recuerda guardarla en un lugar seguro!")












