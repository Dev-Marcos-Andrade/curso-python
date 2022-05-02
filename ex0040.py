n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('A nota {} e a nota {} é igual a Média {:.1f}'.format(n1, n2, media))
if media < 5.0:
    print('O aluno foi REPROVADO!!!')
elif media == 5.0 and 6.9:
    print('O aluno esta em RECUPERAÇÃO!!!')
elif media >= 7.0:
    print('O aluno foi APROVADO!!!')

