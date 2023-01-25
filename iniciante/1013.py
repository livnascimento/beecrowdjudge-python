a , b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)

maiorAB = (a+b+abs(a-b)) / 2

if (maiorAB > c):
    maior = maiorAB
elif(maiorAB < c):
    maior = c

print("{} eh o maior".format(int(maior))) 