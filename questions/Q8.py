'''

entre com a sigla de um estado e imprima o uma das mensagens:
-Piauiense, Pernambucano, Cearense, Maranhense, Potiguar,
Paraibano, Baiano, Alagoano, Sergipano

'''

print('Pi- Piauiense, Pe- Pernambucano, Ce- Cearense')
print('Ma- Maranhense, Rn- Potiguar, Pb- Paraibano, Ba- Baiano, Al- Alagoano, Se- Sergipano')  # noqa
sigla = input('Digite a sigla do estado: ').lower()

if sigla == 'pi':
    print('Piauiense')
elif sigla == 'pe':
    print('Pernambucano')
elif sigla == 'ce':
    print('Cearense')
elif sigla == 'ma':
    print('Maranhense')
elif sigla == 'rn':
    print('Potiguar')
elif sigla == 'pb':
    print('Paraibano')
elif sigla == 'ba':
    print('Baiano')
elif sigla == 'al':
    print('Alagoano')
elif sigla == 'se':
    print('Sergipano')
else:
    print('Sigla invalida')
