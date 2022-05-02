from time import sleep
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro numero: '))
o = 0
while o != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    o = int(input('Qual a sua opção: '))
    if o == 1:
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1, n2, soma))
    elif o == 2:
        m = n1 * n2
        print('A multiplicação de {} e {} é {}'.format(n1, n2, m))
    elif o == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} é {} o maior é {}'.format(n1, n2, maior))
    elif o == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif o == 5:
        sleep(1)
        print('FINALIZANDO...')
print('Fim do programa!')
