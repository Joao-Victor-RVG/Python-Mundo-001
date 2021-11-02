a = int(input('Primeiro valor:\n'))
b = int(input('Segundo valor:\n'))
c = int(input('Terceiro Valor:\n'))
#verificando quem é o menor
menor = a
if b<10 and b<c:
    menor = b
if c<a and c<b:
    menor = c
# verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
