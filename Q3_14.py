km_pecorrido = float(input('Digite a quantidade de km pecorridos:   '))
dias = float(input('Digite a quantidade de dias que o carro foi alugado:    '))
km_pecorrido = km_pecorrido * 0.15
dias = dias * 60
total = dias + km_pecorrido

print(f'A valor total a pagar é {total}')