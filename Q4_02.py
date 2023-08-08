velocidade = float(input('Digite a velocidade do carro:   '))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print(f'Sua velocidade ultrapassou 80km/h, a multa a pagar é de {multa}')
if velocidade <= 80:
    print(f'Sua velocidade está ok!')
    