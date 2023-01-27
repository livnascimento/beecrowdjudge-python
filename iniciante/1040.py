n1, n2, n3, n4 = input().split(" ")
n1, n2, n3, n4 = float(n1), float(n2), float(n3), float(n4)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

print("Media: {:.1f}".format(media))

if (media >= 7.0):
    print("Aluno aprovado.")
    exit()
elif (media < 5.0):
    print("Aluno reprovado.")
    exit()
elif (media >= 5.0 and media <= 6.9):
    print("Aluno em exame.")
    n5 = float(input())
    print("Nota do exame: {:.1f}".format(n5))
    media = (media + n5) / 2
    if (media >= 5.0):
        print("Aluno aprovado.")
    elif(media < 5.0):
        print("Aluno reprovado")
    print("Media final: {:.1f}".format(media))