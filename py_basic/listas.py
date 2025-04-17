# Aula: Listas em Python

# Introdução às Listas
# As listas são uma estrutura de dados em Python que permitem armazenar múltiplos valores em uma única variável.
# Elas são ordenadas, mutáveis e podem conter elementos de diferentes tipos.

# Criando listas
print("Criando listas:")
lista_vazia = []  # Lista vazia
lista_numeros = [1, 2, 3, 4, 5]  # Lista de números inteiros
lista_mista = [1, "Python", 3.14, False]  # Lista com diferentes tipos de dados

print("Lista vazia:", lista_vazia)
print("Lista de números:", lista_numeros)
print("Lista mista:", lista_mista)

# Acessando elementos de uma lista
print("\nAcessando elementos de uma lista:")
print("Primeiro elemento da lista_numeros:", lista_numeros[0])  # Índice 0
print("Último elemento da lista_numeros:", lista_numeros[-1])  # Índice negativo

# Modificando elementos de uma lista
print("\nModificando elementos de uma lista:")
lista_numeros[0] = 10  # Alterando o primeiro elemento
print("Lista modificada:", lista_numeros)

# Adicionando elementos a uma lista
print("\nAdicionando elementos a uma lista:")
lista_numeros.append(6)  # Adiciona um elemento ao final da lista
print("Lista após append:", lista_numeros)

lista_numeros.insert(2, 15)  # Insere o número 15 na posição 2
print("Lista após insert:", lista_numeros)

# Removendo elementos de uma lista
print("\nRemovendo elementos de uma lista:")
lista_numeros.remove(15)  # Remove o primeiro elemento com o valor 15
print("Lista após remove:", lista_numeros)

elemento_removido = lista_numeros.pop()  # Remove e retorna o último elemento
print("Elemento removido com pop:", elemento_removido)
print("Lista após pop:", lista_numeros)

# Verificando a existência de um elemento
print("\nVerificando a existência de um elemento:")
print("O número 3 está na lista?", 3 in lista_numeros)
print("O número 10 está na lista?", 10 in lista_numeros)

# Iterando sobre uma lista
print("\nIterando sobre uma lista:")
for numero in lista_numeros:
    print(numero)

# Funções úteis para listas
print("\nFunções úteis para listas:")
print("Tamanho da lista:", len(lista_numeros))  # Retorna o número de elementos
print("Maior elemento:", max(lista_numeros))  # Retorna o maior elemento
print("Menor elemento:", min(lista_numeros))  # Retorna o menor elemento
print("Soma dos elementos:", sum(lista_numeros))  # Retorna a soma dos elementos

# Ordenando uma lista
print("\nOrdenando uma lista:")
lista_numeros.sort()  # Ordena a lista em ordem crescente
print("Lista ordenada (crescente):", lista_numeros)

lista_numeros.sort(reverse=True)  # Ordena a lista em ordem decrescente
print("Lista ordenada (decrescente):", lista_numeros)

# Copiando uma lista
print("\nCopiando uma lista:")
copia_lista = lista_numeros.copy()  # Cria uma cópia da lista
print("Cópia da lista:", copia_lista)

# Listas aninhadas
print("\nListas aninhadas:")
lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Lista de listas
print("Lista aninhada:", lista_aninhada)
print("Acessando elemento da lista aninhada:", lista_aninhada[1][2])  # Acessa o elemento 6

# Conclusão
# As listas são uma estrutura de dados poderosa e flexível em Python.
# Elas permitem armazenar, acessar e manipular coleções de dados de forma eficiente.