nome = str(input('Qual é o seu nome ??:\n')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é {} '.format(nome.upper()))
print('Seu nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count('  ')))
print('Seu primeiro nome tem {} letras'.format(nome.find('  ')))
