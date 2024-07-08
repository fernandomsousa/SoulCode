'''
Contexto:
Uma empresa precisa registrar informações sobre seus clientes e calcular o IMC
(Índice de Massa Corporal) de cada um deles. As informações devem ser
armazenadas em um dicionário e exibidas ao final.
'''


'''
Requisitos:
Peça ao usuário para inserir os seguintes dados de um cliente:
Nome
Idade
Peso (em kg)
Altura (em metros)
E-mail
Armazene essas informações em um dicionário.
Calcule o IMC do cliente (IMC = Peso / (Altura * Altura)) e adicione esse valor ao dicionário.
Exiba todas as informações do cliente, incluindo o IMC arredondado para duas casas decimais.

'''

name_usr = input('Digite seu nome: ').title()
age_usr = int(input('Digite sua idade: '))
weight_usr = float(input('Digite seu peso em Kg: '))
height_usr = float(input('Digite sua altura em m: '))
email = input('Digite seu email: ')
imc = weight_usr / (height_usr * height_usr)

if '@' in email:
    client = {'nome': name_usr, 'idade': age_usr, 'peso': weight_usr, 'altura': height_usr, 'email': email, 'imc': imc}
    print('\nINFORMAÇÕES DO CLIENTE:\n')
    print(f"Nome do cliente: {client['nome']}.\nIdade do cliente: {client['idade']} anos.\nPeso do cliente: {client['peso']} Kg")
    print(f"Altura do cliente: {client['altura']}m\nEmail do cliente: {client['email']}\nIMC do cliente: {client['imc']:.2f}")

else:
    print('Digite um e-mail válido!')


# ------ Estudo de caso 01 resolvido sem necessidade de auxilio ------ #

# https://colab.research.google.com/drive/1rwTIr9bSIDjezjyPCzVyKplh1hCmoErX?usp=sharing&authuser=0 colab das tarefas.