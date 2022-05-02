p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
d =  p + (10 - 1) * r
for c in range(p,d + r, r):
    f = p + r
    print(c, end='-->')
print('!!!FIM!!!')