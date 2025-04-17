# Aquecendo na programação

# 1) Exibir o número maior
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > num2:
    print(f"O maior número é: {num1}")
elif num2 > num1:
    print(f"O maior número é: {num2}")
else:
    print("Os números são iguais.")

# 2) Crescimento ou decrescimento
percentual = float(input("Digite o percentual de crescimento da produção: "))
if percentual > 0:
    print("Houve crescimento.")
elif percentual < 0:
    print("Houve decrescimento.")
else:
    print("A produção permaneceu estável.")

# 3) Vogal ou consoante
letra = input("Digite uma letra: ").lower()
if letra in "aeiou":
    print("A letra é uma vogal.")
elif letra.isalpha():
    print("A letra é uma consoante.")
else:
    print("Isso não é uma letra.")

# 4) Valor mais alto e mais baixo
ano1 = float(input("Digite o valor médio do primeiro ano: "))
ano2 = float(input("Digite o valor médio do segundo ano: "))
ano3 = float(input("Digite o valor médio do terceiro ano: "))
print(f"Maior valor: {max(ano1, ano2, ano3)}")
print(f"Menor valor: {min(ano1, ano2, ano3)}")

# 5) Produto mais barato
preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))
if preco1 < preco2 and preco1 < preco3:
    print("Compre o primeiro produto.")
elif preco2 < preco3:
    print("Compre o segundo produto.")
else:
    print("Compre o terceiro produto.")

# 6) Números em ordem decrescente
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
numeros = [num1, num2, num3]
numeros.sort(reverse=True)
print("Números em ordem decrescente:", numeros)

# 7) Turno de estudo
turno = input("Digite o turno que você estuda (manhã, tarde, noite): ").lower()
if turno == "manhã":
    print("Bom Dia!")
elif turno == "tarde":
    print("Boa Tarde!")
elif turno == "noite":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

# 8) Par ou ímpar
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 9) Inteiro ou decimal
numero = float(input("Digite um número: "))
if numero == int(numero):
    print("O número é inteiro.")
else:
    print("O número é decimal.")

# Momento dos projetos

# 10) Operações e análise de números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/" and num2 != 0:
    resultado = num1 / num2
else:
    print("Operação inválida.")
    exit()
print(f"Resultado: {resultado}")
print("Par" if resultado % 2 == 0 else "Ímpar")
print("Positivo" if resultado > 0 else "Negativo")
print("Inteiro" if resultado == int(resultado) else "Decimal")

# 11) Triângulo
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles.")
    else:
        print("Triângulo Escaleno.")
else:
    print("Os lados não formam um triângulo.")

# 12) Combustíveis com desconto
litros = float(input("Digite a quantidade de litros: "))
tipo = input("Digite o tipo de combustível (E para etanol, D para diesel): ").upper()
if tipo == "E":
    preco_litro = 1.70
    desconto = 0.02 if litros <= 15 else 0.04
elif tipo == "D":
    preco_litro = 2.00
    desconto = 0.03 if litros <= 15 else 0.05
else:
    print("Tipo de combustível inválido.")
    exit()
valor_desconto = preco_litro * litros * desconto
valor_total = preco_litro * litros - valor_desconto
print(f"Valor a ser pago: R$ {valor_total:.2f}")

# 13) Análise de vendas
vendas_2022 = int(input("Digite a quantidade de vendas em 2022: "))
vendas_2023 = int(input("Digite a quantidade de vendas em 2023: "))
variacao = ((vendas_2023 - vendas_2022) / vendas_2022) * 100
print(f"Variação percentual: {variacao:.2f}%")
if variacao > 20:
    print("Bonificação para o time de vendas.")
elif 2 <= variacao <= 20:
    print("Pequena bonificação para o time de vendas.")
elif -10 <= variacao < 2:
    print("Planejamento de políticas de incentivo às vendas.")
else:
    print("Corte de gastos.")