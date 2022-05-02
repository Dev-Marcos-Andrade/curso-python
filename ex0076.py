listagem = ('celular', 1500,
            'capinha', 30.00,
            'pelicula', 20.00,
            'fone', 200.00,
            'carregador', 250.00,
           'computador', 2500,
            'mause', 300.00,
            'teclado', 150.00,
            'monitor', 500.00)
print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)
