real = float(input('Quanto dinheiro você tem na carteira?? r$'))
dolar = real / 5.42
euro = real / 6.62
libra = real / 7.34
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar EUR€{:.2f}'.format(real, euro))
print('Com R${:.2f} você pode comprar GBP£{:.2f}'.format(real, libra))