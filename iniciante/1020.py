idadeDias = int(input())

anos = int(idadeDias / 365)
idadeDias -= anos * 365

meses = int(idadeDias / 30)
idadeDias -= meses * 30

dias = idadeDias

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))