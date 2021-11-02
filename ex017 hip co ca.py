import math 
co = float(input('Qual é o tamanho do cateto oposto?\n'))
ca = float(input('Qual é o tamanho do cateto adiacente?\n'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))




