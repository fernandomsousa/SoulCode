'''
Contexto:
Uma escola precisa analisar as notas de seus alunos e determinar se cada aluno
foi aprovado ou reprovado. As notas serão armazenadas em uma lista e a análise
deve ser realizada em um loop.
'''

'''
Requisitos:
Peça ao usuário para inserir o nome e a nota de cinco alunos.
Armazene os nomes e as notas em listas separadas.
Para cada aluno, verifique se a nota é maior ou igual a 60. Se sim, o aluno está
aprovado; caso contrário, está reprovado.
Exiba uma mensagem para cada aluno informando seu nome, nota e se foi aprovado
ou reprovado.
'''

name = []
grade = []

for n in range(5):
    nome = input(f'Digite o nome do aluno: ').capitalize()
    nota = float(input(f'Digite a nota de {nome}: '))
    name.append(nome)
    grade.append(nota)

for g in range(5):
    nome = name[g]
    nota = grade[g]
    
    if nota >= 60:
        situacao = "aprovado"
    else:
        situacao = "reprovado"
    
    print(f'{nome} teve uma nota final de {nota} e, portanto, está {situacao}!')

# ------ Estudo de caso 02 resolvido com auxilio de IA ------ #