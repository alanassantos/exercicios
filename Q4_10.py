quantidade = float(input('Digite a quantidade de kwh consumido:     '))
print('Digite seu tipo de instalação')
instalacao = input(" R - para resiências \n I - para indústrias \n C - para comércios:   ")

if instalacao == 'R' or 'r':
    if quantidade <= 500:
        preco = 0.40 * quantidade
    else: 
        preco = 0.65 * quantidade
elif instalacao == 'C' or 'r':
    if quantidade <= 1000:
        preco = 0.55 * quantidade
    else:
        preco = 0.60 * quantidade
elif instalacao == 'I' or 'i':
    if quantidade <= 5000:
        preco = 0.55 * quantidade
    else:
        preco = 0.60 * quantidade
else:
    print('Digite uma opção válida')
    preco = 0

print(f'O valor a pagar é R$ {preco:.2f}')
