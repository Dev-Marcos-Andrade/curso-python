num = list ()
par = list()
impa = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impa.append(v)
print('-=' * 30)
print(f'Lista completa é {num}')
print(f'Lista de pares é {par}')
print(f'Alista de ímpares é {impa}')


