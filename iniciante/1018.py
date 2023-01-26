total = int(input())

print("{}".format(total))

notas100 = int(total / 100)
total -= notas100 * 100

notas50 = int(total / 50)
total -= notas50 * 50

notas20 = int(total / 20)
total -= notas20 * 20

notas10 = int(total / 10)
total -= notas10 * 10

notas5 = int(total / 5)
total -= notas5 * 5

notas2 = int(total / 2)
total -= notas2 * 2

notas1 = int(total)

print("{} nota(s) de R$ 100,00".format(notas100))
print("{} nota(s) de R$ 50,00".format(notas50))
print("{} nota(s) de R$ 20,00".format(notas20))
print("{} nota(s) de R$ 10,00".format(notas10))
print("{} nota(s) de R$ 5,00".format(notas5))
print("{} nota(s) de R$ 2,00".format(notas2))
print("{} nota(s) de R$ 1,00".format(notas1))