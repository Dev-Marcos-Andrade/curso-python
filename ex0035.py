'''a = float(input('Informe o comprimento da primeira reta: '))
b = float(input('Da segunda reta: '))
c = float(input('Terceira reta: '))
if b-c < a < b+c and a-c < b < a+c and a-b < c < a+b:
    print('É possivel fazer um triangulo com essas retas.')
else:
    print('Não é possilvel fazer um triangulo com essas retas.')'''
print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima Podem Forma triângulo!')
else:
    print('Os segmentos acima NÃO PODEM forma um triângulo!')

