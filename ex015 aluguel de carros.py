dia = int(input('Quantos dias você alugou esse carro?'))
km = float(input('Quantos kilometros você rodou com o automovel alugado?'))
pago = (dia * 60) + (km * 0.15)
print('Então você alugou o carro durante {} dias e rodou {} km com o carro, então o seu total a pagar vai ser de {}R$'.format(dia, km, pago))