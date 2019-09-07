valor = float(input('Quanto você tem em carteira? R$'))
dolar = valor / 3.78
euro = valor / 4.21

print('Com R${}'.format(valor))
print('Você tem U${:.2f}'.format(dolar))
print('Você tem €{:.2f}'.format(euro))