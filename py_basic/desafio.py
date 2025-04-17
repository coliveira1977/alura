# Aquecendo na programação

# 1) Média de gastos
gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
media_gastos = sum(gastos) / len(gastos)
print(f"Média de gastos: {media_gastos:.2f}")

# 2) Compras acima de 3000 reais
acima_3000 = [gasto for gasto in gastos if gasto > 3000]
percentual_acima_3000 = (len(acima_3000) / len(gastos)) * 100
print(f"Compras acima de 3000: {len(acima_3000)} ({percentual_acima_3000:.2f}%)")

# 3) Coletar 5 números inteiros
numeros = [int(input("Digite um número inteiro: ")) for _ in range(5)]
print("Lista de números:", numeros)

# 4) Lista em ordem inversa
numeros_inverso = [int(input("Digite um número inteiro: ")) for _ in range(5)]
print("Lista em ordem inversa:", numeros_inverso[::-1])

# 5) Números primos até um número
n = int(input("Digite um número: "))
primos = [x for x in range(2, n + 1) if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))]
print("Números primos:", primos)

# 6) Validação de data
dia, mes, ano = map(int, input("Digite uma data (dd mm aaaa): ").split())
valida = (1 <= dia <= 31) and (1 <= mes <= 12) and (ano > 0)
print("Data válida" if valida else "Data inválida")

# Momento dos projetos

# 7) Percentual de crescimento de bactérias
bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
crescimento = [100 * (bacterias[i] - bacterias[i - 1]) / bacterias[i - 1] for i in range(1, len(bacterias))]
print("Percentual de crescimento diário:", crescimento)

# 8) Separar IDs doces e amargos
ids = [int(input("Digite um ID: ")) for _ in range(10)]
doces = [id for id in ids if id % 2 == 0]
amargos = [id for id in ids if id % 2 != 0]
print(f"Doces: {len(doces)}, Amargos: {len(amargos)}")

# 9) Nota do aluno
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
respostas = [input(f"Resposta da questão {i + 1}: ").upper() for i in range(10)]
nota = sum(1 for i in range(10) if respostas[i] == gabarito[i])
print(f"Nota do aluno: {nota}")

# 10) Temperaturas médias do ano
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = [float(input(f"Digite a temperatura média de {mes}: ")) for mes in meses]
media_anual = sum(temperaturas) / len(temperaturas)
acima_media = [(meses[i], temperaturas[i]) for i in range(12) if temperaturas[i] > media_anual]
print(f"Média anual: {media_anual:.2f}")
print("Meses com temperatura acima da média:")
for mes, temp in acima_media:
    print(f"{mes}: {temp:.2f}")

# 11) Total de vendas e produto mais vendido
vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
total_vendas = sum(vendas.values())
mais_vendido = max(vendas, key=vendas.get)
print(f"Total de vendas: {total_vendas}")
print(f"Produto mais vendido: {mais_vendido}")

# 12) Design vencedor e porcentagem de votos
votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}
total_votos = sum(votos.values())
vencedor = max(votos, key=votos.get)
percentual_vencedor = (votos[vencedor] / total_votos) * 100
print(f"Design vencedor: {vencedor} ({percentual_vencedor:.2f}%)")

# 13) Abono salarial
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = {salario: max(salario * 0.1, 200) for salario in salarios}
total_abonos = sum(abonos.values())
abono_minimo = sum(1 for abono in abonos.values() if abono == 200)
maior_abono = max(abonos.values())
print(f"Total de abonos: {total_abonos}")
print(f"Colaboradores com abono mínimo: {abono_minimo}")
print(f"Maior abono: {maior_abono}")

# 14) Diversidade biológica
areas = {'Área Norte': [2819, 7236], 'Área Leste': [1440, 9492], 'Área Sul': [5969, 7496], 'Área Oeste': [14446, 49688], 'Área Centro': [22558, 45148]}
media_especies = {area: sum(especies) / len(especies) for area, especies in areas.items()}
maior_diversidade = max(media_especies, key=media_especies.get)
print("Média de espécies por área:", media_especies)
print(f"Área com maior diversidade: {maior_diversidade}")

# 15) Idades dos colaboradores
setores = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65], 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64], 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56], 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
media_setores = {setor: sum(idades) / len(idades) for setor, idades in setores.items()}
media_geral = sum(sum(idades) for idades in setores.values()) / sum(len(idades) for idades in setores.values())
acima_media = sum(1 for idades in setores.values() for idade in idades if idade > media_geral)
print("Média de idade por setor:", media_setores)
print(f"Média geral: {media_geral:.2f}")
print(f"Pessoas acima da média geral: {acima_media}")