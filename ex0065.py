r = 'S'
s = q = m = maior = menor = 0
while r in 'Ss':
    n = int(input('Digite um número: '))
    s += n
    q += 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
m = s / q
print('Você digitou {} números e a média foi {}'.format(q, m))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
