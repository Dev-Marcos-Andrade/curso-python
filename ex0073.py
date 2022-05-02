time = ('corinthians','bragantino','atlético-mg',
        'santos','coritiba','cuiabá','internacional',
        'avaí','améroca-mg','palmeiras','flamengo',
        'botafogo','são paulo','fluminense','ceará sc',
        'atlético-pr','goiás','juventude','fortaleza')
print('-='*15)
print(f'Lista de time: {time}')
print('-='*15)
print(f'Os 5 primeiros são {time[0:5]}')
print('-='*15)
print(f'Os 4 últimos são {time[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(time)}')
print('-='*15)
print(f'O Flamengo está na {time.index("flamengo")}')
