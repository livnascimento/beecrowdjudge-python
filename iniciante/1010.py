total = 0

for i in range(2):
    codigo, quantidade, preco = input().split(" ")
    total += float(quantidade) * float(preco)

print("VALOR A PAGAR: R$ {:.2f}".format(total))