'''

Faça um progama que leia dois numeros e realize as funçoes da calculadora,
caso o usuario digite '+' ele deve somar,'-' ele deve subtrair,
'/' realiza a divisao,'*' ele deve multiplicar.

'''

num1 = float(input('Digite um numero: '))
num2 = float(input('Digite outro numero: '))

print('(+) somar, (-) subtrair, (/) dividir, (*) multiplicar')
operacao = input('Digite a operação que deseja realizar: ')

if operacao == '+':
    resultado = num1 + num2
    print(resultado)
elif operacao == '-':
    resultado = num1 - num2
    print(resultado)
elif operacao == '/':
    resultado = num1 / num2
    print(resultado)
elif operacao == '*':
    resultado = num1 * num2
    print(resultado)
else:
    print('Operação invalida')
