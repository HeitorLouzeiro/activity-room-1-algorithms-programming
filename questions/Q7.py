'''

Entre com o ano de nascimento de uma pessoa e o ano atual, depois disso,
imprima a idade da pessoa em anos, dias e horas. Não esqueça de verificar
se o ano de nascimento é um ano valido.

'''

anoNascimento = int(input('Digite o ano de nascimento: '))
anoAtual = int(input('Digite o ano atual: '))

if anoNascimento > anoAtual:
    print('Ano de nascimento invalido')
else:
    idade = anoAtual - anoNascimento
    dias = idade * 365
    horas = dias * 24
    print('Idade em anos: %d' % idade)
    print('Idade em dias: %d' % dias)
    print('Idade em horas: %d' % horas)
