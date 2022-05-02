frase = str(input('Digite uma frase: ')).strip().upper()
p = frase.strip()
j = ''.join(p)
i = ''
for letra in range(len(j)-1, -1, -1):
    i += j[letra]
if i == j:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo!')
