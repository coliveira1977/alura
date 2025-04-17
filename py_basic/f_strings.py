# Interpolação de Variáveis
nome = "Chris"
idade = 25
print(f"Meu nome é {nome} e eu tenho {idade} anos.")  # Saída: Meu nome é Chris e eu tenho 25 anos.

# Expressões Dentro de f-strings
a = 5
b = 3
print(f"A soma de {a} e {b} é {a + b}.")  # Saída: A soma de 5 e 3 é 8.

# Formatando Números
valor = 1234.56789
print(f"Valor formatado com 2 casas decimais: {valor:.2f}")  # Saída: 1234.57
print(f"Valor com separador de milhar: {valor:,.2f}")  # Saída: 1,234.57

# Alinhamento de Texto
texto = "Python"
print(f"|{texto:<10}|")  # Alinhado à esquerda
print(f"|{texto:>10}|")  # Alinhado à direita
print(f"|{texto:^10}|")  # Centralizado

# Representações Especiais
numero = 255
print(f"Hexadecimal: {numero:#x}")  # Saída: 0xff
print(f"Binário: {numero:#b}")      # Saída: 0b11111111
print(f"Octal: {numero:#o}")        # Saída: 0o377

# Chamando Funções Dentro de f-strings
nome = "chris"
print(f"Nome em maiúsculas: {nome.upper()}")  # Saída: CHRIS

# Usando f-strings com Dicionários
dados = {"nome": "Chris", "idade": 25}
print(f"Meu nome é {dados['nome']} e eu tenho {dados['idade']} anos.")  # Saída: Meu nome é Chris e eu tenho 25 anos.

# f-strings com Objetos
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa = Pessoa("Chris", 25)
print(f"Meu nome é {pessoa.nome} e eu tenho {pessoa.idade} anos.")  # Saída: Meu nome é Chris e eu tenho 25 anos.

# Escapando de Chaves
print(f"Usando chaves literais: {{texto}}")  # Saída: {texto}


nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45

print('Nome do aluno é %s, ele tem %d anos e sua média é %f.' %(nome_aluno, idade_aluno, media_aluno))

print('Nome do aluno é %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno, idade_aluno, media_aluno))

x = True
print("Valor de x: %s" % str(x))

nome_aluno = 'Fabricio Daniel'

print('Nome do aluno: {}'.format(nome_aluno))

nome_aluno = 'Fabricio Daniel'
idade_aluno = 15
media_aluno = 8.45

print('Nome do aluno é {}, ele tem {} anos e sua média é {}.' .format(nome_aluno, idade_aluno, media_aluno))


print("Estudar é um esforço constante,\nÉ como cultivar uma planta,\nPrecisamos de dedicação e paciência,\nPara ver o fruto amadurecer.")

print('Quantidade\tQualidade\n5 amostras\tAlta\n3 amostras\tBaixa')


print("Caminho do arquivo: C:\\arquivos\\documento.csv")

print("Ouvi uma vez \"Os frutos do conhecimento são os mais doces e duradouros de todos.\"")

print('Minha professora uma vez disse \'Estudar é a chave do sucesso.\' ')
