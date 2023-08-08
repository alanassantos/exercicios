valor_casa = float(input('Digite o valor da casa que deseja comprar:    '))
salario = float(input('Digite seu salário:  '))
anos = int(input('Digite a quantidade de anos a pagar:  '))
meses = anos * 12
prestacao = valor_casa / meses

if prestacao > salario * 0.3:
    print('Inflizmente você não pode obter um empréstimo')
else:
    print(f'O valor da sua prestação será de R$ {prestacao:.2f}')