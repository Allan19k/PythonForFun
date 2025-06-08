import random
import emoji

# lista de tipos de clima con su representacion en emoji
climas = [
    ("Soleado", emoji.emojize(":sunny:", language='alias')),
    ("Nublado", emoji.emojize(":cloud:", language='alias')),
    ("Lluvioso", emoji.emojize(":cloud_with_rain:", language='alias')),
    ("Tormenta", emoji.emojize(":thunder_cloud_and_rain:", language='alias')),
    ("Nevado", emoji.emojize(":snowflake:", language='alias')),
    ("Ventoso", emoji.emojize(":wind_face:", language='alias')),
    ("Despejado", emoji.emojize(":sun_behind_small_cloud:", language='alias')),
    ("Húmedo", emoji.emojize(":droplet:", language='alias')),
    ("Niebla", emoji.emojize(":fog:", language='alias')),
    ("Calor", emoji.emojize(":fire:", language='alias')),
    ("Frío", emoji.emojize(":snowman:", language='alias')),
    ("Tornado", emoji.emojize(":tornado:", language='alias')),
    ("Huracán", emoji.emojize(":cyclone:", language='alias')),
    ("Arcoíris", emoji.emojize(":rainbow:", language='alias'))
    
]
# Seleccion aleatoria de un clima
clima_aleatorio = random.choice(climas)
# Imprimir el clima seleccionado
print(f"El clima seleccionado es: {clima_aleatorio[0]} {clima_aleatorio[1]}")
