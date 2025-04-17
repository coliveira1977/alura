frase = input("Digite uma frase: ")

# Tratando a frase para remover pontuações
frase_tratada = frase.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ")

# Filtrando palavras com tamanho maior ou igual a 5
palavras_filtradas = list(filter(lambda palavra: len(palavra) >= 5, frase_tratada.split()))

# Exibindo o resultado
print(f"Palavras com 5 ou mais caracteres: {palavras_filtradas}")