def round_to_two_decimals(number):
    # Redondea el número a dos decimales
    return round(number, 2)

# Ejemplo de uso:
number = float(input("Ingresa un número: "))
result = round_to_two_decimals(number)
print(f"Número redondeado a dos decimales: {result:.2f}")
