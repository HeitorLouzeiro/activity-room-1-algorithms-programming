'''

A prefeitura municipal de Corrente-PI, abriu uma linha de credito para os
funcionarios estatutarios. O valor maximo da prestacao nao poderá ultrapassar
30% do salario bruto. Fazer um programa que permita entrar com o salario bruto
e o valor da prestacao, e informar se o emprestimo pode ou nao ser concedido.

'''
salario = float(input('Digite o salario: '))
prestacao = float(input('Digite o valor da prestacao: '))

limitePrestacao = salario * 0.3

if prestacao <= limitePrestacao:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo não pode ser concedido')
