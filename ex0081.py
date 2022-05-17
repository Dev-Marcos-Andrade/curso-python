valor = []
while True:
    valor.append(int(input('Digite um valor: ')))
    per = str(input('Quer continuar? [S/N] '))
    if per in 'Nn':
        break
print('-=' * 30)
print(f'Voçê digitou {len(valor)} elementos.')
valor.sort(reverse=True)
print(f'Os valores em ordem decrecente são {valor}')
if 5 in valor:
    print('O valor 5 esta na lista ')
else:
    print('O valor 5 não esta na lista ')
