# velocidade media = diastancia pecorrida / tempo
# tempo = distancia / velocidade

distancia = float(input('Digite a distância que irá pecorrer em km: '))
velocidade = float(input('Digite a velocidade média esperada para viagem em km/h:   '))

tempo = distancia / velocidade

print(f'Para uma viagem com distância de {distancia}km, em uma velocidade média de {velocidade}km/h, o tempo esperado é de {tempo}h')