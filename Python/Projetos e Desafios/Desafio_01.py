print('\n====== DESAFIO 01 - CADASTRO DE FUNCIONÁRIO EM PYTHON! ======\n')

funcionarios = {} # Iniciando a lista de funcionários
cont = 1

def adicionar_func(): # Iniciando a área de adicionar funcionários
    while True:
        cpf = input('Digite o CPF do funcionário (apenas números): ')
        if len(cpf) != 11:
            print('\033[1;31mPOR FAVOR INSIRA UM CPF VÁLIDO!\033[m')
        elif cpf in funcionarios:
            print('\033[1;31mCPF JÁ CADASTRADO!\033[m')
        else:
            break
    
    nome = input('Digite o nome do funcionário: ').title()
    cidade = input('Digite a cidade do funcionário: ').title()
    estado = input('Digite o estado do funcionário: ').title()
    idade = input('Digite a idade do funcionário: ')
    escolaridade = input('Digite a escolaridade do funcionário: ').title()
    cargo = input('Digite o cargo do funcionário: ').title()
    salario = input('Digite o salário do funcionário: ')
    email = input('Digite o e-mail do funcionário: ')

    funcionarios[cpf] = {'Nome': nome,'Cidade': cidade,'Estado': estado,'Idade': idade,'Escolaridade': escolaridade,'Cargo': cargo,'Salário': salario,'E-mail': email}

    print('\033[1;32mFUNCIONÁRIO CADASTRADO COM SUCESSO!\033[m')

def atualizar_func(): # Iniciando a área de atualizar funcionario
    cpf = input('Digite o CPF do funcionário que deseja atualizar: ')
    if cpf not in funcionarios:
        print('\033[1;31mFUNCIONÁRIO NÃO ENCONTRADO!\033[m')
    else:
        print('\033[1;32mFUNCIONÁRIO ENCONTRADO!\033[m')
        print(funcionarios[cpf])
        for key in funcionarios[cpf]:
            novo_dado = input(f'Digite o novo {key} ou pressione Enter para manter o atual ({funcionarios[cpf][key]}): ')
            if novo_dado:
                funcionarios[cpf][key] = novo_dado
        print('\033[1;32mINFORMAÇÕES ATUALIZADAS COM SUCESSO!\033[m')

def listar_func(): # Iniciando a área de listar funcionários
    if not funcionarios:
        print('\033[1;31mNENHUM FUNCIONÁRIO CADASTRADO!\033[m')
    else:
        for cpf, dados in funcionarios.items():
            print(f'\nCPF: {cpf}\n')
            for key, value in dados.items():
                print(f'{key}: {value}')

def remover_func(): # Iniciando a área de remover funcionários
    cpf = input('Digite o CPF do funcionário que deseja remover: ')
    if cpf in funcionarios:
        del funcionarios[cpf]
        print('\033[1;32mFUNCIONÁRIO REMOVIDO COM SUCESSO!\033[m')
    else:
        print('\033[1;31mFUNCIONÁRIO NÃO ENCONTRADO!\033[m')

while cont != 0: # Loop para acessar o menu principal
    print('-=-'*21)
    print('\033[1;32m{}BEM-VINDO AO MENU\033[m'.format(' '*20))
    print('-=-'*21)
    opcao = int(input('Selecione a opção desejada:\n[1] - Adicionar funcionário.\n[2] - Atualizar cadastro.\n[3] - Listar base de dados.\n[4] - Remover usuário.\n[5] - Sair.\nSua escolha será: ')) 

    while opcao > 5 or opcao < 1: # Condição para opções inválidas
        print('\033[1;31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
        opcao = int(input('Selecione a opção desejada:\n[1] - Adicionar funcionário.\n[2] - Atualizar cadastro.\n[3] - Listar base de dados.\n[4] - Remover usuário.\n[5] - Sair.\nSua escolha será: '))
    
    if opcao == 1: # Ao selecionar o valor no menu, o valor redirecionará você para cada função de acordo com o selecionado.
        adicionar_func()
    elif opcao == 2:
        atualizar_func()
    elif opcao == 3:
        listar_func()
    elif opcao == 4:
        remover_func()
    elif opcao == 5:
        print('\033[1;32mSAINDO...\033[m')
        cont = 0