largura = float(input('Digite a largura da parede: '))
altura = float(input('Digiite a altura da parede: '))
area = largura * altura
tinta = area / 2

print('Area a ser pintada:{}m²'.format(area))
print('Litros de tinta necessários para pintar a parede:{}l'.format(tinta))
