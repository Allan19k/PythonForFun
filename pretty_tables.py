# pip install PrettyTable 
from prettytable import PrettyTable

# Crear una tabla
tabla = PrettyTable(["no. de articulo", "cantidad", "descripcion","marca", "precio unitario","precio total"])
# Agregar filas a la tabla
tabla.add_row([1, 1, "Atun", "El Dorado", 12.50, 12.50])
tabla.add_row([2, 4, "Leche UHT", "NutriLeche", 25.9, 103.6])
tabla.add_row([3, 2, "Galletas", "María", 25.00, 50.00])
tabla.add_row([4, 1, "Cereal", "Cheerios", 65.00, 65.00])
tabla.add_row([5, 1, "Avena", "No 1", 25.9, 25.9])
tabla.add_row([6, 1, "crema", "Lala", 30.00, 30.00])
tabla.add_row([7, 0.582, "Tomate ", "Saladet", 25.00, 14.55])
tabla.add_row([8, 1.158, "Cebolla", "Blanca", 28.00, 32.45])
tabla.add_row([9, 1, "Pimiento Morron", "Arcoiris", 75.00, 75.00])
tabla.add_row([10, 1, "Aguacate Hass", "Alsuper", 25.00, 25.00])
tabla.add_row([11, 0.850, "Limón", "Eureka", 80.00, 68.00])
tabla.add_row([12, 1, "Pasta", "La Moderna", 20.00, 20.00])
tabla.add_row([13, 1, "Salsa de tomate", "La Costeña", 25.00, 25.00])
tabla.add_row([14, 0.600, "Carne molida especial", "Alsuper", 120.00, 72.00])
tabla.add_row([15, 0.580, "Pepino", "Alsuper", 20.00, 11.60])
tabla.add_row([16, 1, "Papel higienico", "Charmin", 50.00, 50.00])
tabla.add_row([17, 1, "Detergente", "Ariel", 100.00, 100.00])
tabla.add_row([18, 1, "Suavizante", "Suavitel", 80.00, 80.00])
tabla.add_row([19, 1, "Jabón de tocador", "Palmolive", 25.00, 25.00])
tabla.add_row([20, 1, "Jabón de lavar", "Zote", 20.00, 20.00])
tabla.add_row([21, 1, "Desodorante", "Dove", 50.00, 50.00])
tabla.add_row([22, 1, "Pasta de dientes", "Colgate", 30.00, 30.00])
tabla.add_row([23, 2.500, "Papa blanca sin lavar", "Alsuper", 13.00, 32.50])
tabla.add_row([24, 1, "Cereal de avena", "Quaker", 50.00, 50.00])
# Mostrar la tabla
print(tabla)

