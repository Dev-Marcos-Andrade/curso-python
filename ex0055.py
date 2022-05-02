maior = 0
menor = 1000
for c in range(0, 5):
    peso = float(input('Informe o seu peso: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso foi {}kg e o menor peso foi {}kg'.format(maior, menor))