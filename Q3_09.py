# dia = 24 horas 
# 1 hora = 60 minutos
# 1 minuto = 60 segundos

dias = int(input('Digite a quantidade de dias:  '))
horas = int(input('Digite a quantidade de horas:    '))
minutos = int(input('Digite a quantidade de minutos:    '))
segundos = int(input('Digite a quantidade de segundos:  '))

dias = dias * 24 * 60 * 60
horas = horas * 60 * 60
minutos = minutos * 60

t_segundos = segundos + dias + horas + minutos
print(f'O total em segundos é igual a {t_segundos}')
