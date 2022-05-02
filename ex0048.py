s = 0
for num in range(1, 501, 2):
        if num % 3 == 0:
            s += num
print('A soma dos múltiplos é: {}.'.format(s))
