# Operador AND
# Retorna True somente se ambas as condições forem verdadeiras
idade = 20
tem_carteira = True
print(idade >= 18 and tem_carteira)  # Saída: True

idade = 16
tem_carteira = True
print(idade >= 18 and tem_carteira)  # Saída: False

# Operador OR
# Retorna True se pelo menos uma das condições for verdadeira
idade = 16
tem_autorizacao = True
print(idade >= 18 or tem_autorizacao)  # Saída: True

idade = 16
tem_autorizacao = False
print(idade >= 18 or tem_autorizacao)  # Saída: False

# Operador NOT
# Inverte o valor lógico de uma condição
tem_ingresso = False
print(not tem_ingresso)  # Saída: True

tem_ingresso = True
print(not tem_ingresso)  # Saída: False

# Combinação de Operadores Lógicos
idade = 20
tem_carteira = True
tem_autorizacao = False
print((idade >= 18 and tem_carteira) or tem_autorizacao)  # Saída: True

# Exemplo Prático: Verificar se um número está dentro de um intervalo
numero = 15
print(numero > 10 and numero < 20)  # Saída: True

# Exemplo Prático: Verificar se um número está fora de um intervalo
numero = 25
print(not (numero > 10 and numero < 20))  # Saída: True

# Exemplo Prático: Login Simples
usuario = "admin"
senha = "1234"
print(usuario == "admin" and senha == "1234")  # Saída: True

# Exemplo Prático: Acesso com múltiplas condições
idade = 17
tem_autorizacao = True
tem_ingresso = True
print((idade >= 18 or tem_autorizacao) and tem_ingresso)  # Saída: True