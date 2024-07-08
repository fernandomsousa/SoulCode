'''
5.2. Peça ao usuário para digitar uma frase e:
Converta a frase para maiúsculas.
Converta a frase para minúsculas.
Converta a primeira letra de cada palavra para maiúscula.
Verifique se a frase começa com uma determinada palavra (ex.: 'Olá').
'''

phrase = input('Digite uma frase qualquer: ').capitalize()

if phrase.startswith('Olá'): # Função de "Começa com"
    print(f'Frase toda em letras maiúsculas: {phrase.upper()}')
    print(f'Frase toda em letras minúsculas: {phrase.lower()}')
    print(f'Frase com a primeira letra de cada palvara em maiúscula: {phrase.title()}')
    print('A frase começa com Olá!')
else:
    print(f'Frase toda em letras maiúsculas: {phrase.upper()}')
    print(f'Frase toda em letras minúsculas: {phrase.lower()}')
    print(f'Frase com a primeira letra de cada palvara em maiúscula: {phrase.title()}')
    print('A frase não começa com Olá!')

# ------ Ex 5.2 resolvido sem necessidade de auxilio ------ #