salario = float(input('Digite seu salário:  '))
porcentagem = float(input('Digite a porcentegem do aumento'))
novo_salario = salario + (salario * porcentagem / 100)
aumento = salario * porcentagem / 100

print(f'O valor do aumento foi {aumento}, logo o novo salário é igual a {novo_salario}')