salario = float(input())
aumento = 0

if (salario > 0 and salario <= 400):
    aumento = 15/100
elif (salario > 400 and salario <= 800):
    aumento = 12/100
elif (salario > 800 and salario <= 1200):
    aumento = 10/100
elif (salario > 1200 and salario <= 2000):
    aumento = 7/100
elif (salario > 2000):
    aumento = 4/100

novoSalario = salario + (salario * aumento)
reajuste = salario * aumento
percentual = int(aumento * 100)

print("Novo salario: {:.2f}".format(novoSalario))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {} %".format(percentual))