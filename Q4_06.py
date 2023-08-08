distancia = float(input('Digite a distância que deseja pecorrer:    '))

if distancia <= 200:
    passagem = distancia * 0.50

else:
    passagem = distancia * 0.45

print(f'Ovalor da passagem para a distância pecorrida será de {passagem}')