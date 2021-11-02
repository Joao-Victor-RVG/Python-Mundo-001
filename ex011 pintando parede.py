larg = float(input('Qual é a largura da parede que você deseja pintar?'))
alt = float(input('Qual é a altura da parede que você deseja printar?'))
area = larg * alt 
print('Sua parede tem a dimensão de {}x{} e a sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2 
print('Para você pintar essa parede você vai precisar usar {} litros de tinta '.format(tinta))



