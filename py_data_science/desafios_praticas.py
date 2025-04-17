# Aquecimento

# 1. Instalar a versão 3.7.1 da biblioteca matplotlib
# Comando para ser executado no terminal:
# pip install matplotlib==3.7.1

# 2. Importar a biblioteca numpy com o alias np
import numpy as np

# 3. Escolher aleatoriamente um número da lista
import random
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
numero_escolhido = random.choice(lista)
print(f"Número escolhido aleatoriamente: {numero_escolhido}")

# 4. Sortear um número inteiro positivo menor que 100
numero_sorteado = random.randrange(100)
print(f"Número sorteado: {numero_sorteado}")

# 5. Calcular a potência do 1º número elevado ao 2º
import math
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
potencia = math.pow(num1, num2)
print(f"{num1} elevado a {num2} é igual a {potencia}")

# Aplicando a projetos

# 6. Sortear uma pessoa seguidora de uma rede social
num_participantes = int(input("Digite o número de participantes do sorteio: "))
numero_ganhador = random.randint(1, num_participantes)
print(f"O número sorteado foi: {numero_ganhador}")

# 7. Gerar um token de acesso
nome = input("Digite seu nome: ")
token = random.randrange(1000, 9999, 2)  # Gera números pares
print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)!")

# 8. Selecionar 3 frutas aleatórias para a salada de frutas
frutas = ["maçã", "banana", "uva", "pêra", 
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]
salada = random.sample(frutas, 3)
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

# Listas fornecidas
nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

# Processando e exibindo os nomes completos
for nome, sobrenome in zip(nomes, sobrenomes):
    nome_completo = f"{nome.capitalize()} {sobrenome.capitalize()}"
    print(f"Nome completo: {nome_completo}")


#################################################################################################################################################################
#9. Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.
#O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.
#Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).
#Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.
#"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custari


# Listas com os dados das cidades
cidades = ["Salvador", "Fortaleza", "Natal", "Aracaju"]
hotel = [150, 150, 150, 150]  # Custo da diária do hotel
distancia = [850, 800, 300, 550]  # Distância de Recife para cada cidade (km)
passeio = [200, 400, 250, 300]  # Custo diário de passeios e alimentação
carro_consumo = 14  # Consumo do carro (km/l)
preco_gasolina = 5  # Preço do litro da gasolina (R$)

def gasto_hotel(dias, cidade_index):
    """Calcula o gasto com hotel."""
    return dias * hotel[cidade_index]

def gasto_gasolina(cidade_index):
    """Calcula o gasto com gasolina."""
    distancia_total = distancia[cidade_index] * 2  # Ida e volta
    litros_necessarios = distancia_total / carro_consumo
    return litros_necessarios * preco_gasolina

def gasto_passeio(dias, cidade_index):
    """Calcula o gasto com passeios e alimentação."""
    return dias * passeio[cidade_index]

# Solicitando os dados ao usuário
print("Destinos disponíveis:")
for i, cidade in enumerate(cidades):
    print(f"{i + 1}. {cidade}")

cidade_index = int(input("Escolha o destino (1-4): ")) - 1
dias = int(input("Quantos dias você deseja ficar? "))

# Calculando os gastos
gasto_total_hotel = gasto_hotel(dias, cidade_index)
gasto_total_gasolina = gasto_gasolina(cidade_index)
gasto_total_passeio = gasto_passeio(dias, cidade_index)

# Soma total dos gastos
gasto_total = gasto_total_hotel + gasto_total_gasolina + gasto_total_passeio

# Exibindo o resultado
print(f"\nCom base nos gastos definidos, uma viagem de {dias} dias para {cidades[cidade_index]} saindo de Recife custaria R$ {gasto_total:.2f}")


##########################################################################################################################################################

""" 10. Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função embutida filter() recebe uma função (no nosso exemplo uma função lambda) e filtra um iterável de acordo com a função. Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.

Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código. """

# Recebendo a frase da pessoa usuária
frase = input("Digite uma frase: ")

# Tratando a frase para remover pontuações
frase_tratada = frase.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ")

# Filtrando palavras com tamanho maior ou igual a 5
palavras_filtradas = list(filter(lambda palavra: len(palavra) >= 5, frase_tratada.split()))

# Exibindo o resultado
print(f"Palavras com 5 ou mais caracteres: {palavras_filtradas}")