numero = int(input())
horasTrabalhadas = int(input())
precoHora = float(input())

salario = float(horasTrabalhadas * precoHora)

print("NUMBER = {}".format(numero))
print("SALARY = U$ {:.2f}".format(salario))