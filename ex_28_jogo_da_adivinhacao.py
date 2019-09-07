import random
valor = random.randint(0, 5) # gera um numero aleatório entre 0 e 5

num = int(input('Digite um numero entre 0 e 5: '))
if num == valor:
    print('Você acertou! Parabéns!')
else:
    print('Você errou!! Que pena!!')
    