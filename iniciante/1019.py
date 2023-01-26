duracaoSegundos = int(input())

horas = int(duracaoSegundos / 3600)
duracaoSegundos -= horas * 3600

minutos = int(duracaoSegundos / 60)
duracaoSegundos -= minutos * 60

segundos = duracaoSegundos

print("{}:{}:{}".format(horas, minutos, segundos))