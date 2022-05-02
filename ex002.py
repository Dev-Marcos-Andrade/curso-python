n1 = int(input('um valor:'))
n2 = int(input('outro valor:'))
s = n1 + n2
n = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n o produto é {}\n E a divisão é {:.2f}\n'.format(s,n,d), end=' ')
print('divisão inteira {}, e potensia {}'.format(di,e))
