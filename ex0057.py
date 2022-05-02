'''masculino = 'M'
feminino = 'F'
sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informe seu sexo [M/F]: ')).upper()
    if sexo != 'M' and sexo != 'F':
        print('Digite certo, preste atenção no serviço...')
feminino = 'F'
masculino = 'M'
if sexo == 'M':
    print('A pessoa é do sexo masculino. ')
else:
    print('A pessoa é do sexo feminono. ')'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, Informe seu sexo: '))
print('Sexo {} registrado com sucesso'.format(sexo))
