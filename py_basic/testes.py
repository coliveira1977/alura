print("\nExercício 4:")
temperaturas = []

while True:
    temp = float(input("Digite uma temperatura em Celsius (-273 para encerrar): "))
    if temp == -273:
        break
    temperaturas.append(temp)

if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"A média das temperaturas é {media:.2f}°C.")
else:
    print("Nenhuma temperatura foi informada.")