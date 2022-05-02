'''nome = str(input('Digite seu nome completo:')).strip().lower().split()
print('Primeiro nome: {}'.format(nome[0]))
print('Segundo nome: {}'.format(nome[len(nome)-1]))'''

n = str(input('Digite seu nome completo:')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'. format(nome[0]))
print('Seu segundo nome é {}'.format(nome[len(nome)-1]))

