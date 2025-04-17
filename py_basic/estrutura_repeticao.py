# Laço WHILE
# Exemplo 1: Contagem de 1 a 5
contador = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa o contador
# Saída: Contador: 1, Contador: 2, ..., Contador: 5

# Exemplo 2: Entrada de dados válida
idade = int(input("Digite sua idade (entre 0 e 120): "))
while idade < 0 or idade > 120:
    print("Idade inválida. Tente novamente.")
    idade = int(input("Digite sua idade (entre 0 e 120): "))
print(f"Idade registrada: {idade}")
# Saída: Solicita até que a idade seja válida

# Exemplo 3: Loop infinito com condição de parada
while True:
    resposta = input("Digite 'sair' para encerrar: ").lower()
    if resposta == "sair":
        print("Encerrando o programa...")
        break  # Sai do laço
# Saída: Sai do loop quando o usuário digitar "sair"

# Laço FOR
# Exemplo 1: Iterando sobre uma lista
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"Fruta: {fruta}")
# Saída: Fruta: maçã, Fruta: banana, Fruta: laranja

# Exemplo 2: Iterando sobre um intervalo de números
for numero in range(1, 6):  # De 1 a 5 (6 não é incluído)
    print(f"Número: {numero}")
# Saída: Número: 1, Número: 2, ..., Número: 5

# Exemplo 3: Iterando sobre uma string
palavra = "Python"
for letra in palavra:
    print(f"Letra: {letra}")
# Saída: Letra: P, Letra: y, ..., Letra: n

# Exemplo 4: Usando o FOR com a função enumerate
frutas = ["maçã", "banana", "laranja"]
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")
# Saída: Índice 0: maçã, Índice 1: banana, Índice 2: laranja

# Exemplo 5: Laço FOR com condição
for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")
# Saída: Identifica números pares e ímpares de 1 a 10

# Exemplo 6: FOR com BREAK e CONTINUE
for numero in range(1, 11):
    if numero == 5:
        print("Interrompendo o laço no número 5.")
        break  # Sai do laço
    if numero % 2 == 0:
        continue  # Pula para a próxima iteração
    print(f"Número ímpar: {numero}")
# Saída: Mostra números ímpares até o 5, mas interrompe no 5

# Exemplo 7: FOR com ELSE
for numero in range(1, 6):
    print(f"Número: {numero}")
else:
    print("Laço concluído com sucesso!")
# Saída: Imprime números de 1 a 5 e depois "Laço concluído com sucesso!"