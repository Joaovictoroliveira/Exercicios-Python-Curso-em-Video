nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 7 and media <=10:
    print('Com média de {:.1f} o aluno esta Aprovado!!'.format(media))
elif media >= 5:
    print('Com média de {:.1f} o aluno esta em recuperção!!'.format(media))
else:
    print('Com média de {:.1f} o aluno esta reprovado!!'.format(media))
