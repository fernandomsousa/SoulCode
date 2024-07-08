'''
6.2. Adicione um novo nome à lista de amigos e remova o primeiro nome.
Imprima a lista atualizada.
'''

friends = ['Manuela', 'Fernando', 'Douglas', 'Rafael', 'Maria']

print(f'Lista antiga: {friends}')

friends.append(input('Digite um nome para a lista: ')) 
friends.pop(0)

print(f'Lista atualizada: {friends}')

# ------ Ex 6.2 resolvido sem necessidade de auxilio ------ #