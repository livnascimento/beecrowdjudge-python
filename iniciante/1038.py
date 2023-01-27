item, qtd = input().split(" ")
item, qtd = int(item), int(qtd)

if (item == 1):
    preco = 4.00
elif (item == 2):
    preco = 4.50
elif (item == 3):
    preco = 5.00
elif (item == 4):
    preco = 2.00
elif (item == 5):
    preco = 1.50

total = qtd * preco
print("Total: R$ {:.2f}".format(total))