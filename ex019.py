import random
n1 = str(input('Primeiro aluno:\n'))
n2 = str(input('Segundo aluno:\n'))
n3 = str(input('Terceiro aluno:\n'))
n4 = str(input('Quarto aluno:\n'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolido foi: {}'.format(escolhido))