numero = int(input('Me diga um numero qualquer\n'))
resultado = numero % 2
print('Resultado foi {}'.format(resultado))
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))


