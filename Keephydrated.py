import math

def litres(time):
    # Calcula los litros de agua y redondea hacia abajo
    return math.floor(time * 0.5)

# Ejemplo de uso:
time = float(input("Ingresa el tiempo en horas: "))
result = litres(time)
print(f"Litros de agua que Nathan beberá: {result}")
