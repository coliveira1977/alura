# Coleta e amostragem de dados
# 1. Nome
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# 2. Nome e idade
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print(f"Olá, {nome}, você tem {idade} anos.")

# 3. Nome, idade e altura
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura em metros: ")
print(f"Olá, {nome}, você tem {idade} anos e mede {altura} metros!")

# Calculadora com operadores
# 1. Soma de dois valores
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print(f"A soma dos dois números é: {num1 + num2}")

# 2. Soma de três valores
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
print(f"A soma dos três números é: {num1 + num2 + num3}")

# 3. Subtração
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print(f"A subtração do primeiro pelo segundo número é: {num1 - num2}")

# 4. Multiplicação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print(f"A multiplicação dos dois números é: {num1 * num2}")

# 5. Divisão
num1 = float(input("Digite o numerador: "))
num2 = float(input("Digite o denominador (não pode ser 0): "))
if num2 != 0:
    print(f"A divisão é: {num1 / num2}")
else:
    print("Erro: o denominador não pode ser 0.")

# 6. Exponenciação
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
print(f"O resultado da exponenciação é: {base ** expoente}")

# 7. Divisão inteira
num1 = float(input("Digite o numerador: "))
num2 = float(input("Digite o denominador (não pode ser 0): "))
if num2 != 0:
    print(f"A divisão inteira é: {num1 // num2}")
else:
    print("Erro: o denominador não pode ser 0.")

# 8. Resto da divisão
num1 = float(input("Digite o numerador: "))
num2 = float(input("Digite o denominador (não pode ser 0): "))
if num2 != 0:
    print(f"O resto da divisão é: {num1 % num2}")
else:
    print("Erro: o denominador não pode ser 0.")

# 9. Média de três notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media:.2f}")

# 10. Média ponderada
pesos = [1, 2, 3, 4]
valores = [5, 12, 20, 15]
media_ponderada = sum(v * p for v, p in zip(valores, pesos)) / sum(pesos)
print(f"A média ponderada é: {media_ponderada:.2f}")

# Editando textos
# 1. Imprimir uma frase
frase = "Python é incrível!"
print(frase)

# 2. Solicitar uma frase e imprimir
frase = input("Digite uma frase: ")
print(frase)

# 3. Frase em maiúsculas
frase = input("Digite uma frase: ")
print(frase.upper())

# 4. Frase em minúsculas
frase = input("Digite uma frase: ")
print(frase.lower())

# 5. Frase sem espaços no início e no fim
frase = "   Python é incrível!   "
print(frase.strip())

# 6. Solicitar frase e remover espaços
frase = input("Digite uma frase: ")
print(frase.strip())

# 7. Frase sem espaços e em minúsculas
frase = input("Digite uma frase: ")
print(frase.strip().lower())

# 8. Substituir vogais "e" por "f"
frase = input("Digite uma frase: ")
print(frase.replace("e", "f").replace("E", "F"))

# 9. Substituir vogais "a" por "@"
frase = input("Digite uma frase: ")
print(frase.replace("a", "@").replace("A", "@"))

# 10. Substituir consoantes "s" por "$"
frase = input("Digite uma frase: ")
print(frase.replace("s", "$").replace("S", "$"))