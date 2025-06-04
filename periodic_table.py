import periodictable

# obtener dellates de un elemento por su numero atomico 
num_atomico = int(input("Ingrese el número atómico del elemento: "))
elemento = periodictable.elements[num_atomico]
# mostrar detalles del elemento
print(f"Elemento: {elemento.name}")
print(f"Símbolo: {elemento.symbol}")
print(f"Número atómico: {elemento.number}")
print(f"Masa atómica: {elemento.mass}")
print(f"Densidad: {elemento.density} g/cm³")
print(f"Masa atomica: {elemento.mass} u")
