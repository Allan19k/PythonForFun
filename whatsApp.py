import pywhatkit

numero_telefono = input("Ingrese el número de teléfono (con código de país): ")
mensaje = input("Ingrese el mensaje que desea enviar: ")
hora = int(input("Ingrese la hora (en formato 24 horas): "))
minuto = int(input("Ingrese los minutos: "))

pywhatkit.sendwhatmsg(numero_telefono, mensaje, hora, minuto)
print("Mensaje programado para ser enviado a las", hora, ":", minuto)