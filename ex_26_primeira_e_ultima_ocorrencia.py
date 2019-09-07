frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra aparece {} vezes'.format(frase.count('a')))
print('A primeira letra a apareceu na posição {}'.format(frase.find('a')))
print('A ultima letra a apareceu na posição {}'.format(frase.rfind('a')))
