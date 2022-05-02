from datetime import date
atual = date.today().year
aduto = 0
criança = 0
for i in range(7):
    n = int(input('Digite o ano de nascimento: '))
    if atual - n >= 21:
        aduto += 1
    elif atual - n < 21:
        criança += 1
print('Ao todo tivemos {} adutos e {} crianças '.format(aduto, criança))
