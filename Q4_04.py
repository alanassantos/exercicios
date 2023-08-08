salario = float(input('Digite o seu salário:    '))

if salario <= 1250:
    aumento = salario * 15 / 100

if salario > 1250:
    aumento = salario * 10 / 100

print(f'Seu amento será de {aumento}')