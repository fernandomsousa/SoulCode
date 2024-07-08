'''
Contexto
Uma empresa deseja realizar uma pesquisa de opinião com cinco participantes
sobre um novo produto. As respostas devem ser armazenadas e analisadas para
verificar a satisfação dos clientes.
'''

'''
Requisitos
Peça ao usuário para inserir o nome e a opinião (satisfeito/insatisfeito) de
cinco participantes.
Armazene os nomes e as opiniões em um dicionário.
Conte o número de participantes satisfeitos e insatisfeitos.
Exiba a lista de participantes satisfeitos e insatisfeitos, bem como o número
total de cada categoria.
'''

participants = {}
satisfied = {}
dissatisfied = {}
invalid = {}

for i in range(5):
  nome = input('Digite seu nome: ').capitalize()
  opiniao = input('Digite sua opinião: ').capitalize()

  if opiniao == 'Satisfeito':
    satisfied[nome] = opiniao

  elif opiniao == 'Insatisfeito':
    dissatisfied[nome] = opiniao

  else:
    print("Digite uma opção valida!")
    invalid[nome] = opiniao

print('\n------------------------------\nRESULTADO:')
print(f'Participantes satisfeitos: {len(satisfied)}\nParticipantes insatisfeitos: {len(dissatisfied)}\nParticipantes inválidos: {len(invalid)}')

# ------ Estudo de caso 01 resolvido sem necessidade de auxilio ------ #
