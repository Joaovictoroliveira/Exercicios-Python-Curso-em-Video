dias = float(input('Quantidade de dias: '))
km_percorridos = float(input('Quantidade de Km percorridos: '))
aluguel = (dias * 60) + (km_percorridos * 0.15)

print('Com {} dias e {}km percorridos, o total do aluguel é R${:.2f}'.format(dias, km_percorridos, aluguel))
