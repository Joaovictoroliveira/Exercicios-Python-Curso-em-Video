valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o salario: R$'))
anos = int(input('Digite em quantos será pago o empréstimo: '))
valor_prestacao_mensal = valor_casa / (anos * 12)

print('O valor da prestação será de R${}'.format(valor_prestacao_mensal))

if valor_prestacao_mensal <= salario * 0.30:
    print('O empréstimo esta aprovado!!')
else:
    print('O empréstimo foi negado!!')
