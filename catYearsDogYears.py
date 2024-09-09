# Calcula la edad del perro y el gato en años humanos
def calculate_ages(humanYears):
    # Inicializamos los años de gato y perro
    catYears = 0
    dogYears = 0

    # Calculamos los años para el primer año humano
    if humanYears >= 1:
        catYears += 15
        dogYears += 15

    # Calculamos los años para el segundo año humano
    if humanYears >= 2:
        catYears += 9
        dogYears += 9

    # Calculamos los años para los años humanos adicionales (más de 2)
    if humanYears > 2:
        catYears += (humanYears - 2) * 4
        dogYears += (humanYears - 2) * 5

    return [humanYears, catYears, dogYears]


# Ejemplo de uso:
human_years = int(input("Dame los años humanos: "))
ages = calculate_ages(human_years)

# Mostrar el resultado con el texto deseado
print(f"La edad del gato en años es: {ages[1]}")
print(f"La edad del perro en años es: {ages[2]}")

# Muestra el tipo de datos devuelto por la función
print(type(ages))

