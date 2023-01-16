n = int(input())

for i in range(n):
    figs1, figs2 = map(int, input().split())
    resto = figs1 % figs2

    while (resto != 0):
        figs1 = figs2
        figs2 = resto
        resto = figs1 % figs2
    
    print(figs2)