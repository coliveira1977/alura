# Aula: Dicionários em Python

# Introdução aos Dicionários
# Os dicionários são uma estrutura de dados em Python que armazenam pares de chave-valor.
# Eles são mutáveis, não ordenados (em versões anteriores ao Python 3.7) e permitem acesso rápido aos valores por meio das chaves.

# Criando dicionários
print("Criando dicionários:")
dicionario_vazio = {}  # Dicionário vazio
dicionario_pessoa = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}  # Dicionário com dados
dicionario_misto = {1: "um", "dois": 2, 3.0: [1, 2, 3]}  # Dicionário com diferentes tipos de chave e valor

print("Dicionário vazio:", dicionario_vazio)
print("Dicionário de pessoa:", dicionario_pessoa)
print("Dicionário misto:", dicionario_misto)

# Acessando valores em um dicionário
print("\nAcessando valores em um dicionário:")
print("Nome:", dicionario_pessoa["nome"])  # Acessa o valor associado à chave "nome"
print("Idade:", dicionario_pessoa["idade"])  # Acessa o valor associado à chave "idade"

# Usando o método get para acessar valores
print("\nUsando o método get:")
print("Cidade:", dicionario_pessoa.get("cidade"))  # Retorna o valor associado à chave "cidade"
print("País (chave inexistente):", dicionario_pessoa.get("país", "Chave não encontrada"))  # Retorna um valor padrão

# Adicionando e modificando valores
print("\nAdicionando e modificando valores:")
dicionario_pessoa["profissao"] = "Engenheira"  # Adiciona uma nova chave-valor
print("Dicionário após adicionar profissão:", dicionario_pessoa)

dicionario_pessoa["idade"] = 26  # Modifica o valor associado à chave "idade"
print("Dicionário após modificar idade:", dicionario_pessoa)

# Removendo itens de um dicionário
print("\nRemovendo itens de um dicionário:")
dicionario_pessoa.pop("cidade")  # Remove a chave "cidade" e seu valor
print("Dicionário após remover cidade:", dicionario_pessoa)

# Usando del para remover uma chave
del dicionario_pessoa["profissao"]
print("Dicionário após remover profissão:", dicionario_pessoa)

# Iterando sobre um dicionário
print("\nIterando sobre um dicionário:")
for chave, valor in dicionario_pessoa.items():
    print(f"Chave: {chave}, Valor: {valor}")

# Verificando a existência de uma chave
print("\nVerificando a existência de uma chave:")
print("A chave 'nome' está no dicionário?", "nome" in dicionario_pessoa)
print("A chave 'cidade' está no dicionário?", "cidade" in dicionario_pessoa)

# Métodos úteis para dicionários
print("\nMétodos úteis para dicionários:")
print("Chaves do dicionário:", dicionario_pessoa.keys())  # Retorna as chaves
print("Valores do dicionário:", dicionario_pessoa.values())  # Retorna os valores
print("Itens do dicionário:", dicionario_pessoa.items())  # Retorna os pares chave-valor

# Copiando um dicionário
print("\nCopiando um dicionário:")
copia_dicionario = dicionario_pessoa.copy()  # Cria uma cópia do dicionário
print("Cópia do dicionário:", copia_dicionario)

# Limpando um dicionário
print("\nLimpando um dicionário:")
dicionario_pessoa.clear()  # Remove todos os itens do dicionário
print("Dicionário após limpar:", dicionario_pessoa)

# Conclusão
# Os dicionários são uma estrutura de dados poderosa e flexível em Python.
# Eles permitem armazenar e acessar dados de forma eficiente usando pares de chave-valor.

loja = {'nomes': ['televisão', 'celular', 'notebook', 'geladeira', 'fogão'],
        'precos': [2000, 1500, 3500, 4000, 1500]}

for chave, elementos in loja.items():
  print(f'Chave: {chave}\nElementos:')
  for dado in elementos:
    print(dado)



# Dados da loja - FORMATO TABELA
loja = {
    'nomes': ['televisão', 'celular', 'notebook', 'geladeira', 'fogão'],
    'precos': [2000, 1500, 3500, 4000, 1500]
}

# Exibindo os dados no formato de tabela
print(f"{'Produto':<15} {'Preço (R$)':>10}")
print("-" * 26)

for nome, preco in zip(loja['nomes'], loja['precos']):
    print(f"{nome:<15} {preco:>10}")