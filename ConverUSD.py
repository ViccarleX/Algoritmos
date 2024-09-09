def usd_to_cny(usd):
    # Tasa de conversión de USD a CNY
    conversion_rate = 6.75

    # Calcula la cantidad en yuanes
    cny = usd * conversion_rate

    # Retorna el resultado en el formato especificado
    return f"{cny:.2f} Chinese Yuan"


# Ejemplo de uso:
usd_amount = int(input("Ingresa la cantidad de USD: "))
result = usd_to_cny(usd_amount)
print(result)
