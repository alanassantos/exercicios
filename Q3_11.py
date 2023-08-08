valor_mer = float(input('Digite o valor da mercadoria:  '))
p_desconto = float(input('Digite o percentual de desconto:  '))
preco_pagar = valor_mer - (valor_mer * p_desconto / 100)
valor_des = valor_mer * p_desconto / 100

print(f'O valor do desconto é {valor_des}, logo o valor a pagar é {preco_pagar}')
