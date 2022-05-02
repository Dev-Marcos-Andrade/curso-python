from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. tente adivinhar...')
print('-=-' *20)
jogador = int(input('Em qual número estou pensado? ')) #jogador tentado adivinhar.
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabens você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))


