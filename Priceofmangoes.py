def mango(quantity, price):
    # Calcula cuántos mangos se pagan (cada 3 mangos, solo se pagan 2)
    paid_mangoes = (quantity // 3) * 2 + (quantity % 3)

    # Calcula el costo total
    total_cost = paid_mangoes * price

    return total_cost


# Ejemplo de uso:
quantity = int(input("Ingresa la cantidad de mangos: "))
price = float(input("Ingresa el precio por mango: "))

result = mango(quantity, price)
print(f"El costo total es: {result}")
