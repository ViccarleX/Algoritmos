import math


def convert_to_16_9(x, y):
    # Calcula la nueva resolución de ancho con la relación 16:9
    new_x = math.ceil(y * 16 / 9)

    return new_x, y


# Ejemplo de uso:
x_resolution = int(input("Ingresa la resolución X (ancho): "))
y_resolution = int(input("Ingresa la resolución Y (altura): "))

new_x, new_y = convert_to_16_9(x_resolution, y_resolution)

print(f"La nueva resolución con relación de aspecto 16:9 es: {new_x}x{new_y}")
