'''
1.1. Crie variáveis para armazenar o nome, idade, peso e altura de uma pessoa.
Imprima os valores e os tipos de dados dessas variáveis.
'''

name_usr = input('Insira seu nome: ')
age_usr = int(input('Insira sua idade: '))
weight_usr = float(input('Insira seu peso: '))
height_usr = float(input('Insira sua altura: '))
imc = float(weight_usr / height_usr**2)

print(f'------------\nOlá {name_usr.capitalize()}, tudo bem?\nVocê tem {age_usr} anos!')
print(f'Seu peso atual é {weight_usr}Kg\nSua altura é {height_usr:.2f}m\n------------')
print(f'Com isso, podemos calcular seu IMC:\nSeu IMC atual é {imc:.2f}\n------------')
print(f'Tipo de dados do nome: {type(name_usr)}\nTipo de dados da idade: {type(age_usr)}')
print(f'Tipo de dados do peso: {type(weight_usr)}\nTipo de dados da altura: {type(height_usr)}')

# ------ Ex 1.1 resolvido sem necessidade de auxilio ------ #