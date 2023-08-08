num1 = float(input('Digite um número:   '))
num2 = float(input('Digite outro número:    '))
num3 = float(input('Digite mais outro número:   '))

maior = num3
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2

menor = num3
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
print(f'O maior número é {maior} e o menor {menor}')