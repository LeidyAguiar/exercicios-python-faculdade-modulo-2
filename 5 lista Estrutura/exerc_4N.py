"""
4. Uma escola precisa montar o cadastro geral de seus alunos. Este cadastro deverá conter as seguintes informações por aluno: 
nome completo, data de nascimento, telefone, endereço e série atual. Levando em conta que esta escola possui no máximo 500 alunos, 
como você faria para estruturar estas informações num sistema de gerenciamento para a escola? Implemente utilizando estrutura. 
Também use a criação de funções para cada operação. Use o menu a seguir:

Menu de opções:
    1. Cadastrar alunos
    2. Consulta por nome
    3. Visualizar todos os dados
    4. Sair
"""
class TipoEscola:
    nome_completo = ''
    data_nascimento = ''
    telefone = ''
    endereco = ''
    serie_atual = 0

def menu():
    print('1.Cadastrar alunos') 
    print('2.Consulta por nome')
    print('3.Visualizar todos os dados')
    print('4.Sair')
    op = int(input('Qual é a opção desejada? '))
    print()
    return op

def cadastrar_alunos(vet_alunos):
    continuar = 'S'
    while continuar == 'S':
        aluno = TipoEscola() 
        aluno.nome_completo = input('Cadastre o nome do aluno(a): ').ljust(13, ' ')
        aluno.data_nascimento =  input('Coloque a Data de Nascimento do aluno(a): ').ljust(10, ' ')
        aluno.telefone = input('Número de telefone do aluno(a): ').ljust(13, ' ')
        aluno.endereco = input('Coloque o endereço do Aluno: ').ljust(20, ' ')
        aluno.serie_atual = int (input('Qual a série do aluno(a)? '))
        continuar = input('Deseja continuar? [s]im ou [n]ão: ').upper()
        vet_alunos.append(aluno)
        print()

def consultar_nome(vet_nome):
    if len(vet_nome) > 0:
        achou = None
        nome = input('Informe o nome do aluno: ')
        for i in range(len(vet_nome)):
            if nome.lower() in vet_nome[i].nome_completo.lower():
                achou = vet_nome[i]
        if achou:
            print(f'Nome completo: {achou.nome_completo} \tData de Nascimento: {achou.data_nascimento} \tTelefone: {achou.telefone} \tEndereço: {achou.endereco} \tSérie: {achou.serie_atual}')
        else: 
            print(f'Aluno(a) {nome} não existe.')
    else:
        print('Sem dados cadastrados.')
    print()

def exibir_dados(vet_dados):
    if len(vet_dados) > 0:
        for i in range(len(vet_dados)):
            print(f'Nome completo: {vet_dados[i].nome_completo} \tData de Nascimento: {vet_dados[i].data_nascimento} \tTelefone: {vet_dados[i].telefone} \tEndereço: {vet_dados[i].endereco} \tSérie: {vet_dados[i].serie_atual}')
    else:
        print('Sem dados cadastrados.')
    print()

def main():
    opcao = menu()
    vetluno = []
    while opcao >= 1 and opcao <= 3:
        if opcao == 1:
            cadastrar_alunos(vetluno)
        elif opcao == 2:
            consultar_nome(vetluno)
        elif opcao == 3:
            exibir_dados(vetluno)
        opcao = menu()
    print('\nTérmino da execução do programa........')

main()