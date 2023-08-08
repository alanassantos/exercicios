a = float(input('Digite um número:  '))
b = float(input('Digite outro número:   '))
operacao = input('Digite a operação que deseja realizar. SOMA (+), SUBTRAÇÃO (-), MULTIPLICAÇÃO(*), DIVISÃO (/):    ')

if operacao == '+':
    conta = a + b

elif operacao == '-':
    conta = a - b

elif operacao == '*':
    conta = a * b

elif operacao == '/':
    conta = a / b

else:
    print('Digite uma opção válida!')
    conta = "Não foi possível realizar uma operação"

print(conta)
