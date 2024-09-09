def third_angle(angle1, angle2):
    # Calcula el tercer ángulo
    return 180 - (angle1 + angle2)

# Ejemplo de uso:
angle1 = int(input("Ingresa el primer ángulo: "))
angle2 = int(input("Ingresa el segundo ángulo: "))

result = third_angle(angle1, angle2)
print(f"El tercer ángulo es: {result}")
