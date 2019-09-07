numero = int(input('Digite um número inteiro: '))
print('Escolha a base numérica para conversão')
print('[1] para binário')
print('[2] para octadecimal')
print('[3] para hexadecimal')
opcao = int(input('sua opcao: '))

if opcao == 1:
    print('O número {} convertido para binário é {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('O número {} convertido para octadecimal é {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('O número {} convertido para hexadecimal é {}'.format(numero, hex(numero)))
else:
    print('Opcão inválida!!')
