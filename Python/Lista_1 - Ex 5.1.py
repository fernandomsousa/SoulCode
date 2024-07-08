'''
5.1. Peça ao usuário para digitar um e-mail e verifique se o e-mail contém o
caractere '@'. Imprima uma mensagem indicando se é um e-mail válido ou não.
'''

email = input('Digite seu email: ')

if '@' in email:
    print('Email válido ^-^')
else:
    print('Email inválido! Digite novamente.')

# ------ Ex 5.1 resolvido sem necessidade de auxilio ------ #