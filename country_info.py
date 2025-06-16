from countryinfo import CountryInfo

# Crear una instancia de CountryInfo para México (puedes cambiar el país a tu elección, pero debe estar escrito en íngles)
country = CountryInfo('Mexico')

# Obtener el nombre oficial
print(f"Nombre oficial: {country.name()}")

# Obtener la capital
print(f"Capital: {country.capital()}")

# Obtener la población
print(f"Población: {country.population()}")

# Obtener las fronteras
print(f"Fronteras: {country.borders()}")

# Obtener el área
print(f"Área: {country.area()} km²")

# Obtener el idioma oficial
print(f"Idioma oficial: {country.languages()}")

# Obtener la moneda
print(f"Moneda: {country.currencies()}")

# Obtener la zona horaria
print(f"Zona horaria: {country.timezones()}")

