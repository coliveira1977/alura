#1. Escreva um código que lê a lista abaixo e faça:
#lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
print("Tamanho da lista:", len(lista))  # Exibe o tamanho da lista)
print(f"Tamanho da lista: {len(lista)}")  # Exibe o tamanho da lista com f-string
print("Maior número da lista:", max(lista))  # Exibe o maior número da lista
print("Menor número da lista:", min(lista))  # Exibe o menor número da lista
print("Soma dos números da lista:", sum(lista))  # Exibe a soma dos números da lista
print("Lista ordenada:", sorted(lista))  # Exibe a lista ordenada
print("Lista invertida:", sorted(lista, reverse=True))  # Exibe a lista invertida
print("Lista original:", lista)  # Exibe a lista original



#2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

#Tabuada do 7:
#7 x 0 = 0
#7 x 1 = 7
#[...]
#7 x 10 = 70

def tabuada(numero):
    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Digite um número para gerar a tabuada: "))
tabuada(numero)

#3. Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
multiplicador = int(input('Escolha o multiplicador: '))
multiplos = list(map(lambda x: x * multiplicador, lista))
print(f'Lista de multiplos de {multiplicador}: {multiplos}')

# 3. Escreva uma função que receba uma lista de números inteiros e retorne a soma dos números pares da lista.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def soma_pares(lista):
    return sum(filter(lambda x: x % 2 == 0, lista)) # Usando filter para filtrar os números pares e sum para somá-los

print('Somatória dos Números Pares da Lista= ', soma_pares(lista))  # Exibe a soma dos números pares da lista    

#4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
#  Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = list(map(lambda x: x ** 2, lista))
print(quadrado)

# 5. Você foi contratado(a) como cientista de dados de uma associação de skate. 
# Para analisar as notas recebidas de skatistas em algumas competições ao longo do ano, 
# você precisa criar um código que calcula a pontuação dos(as) atletas. 
# Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.
# Para calcular a pontuação de um(a) skatista, 
# você precisa eliminar a maior e a menor pontuação dentre as 5 notas e tirar a média das 3 notas que sobraram. 
# Retorne a média para apresentar o texto:
#"Nota da manobra: [media]"
# receber 5 notas, descartar a maior e a menor, retornar a média das 3 notas restantes
notas = []

for i in range(5):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

# Remove a maior e a menor nota
print(notas)
notas.remove(max(notas))
notas.remove(min(notas))

# Calcula a média das 3 notas restantes
media = sum(notas) / len(notas)

# Exibe o resultado formatado
print(f"Nota da manobra: {media:.2f}")