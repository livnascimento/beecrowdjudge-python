a, b = input().split(" ")
a, b = int(a), int(b)

if ( a > b):
    maior = a
    menor = b
else:
    maior = b
    menor = a

if (maior % menor == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")