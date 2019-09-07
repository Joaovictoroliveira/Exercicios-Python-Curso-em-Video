cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

print('Cateto oposto: {}'.format(cateto_oposto))
print('Cateto adjacente: {}'.format(cateto_adjacente))
print('Hipotenusa: {:.2f}'.format(hipotenusa))
