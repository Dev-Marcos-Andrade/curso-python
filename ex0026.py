'''frase = str(input('Digite uma frase: ')).strip().lower()
print('A quantidade de vezes que a letra a aparece é: {}'.format(frase.count('a')))
print('Em qual posição ela aparece a primeira vez: {}'.format(frase.find('a')+1))
print('Em qual posição ela aparece pela ultima vez: {}'.format(frase.rfind('a')+1))'''

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra a aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra a apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima posição da letra a {}'.format(frase.rfind('A')+1))
