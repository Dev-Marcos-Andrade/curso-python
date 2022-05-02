import math
an = float(input('Digite o ângulo que você deseja: '))
s = math.sin(math.radians(an))
c = math.cos(math.radians(an))
t = math.tan(math.radians(an))
print('O ângulo de {:.2f} tem o seno de {:.2f}'.format(an, s))
print('O ângulo de {:.2f} tem o cosseno de {:.2}'.format(an, c))
print('O ângulo de {:.2f} tem a tangente de {:.2f}'.format(an, t))
