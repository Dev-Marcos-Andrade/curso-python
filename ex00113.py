def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('por favor, digite um número real válido.')
            continue
        except (KeyboardInterrupt):
            print('O usuário preferio não digitar esse número.')
            return 0
        else:
            return n


num = leiaInt('Digite um valor:')
print(f'O valor digitado foi {num}')