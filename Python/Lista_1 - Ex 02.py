'''
2.1. Crie uma variável 'A' com valor 10 e uma variável 'B' com valor 3. Realize as
seguintes operações e imprima os resultados:
Soma
Subtração
Multiplicação
Divisão
Parte inteira da divisão
Resto da divisão
Exponenciação
'''
a = 10
b = 3

sum = a + b
multiplication = a * b
division = a / b
whole_division = a // b
rest_division = a % b
exponentiation = a ** b

print(f'Soma: {a} + {b} = {sum}\nMultiplicação: {a} x {b} = {multiplication}')
print(f'Divisão: {a} / {b} = {division:.2f}\nParte Inteira da divisão: {a} // {b} = {whole_division}')
print(f'Resto da divisão: {a} % {b} = {rest_division}\nExponenciação: {a} ** {b} = {exponentiation}')

# ------ Ex 01 resolvido sem necessidade de auxilio ------ #