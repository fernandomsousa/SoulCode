'''
7.2. Crie uma nova tupla concatenando a tupla do exercício anterior com o e-mail
do cliente. Imprima a nova tupla.
'''
# Coloquei novamente as entradas abaixo por opção.

email = input('Digite um email: ')
info_client = ('Douglas', 47, 72, 1.72) # Mesma tupla do anterior
info_client = info_client + (email,) # Deste modo consigo concatenar a lista com o email.

if '@' in email:
    print(f'Informações do cliente: {info_client}')
else:
    print('Email inválido! Digite novamente.')

# ------ Ex 7.2 resolvido sem necessidade de auxilio ------ #
