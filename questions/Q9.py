'''

Faça um progama que receba 3 numeros e imprima
eles de forma decrescente e crescente

'''
# Descendente
num1 = 35
num2 = 20
num3 = 10

# Crescente
# num1 = 10
# num2 = 20
# num3 = 35


if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(num1, num2, num3)
    else:
        print(num1, num3, num2)
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
elif num3 > num1 and num3 > num2:
    if num1 > num2:
        print(num3, num1, num2)
    else:
        print(num3, num2, num1)
else:
    print('Os numeros sao iguais')
