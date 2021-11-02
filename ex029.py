velocidade = float(input('Qual é a velocidade de um carro?'))
if velocidade >= 80:
    print('Você foi MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80) * 7
    print('Você deve pagar uma multa no valor de {:.2f}!'.format(multa))
print('Bom dia!, dirija com segurança!')
    
