from datetime import date

ano_nascimento = int(input('Digite o ano de seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
tempo_que_passou = idade - 18
tempo_que_falta = 18 - idade

print('Seu ano de nascimento é {} e você tem {} anos'.format(ano_nascimento, idade))

if idade == 18:
    print('Você tem que se alistar esse ano!!')
elif idade > 18:
    print('Com {} anos você deveria ter se alistado a {} anos!!'.format(idade, tempo_que_passou)) 
    ano_alistamento = ano_atual - tempo_que_passou
    print('Em {} você deveria ter se alistado!!'.format(ano_alistamento))
else:
    print('Com {} anos faltam {} anos para você se alistar!!'.format(idade, tempo_que_falta))
    ano_alistamento = ano_atual + tempo_que_falta
    print('em {} será seu alistamento!!'.format(ano_alistamento))
