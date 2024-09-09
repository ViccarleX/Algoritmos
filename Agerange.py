import math


def dating_range(age):
    if age > 14:
        # Fórmula para personas mayores de 14 años
        min_age = math.floor(age / 2 + 7)
        max_age = math.floor((age - 7) * 2)
    else:
        # Fórmula para personas menores o iguales a 14 años
        min_age = math.floor(age - 0.10 * age)
        max_age = math.floor(age + 0.10 * age)

    return f"{min_age}-{max_age}"


# Ejemplo de uso:
age = int(input("Ingresa tu edad: "))

result = dating_range(age)
print(f"Rango de edad recomendado: {result}")
