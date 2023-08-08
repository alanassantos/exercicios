cigarro = int(input('Digite a quantidade cigarros fumados por dia:  '))
anos = int(input('Digite a quantidade de anos que já fumou: '))
minutos = cigarro * 10 * anos * 365

"""1 h -> 60 minutos 
   x h -> 1 m
   60x -> 1
   x   -> 1 / 60

24 h   -> 1 d 
1 / 60 -> x 
24 x   -> 1 / 60
x      -> 1 / 24 * 60"""

reducao = minutos / (24 * 60)

print(f'Uma pessoa que fuma {cigarro} por dia, durante {anos}anos. Terá a redução do tempo de vidas em um total de {reducao:.2f} dias')