salario_atual = float(input('Digite o salário atual do funcionário:R$'))

if salario_atual > 1250:
    salario_novo = salario_atual + (salario_atual * 0.10)
else:
    salario_novo = salario_atual + (salario_atual * 0.15)

print('O novo salário é de R${:.2f}'.format(salario_novo))
