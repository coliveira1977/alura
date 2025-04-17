# Aquecendo na programação

# 1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
print("Exercício 1:")
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num1 > num2:
    num1, num2 = num2, num1

for i in range(num1 + 1, num2):
    print(i)

# 2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, 
# com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.
print("\nExercício 2:")
colonia_a = 4
colonia_b = 10
taxa_a = 0.03
taxa_b = 0.015
dias = 0

while colonia_a < colonia_b:
    colonia_a += colonia_a * taxa_a
    colonia_b += colonia_b * taxa_b
    dias += 1

print(f"Serão necessários {dias} dias para a colônia A ultrapassar ou igualar a colônia B.")

# 3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. 
# Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. 
# Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.
print("\nExercício 3:")
notas = []
while len(notas) < 15:
    nota = float(input("Digite uma nota de 0 a 5: "))
    if 0 <= nota <= 5:
        notas.append(nota)
    else:
        print("Nota inválida. Tente novamente.")

# 4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. 
# A leitura deve ser encerrada ao ser enviado o valor -273°C.
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

# 5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. 
# Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. 
# Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.
print("\nExercício 5:")
num = int(input("Digite um número inteiro para calcular o fatorial: "))

fatorial = 1
for i in range(1, num + 1):
    fatorial *= i

print(f"O fatorial de {num} é {fatorial}.")

# Momento dos projetos

# 6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária.
print("\nExercício 6:")
num = int(input("Digite um número inteiro para gerar a tabuada (1 a 10): "))

print(f"Tabuada do {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 7) Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
print("\nExercício 7:")
num = int(input("Digite um número inteiro para verificar se é primo: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} não é um número primo.")
            break
    else:
        print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")

# 8) Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100].
print("\nExercício 8:")
intervalos = [0, 0, 0, 0]

while True:
    idade = int(input("Digite a idade (número negativo para encerrar): "))
    if idade < 0:
        break
    elif 0 <= idade <= 25:
        intervalos[0] += 1
    elif 26 <= idade <= 50:
        intervalos[1] += 1
    elif 51 <= idade <= 75:
        intervalos[2] += 1
    elif 76 <= idade <= 100:
        intervalos[3] += 1

print(f"Distribuição de idades:")
print(f"[0-25]: {intervalos[0]}")
print(f"[26-50]: {intervalos[1]}")
print(f"[51-75]: {intervalos[2]}")
print(f"[76-100]: {intervalos[3]}")

# 9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as).
print("\nExercício 9:")
votos = [0, 0, 0, 0, 0, 0]

for i in range(20):
    voto = int(input("Digite o número do candidato (1-4), nulo (5) ou branco (6): "))
    if 1 <= voto <= 6:
        votos[voto - 1] += 1
    else:
        print("Voto inválido. Tente novamente.")

total_votos = sum(votos)
print(f"Resultado da eleição:")
for i in range(4):
    print(f"Candidato {i + 1}: {votos[i]} votos")
print(f"Votos nulos: {votos[4]} ({(votos[4] / total_votos) * 100:.2f}%)")
print(f"Votos em branco: {votos[5]} ({(votos[5] / total_votos) * 100:.2f}%)")