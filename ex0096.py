def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m² ')


# Programa principal
print('Controle de Terrenos')
print('-' * 20)
l = float(input('Lagura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
