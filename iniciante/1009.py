nome = input()
salario = float(input())
totalVendas = float(input())

salarioComBonus = salario + (totalVendas * (15 / 100))

print("TOTAL = R$ {:.2f}".format(salarioComBonus))