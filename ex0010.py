real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.73
euro = real / 5.10
print('Com R${:.2f} Você pode compra US${:.2f} e EUR${:.2f}' .format(real, dolar,euro))