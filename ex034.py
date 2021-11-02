salario = float(input('Qual é o salário do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario *15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava {:.2f} Reais agora passa a ganhar {:.2f} Reais'.format(salario, novo))
