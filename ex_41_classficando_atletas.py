from datetime import date

ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade > 25:
    print('O atleta é Master!!')
elif idade > 19 and idade <= 25:
    print('O atleta é Sênior!!')
elif idade > 14 and idade <= 19:
    print('O atleta é Junior!!')
elif idade > 9 and idade <= 14:
    print('O atleta é Infantil!!')
else:
    print('O atleta é Mirim!!')