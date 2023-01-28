horaInicial, horaFinal = input().split(" ")
horaInicial, horaFinal = int(horaInicial), int(horaFinal)

if (horaInicial == horaFinal):
    duracao = 24
else:
    if (horaInicial > horaFinal):
        duracao = (24 - horaInicial) + horaFinal
    else:
        duracao = horaFinal - horaInicial

print("O JOGO DUROU {} HORA(S)".format(duracao))