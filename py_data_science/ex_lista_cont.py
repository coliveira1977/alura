# Aquecimento

# 1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:
# lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]
lista_de_listas = [[4, 6, 5, 9], [1, 0, 7, 2], [3, 4, 1, 8]]
somas = [sum(lista) for lista in lista_de_listas]
print("Somas:", somas)

# 2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:
# lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
terceiros = [tupla[2] for tupla in lista_de_tuplas]
print("Terceiros elementos:", terceiros)

# 3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.
lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
tuplas = [(i, nome) for i, nome in enumerate(lista)]
print("Lista de tuplas:", tuplas)

# 4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:
# aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]
valores_apartamento = [valor for tipo, valor in aluguel if tipo == 'Apartamento']
print("Valores de Apartamentos:", valores_apartamento)

# 5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista meses e os valores estão em despesa.
# meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
# despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]
despesas_dict = {mes: valor for mes, valor in zip(meses, despesa)}
print("Dicionário de despesas:", despesas_dict)

# Aplicando a projetos

# 6. Filtrar somente os dados do ano 2022 com venda maior do que 6000.
# vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
vendas_filtradas = [venda for ano, venda in vendas if ano == '2022' and venda > 6000]
print("Vendas filtradas:", vendas_filtradas)

# 7. Criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia.
# glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]
glicemia_rotulada = [(valor, 'Hipoglicemia' if valor <= 70 else 'Normal' if valor <= 99 else 'Alterada' if valor <= 125 else 'Diabetes') for valor in glicemia]
print("Glicemia rotulada:", glicemia_rotulada)

# 8. Criar uma lista de tuplas com id, quantidade, preço e valor total.
# id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
# preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]
tabela = [('id', 'quantidade', 'preco', 'total')] + [(id[i], quantidade[i], preco[i], quantidade[i] * preco[i]) for i in range(len(id))]
print("Tabela de vendas:", tabela)

# 9. Criar um dicionário com a contagem de filiais em cada Estado.
# estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
estados = ['SP', 'ES', 'MG', 'MG', 'SP', 'MG', 'ES', 'ES', 'ES', 'SP', 'SP', 'MG', 'ES', 'SP', 'RJ', 'MG', 'RJ', 'SP', 'MG', 'SP', 'ES', 'SP', 'MG']
contagem_filiais = {estado: estados.count(estado) for estado in set(estados)}
print("Contagem de filiais:", contagem_filiais)

# 10. Criar dois dicionários: um com listas de colaboradores por Estado e outro com a soma de colaboradores por Estado.
# funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES',9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG',8), ('ES',8), ('SP',9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
funcionarios = [('SP', 16), ('ES', 8), ('MG', 9), ('MG', 6), ('SP', 10), ('MG', 4), ('ES', 9), ('ES', 7), ('ES', 12), ('SP', 7), ('SP', 11), ('MG', 8), ('ES', 8), ('SP', 9), ('RJ', 13), ('MG', 5), ('RJ', 9), ('SP', 12), ('MG', 10), ('SP', 7), ('ES', 14), ('SP', 10), ('MG', 12)]
colaboradores_por_estado = {estado: [colaborador[1] for colaborador in funcionarios if colaborador[0] == estado] for estado in set(estado for estado, _ in funcionarios)}
soma_colaboradores = {estado: sum(colaboradores_por_estado[estado]) for estado in colaboradores_por_estado}
print("Colaboradores por Estado:", colaboradores_por_estado)
print("Soma de colaboradores por Estado:", soma_colaboradores)