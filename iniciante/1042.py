a, b, c = input().split(" ")
a, b, c = int(a), int(b), int(c)

numerosOrdenados = [a,b,c]
numerosOrdenados.sort()

for i in range(3):
    print("{}".format(numerosOrdenados[i]))
print("")
print("{}".format(a))
print("{}".format(b))
print("{}".format(c))