# Condicionais
'''
9.1. Peça ao usuário para digitar sua idade e verifique se ele é menor de idade,
 adulto ou idoso. Imprima uma mensagem correspondente.
'''
age = int(input('Digite a sua idade: '))

if age < 18:
    print('Você é menor de idade!')

elif age >= 18 and age < 65 :
    print('Você é maior de idade!')

else:
    print('Você é idoso!')

# ------ Ex 9.1 resolvido sem necessidade de auxilio ------ #