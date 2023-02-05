horaInicial, minutoInicial, horaFinal, minutoFinal = input().split(" ")
horaInicial, minutoInicial, horaFinal, minutoFinal = int(horaInicial), int(minutoInicial), int(horaFinal), int(minutoFinal)

if (horaInicial == horaFinal and minutoInicial == minutoFinal):
    horas = 24
    minutos = 0
elif (horaInicial > horaFinal):
    horas = (24 - horaInicial) + horaFinal
    if (minutoInicial > minutoFinal):
        minutos = (60 - minutoInicial) + minutoFinal
        horas -= 1
    else:
        minutos =  minutoFinal - minutoInicial
elif (horaInicial == horaFinal and minutoInicial > minutoFinal):
    horas = 23
    if (minutoInicial > minutoFinal):
        minutos = (60 - minutoInicial) + minutoFinal
    else:
        minutos =  minutoFinal - minutoInicial
else:
    horas = horaFinal - horaInicial
    if (minutoInicial > minutoFinal):
        minutos = (60 - minutoInicial) + minutoFinal
        horas -= 1
    else:
        minutos =  minutoFinal - minutoInicial

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(horas, minutos))
