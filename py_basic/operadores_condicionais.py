# Operador de Igualdade (==)
a = 10
b = 20
print(a == b)  # Saída: False
print(a == 10)  # Saída: True

# Operador de Diferença (!=)
print(a != b)  # Saída: True
print(a != 10)  # Saída: False

# Operador Maior que (>)
print(a > b)  # Saída: False
print(b > a)  # Saída: True

# Operador Menor que (<)
print(a < b)  # Saída: True
print(b < a)  # Saída: False

# Operador Maior ou Igual (>=)
print(a >= 10)  # Saída: True
print(b >= 30)  # Saída: False

# Operador Menor ou Igual (<=)
print(a <= 10)  # Saída: True
print(b <= 15)  # Saída: False

# Exemplo Prático 1: Verificar se um número é positivo
numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")
elif numero == 0:
    print("O número é zero.")
else:
    print("O número é negativo.")

# Exemplo Prático 2: Verificar se uma pessoa é maior de idade
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# Exemplo Prático 3: Comparar dois números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if num1 > num2:
    print(f"{num1} é maior que {num2}.")
elif num1 < num2:
    print(f"{num1} é menor que {num2}.")
else:
    print(f"{num1} é igual a {num2}.")

# Exemplo Prático 4: Verificar se um número está dentro de um intervalo
numero = int(input("Digite um número: "))
if 10 <= numero <= 20:
    print("O número está entre 10 e 20.")
else:
    print("O número está fora do intervalo.")

# Exemplo Prático 5: Verificar se uma string é igual a outra (case-sensitive)
palavra = input("Digite uma palavra: ")
if palavra == "Python":
    print("Você digitou Python!")
else:
    print("Você digitou outra coisa.")