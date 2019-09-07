num =float(input('Digite a distância em metros: '))
centimetros = num * 100
milimetros = num * 1000
quilometros = num / 1000

print('{} metros'.format(num))
print('São {} quilômetros'.format(quilometros))
print('São {} centímetros'.format(centimetros))
print('São {} milímetros'.format(milimetros))