import random
import emoji

# Funcion para obtener un emoji de clima aleatorio
def get_random_weather_emoji():
    weather_emojis = [
        "☀️",  # Soleado
        "🌤️",  # Soleado con algunas nubes
        "🌤️",  # Parcialmente soleado
        "⛅",   # Sol detrás de una nube
        "🌥️",  # Sol detrás de una nube grande
        "🌦️",  # Soleaso y lluvia ligera
        "🌧️",  # Lluvia ligera
        "🌩️",  # Nube con relámpago
        "🌨️",  # Nube con nieve
        "🌪️",  # Tornado
        "🌫️",  # Niebla
        "❄️",   # Nieve
        "🌈",   # Arcoíris
        "💨"    # Mucho viento
    ]
    return random.choice(weather_emojis)
print("El clima de hoy:", get_random_weather_emoji())