velocidade = int(input('Digite a velocidade do seu carro: '))
multa = (velocidade - 80) * 7.0

if velocidade <= 80:
    print('Tenha um bom dia! Dirija com cuidado!')
else:
    print('Você ultrapassou o limite de velocidade de 80km/h! sua multa foi de R${:.2F}'.format(multa))