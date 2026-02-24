import schedule
import time

def saludo():
    print("¡Hola! Esta es una tarea programada en Python usando las librerías de schedule y time.")
# Programar la tarea para que se ejecute cada 10 segundos
schedule.every(3).seconds.do(saludo)

# Bucle para mantener el programa en ejecución y verificar las tareas programadas
while True:
    schedule.run_pending()
    time.sleep(0.5)