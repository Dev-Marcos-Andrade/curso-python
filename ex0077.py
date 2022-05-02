palavras = ('celular', 'flamengo', 'python',
            'curso', 'casa', 'camarão', 'peixe',
            'tanque', 'fazenda', 'rio', 'gado', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p} temos ',end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
