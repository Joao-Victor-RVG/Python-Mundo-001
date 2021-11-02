salario1 = float(input('Qual é o salario de um funcionario? R$'))
salario2 = salario1 + (salario1 * 15 / 100) 
print(' O salario desse funcionario era de {:.2f} e  após o reajuste de 15% vai ser do valor de {:.2f} reais'.format(salario1, salario2))
