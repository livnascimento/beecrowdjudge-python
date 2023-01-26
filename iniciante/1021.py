notas = [100, 50, 20, 10, 5, 2]
moedas = [1.0, 0.5, 0.25, 0.1, 0.05, 0.01]

total = float(input())

print("NOTAS:")
for nota in notas:
    quantidade = int(total / nota)
    print("{} nota(s) de R$ {}.00".format(quantidade, nota))
    total -= quantidade * nota

print("MOEDAS:")
for moeda in moedas:
    total = round(total, 3)
    quantidade = int(total / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(quantidade, moeda))
    total -= quantidade * moeda