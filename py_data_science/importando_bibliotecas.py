import matplotlib.pyplot as plt
from random import choice, randrange, sample, randint
import math
import numpy as np

estudantes = ['Juan', 'Pedro', 'Maria', 'Ana']
notas = [8.5, 7.0, 9.0, 6.5]

help(choice)

print(choice(estudantes))
print(choice(estudantes))
print(choice(estudantes))
print(choice(estudantes))


plt.bar(x = estudantes, height = notas)
#plt.xlabel('Estudantes')
#plt.ylabel('Notas')
#plt.title('Notas dos Estudantes')
plt.show()

plt.plot(estudantes, notas)
plt.show()

lista = []
for i in range(0, 20):
  lista.append(randrange(100))
print(sample(lista, 5))

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {math.sqrt(n)}")


# Exemplo de arredondamento para cima
receita = 1000
preco_unitario = 15
# Calcula o número de itens vendidos e arredonda para cima
itens_vendidos = math.ceil(receita / preco_unitario)
print(f"Número de itens vendidos: {itens_vendidos}")


# 3. Escolher aleatoriamente um número da lista (from random import choice)

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
numero_escolhido = choice(lista)
print(f"Número escolhido aleatoriamente: {numero_escolhido}")

# 4. Sortear um número inteiro positivo menor que 100 (from random import randrange)
numero_sorteado = randrange(100)
print(f"Número sorteado: {numero_sorteado}")

# 5. Calcular a potência do 1º número elevado ao 2º (import math)
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
potencia = math.pow(num1, num2)
print(f"{num1} elevado a {num2} é igual a {potencia}")

# 6. Sortear uma pessoa seguidora de uma rede social
num_participantes = int(input("Digite o número de participantes do sorteio: "))
numero_ganhador = randint(1, num_participantes)
print(f"O número sorteado foi: {numero_ganhador}")

# 7. Gerar um token de acesso
nome = input("Digite seu nome: ")
token = randrange(1000, 9999, 2)  # Gera números pares
print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!")

# 8. Selecionar 3 frutas aleatórias para a salada de frutas
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
salada = sample(frutas, 3)
print(f"As frutas escolhidas para a salada surpresa são: {salada}")

# 9. Calcular a raiz quadrada e identificar números com raízes inteiras
numeros = [2, 8, 15, 23, 91, 112, 256]
for numero in numeros:
    raiz = math.sqrt(numero)
    if raiz // 1 == raiz:  # Verifica se a raiz é inteira
        print(f"O número {numero} possui raiz inteira: {int(raiz)}")

# 10. Calcular o custo da grama para jardins circulares
raio = float(input("Digite o raio do jardim circular (em metros): "))
preco_m2 = 25.00
area = math.pi * math.pow(raio, 2)  # A = π * r^2
custo = area * preco_m2
print(f"O custo total para cobrir o jardim é de R$ {custo:.2f}")