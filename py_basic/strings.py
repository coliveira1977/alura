# Criando Strings
texto1 = 'Olá, mundo!'
texto2 = "Python é incrível!"
print(texto1)
print(texto2)

# Concatenando Strings
nome = "Chris"
saudacao = "Olá, " + nome + "!"
print(saudacao)  # Saída: Olá, Chris!

# Repetindo Strings
repeticao = "Python! " * 3
print(repeticao)  # Saída: Python! Python! Python!

# Acessando Caracteres
texto = "Python"
primeira_letra = texto[0]
ultima_letra = texto[-1]
print("Primeira letra:", primeira_letra)  # Saída: P
print("Última letra:", ultima_letra)  # Saída: n

# Fatiamento de Strings
fatiado = texto[0:3]  # Do índice 0 ao 2 (não inclui o 3)
print("Fatiado:", fatiado)  # Saída: Pyt

# Métodos Úteis
texto = "  Olá, Mundo!  "
print(texto.lower())  # Saída: "  olá, mundo!  "
print(texto.upper())  # Saída: "  OLÁ, MUNDO!  "
print(texto.strip())  # Saída: "Olá, Mundo!"
print(texto.replace("Mundo", "Python"))  # Saída: "  Olá, Python!  "
print(texto.split())  # Saída: ['Olá,', 'Mundo!']

# Interpolação de Strings
nome = "Chris"
idade = 25
mensagem = f"Meu nome é {nome} e eu tenho {idade} anos."
print(mensagem)  # Saída: Meu nome é Chris e eu tenho 25 anos.

s1 = 'Alura'
s2 = "Alura"
print(type(s1))  # Saída: <class 'str'>

texto = input('Digite seu nome: ') # digite 
texto = texto.strip().upper().replace('Y','T')
print(texto)  # Saída: "GEOVANA ALESSANDRA DIAS SANTOS"

ano_entrada = (int(input('Digite o ano de entrada: ')))
print(ano_entrada)  # Saída: 1980

nota_entrada = (float(input('Digite a nota: ')))
print(f'Ano de Entrada {ano_entrada} - nota teste de ingresso {nota_entrada}')  # Saída: 1980 - nota reste de ingresso 9.5

