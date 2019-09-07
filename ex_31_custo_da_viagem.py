distancia = float(input('Digite a distância da sua viagem: '))

if distancia <= 200:
    valor_viagem = distancia * 0.50
else:
    valor_viagem = distancia * 0.45

print('A sua viagem vai ser de {}km'.format(distancia))
print('Custará R${:.2f}'.format(valor_viagem))