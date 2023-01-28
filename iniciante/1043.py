a, b, c = input().split(" ")
a, b, c = float(a), float(b), float(c)

if (a + c > b and b + c > a and a + b >c):
    perimetro = a + b + c
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((a + b) * c) / 2
    print("Area = {:.1f}".format(area))