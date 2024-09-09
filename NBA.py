def nba_extrap(ppg, mpg):
    # Si mpg es 0, devolver 0 para evitar división por 0
    if mpg == 0:
        return 0

    # Extrapolar los puntos por 48 minutos y redondear al décimo más cercano
    extrapolated_ppg = (ppg / mpg) * 48
    return round(extrapolated_ppg, 1)


# Ejemplo de uso:
ppg = float(input("Ingresa los puntos por partido (ppg): "))
mpg = float(input("Ingresa los minutos por partido (mpg): "))

result = nba_extrap(ppg, mpg)
print(f"Puntos extrapolados por 48 minutos: {result}")
