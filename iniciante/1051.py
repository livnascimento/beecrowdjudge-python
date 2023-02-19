renda = float(input())
imposto = 0

if (renda <= 2000):
    print("Isento")
else:
    renda -= 2000   #2520
    if (renda <= 1000):
        imposto += renda * (8 / 100)
    else:
        imposto += 1000 * (8 / 100)
        renda -= 1000   #1520
        if (renda <= 1500):
            imposto += renda * (18 / 100)
        else:
            imposto += 1500 * (18 / 100)
            renda -= 1500   #20
            if (renda > 0):
                imposto += renda * (28 / 100)
    print("R$ {:.2f}".format(imposto))