a, b, c = input().split(" ")
a, b, c = float(a), float(b), float(c)

ordenados = [a, b, c]
ordenados.sort(reverse=True)
a, b, c = ordenados

if (a >= b + c):
    print("NAO FORMA TRIANGULO")
else:
    if (a * a == b * b + c * c):
        print("TRIANGULO RETANGULO")

    if (a * a > b * b + c * c):
        print("TRIANGULO OBTUSANGULO")

    if (a * a < b * b + c * c):
        print("TRIANGULO ACUTANGULO")

    if ( a == b and b == c):
        print("TRIANGULO EQUILATERO")

    if (a == b and a != c or b == c and b != a or c == a and c != b):
        print("TRIANGULO ISOSCELES")