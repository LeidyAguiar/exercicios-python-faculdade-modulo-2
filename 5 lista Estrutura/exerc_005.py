"""
5. Faça um programa que realize o cadastro de contas bancarias com as seguintes informações: numero da conta, nome do titular e saldo. 
O banco permitirá o cadastramento de 15 contas. **Crie uma função para cada opção do menu** a seguir. Utilize a estrutura na passagem de parâmetro:

Menu de opções:
    1. Cadastrar contas
    2. Visualizar todas as contas
    3. Consultar por nome
    4. Alterar nome e/ou saldo de um número de conta
    5. Excluir a conta com menor saldo
    6. Sair

Observação: 
* No item de menu 4. Alterar nome e/ou saldo de um número de conta, entenda que apenas pode ser alterado 
  o nome e o saldo depois que você pesquisar pelo número da conta.
* No item 5 do menu, encontre o menor saldo dentre todos cadastrados, **depois exclua esta ÚNICA conta.**. 
"""

class TipoConta:
    numero_da_conta = 0
    nome_titular = ''
    saldo = 0.0

def menu():
    print('1. Cadastrar contas')
    print('2. Visualizar todas as contas')
    print('3. Consultar por nome')
    print('4. Alterar nome e/ou saldo de um número de conta')
    print('5. Excluir a conta com menor saldo')
    print('6. Sair')
    op = int(input('Qual é a opção desejada? '))
    print()
    return op

# opção 1
def cadastrar_contas(vet_conta):
    continuar = 'S'
    while continuar == 'S':
        if len(vet_conta) < 5:
            conta = TipoConta()
            conta.numero_da_conta = int(input('Digite o número da conta: '))
            conta.nome_titular = str(input('Digite o nome do titular da conta: '))
            conta.saldo = float(input('Informe o saldo da conta: '))
            continuar = input('Deseja continuar? [s]im ou [n]ão: ').upper()
            vet_conta.append(conta)
            print()
        else:
            print('Excedeu o número máximo de contas, exclua uma conta para poder cadastrar outras...')
            print(80 * '*')
            continuar = 'N'

# opção 2
def exibir_contas(vet_dados):
    for i in range(len(vet_dados)):
        print(f'Número da conta: {vet_dados[i].numero_da_conta} \nNome do Titular: {vet_dados[i].nome_titular} \nSaldo da conta: {vet_dados[i].saldo:.2f}')
        print(30 * '-')
    print()

# opção 3
def consulta_nome(vet_consulta):
    index = -1
    consulta = str(input('Qual o nome do titular da conta? '))
    for i in range(len(vet_consulta)):
       if consulta.lower() in vet_consulta[i].nome_titular.lower():
            index = i
    if index == -1:
        print('Nome não encontrado')
    else:
        print(f'Número da conta: {vet_consulta[index].numero_da_conta} \nNome do Titular: {vet_consulta[index].nome_titular} \nSaldo da conta: {vet_consulta[index].saldo:.2f}')
    print()

# opção 4
def alterar_nome_saldo(vet_alterar):
    index = -1
    consulta_numero_conta = int(input('Qual o número da conta que deseja buscar? '))
    for i in range(len(vet_alterar)):
        if vet_alterar[i].numero_da_conta == consulta_numero_conta:
            index = i
    if index == -1:
        print('Número da conta não encontrada')
    else:
        opcao = menuAlteracao()
        while opcao >= 1 and opcao <= 2:
            if opcao == 1:
                vet_alterar[index].nome_titular = str(input('Digite o novo nome: '))               
            elif opcao == 2:
                vet_alterar[index].saldo = float(input('Digite o novo saldo: '))
            opcao = menuAlteracao()
        print(f'Número da conta: {vet_alterar[index].numero_da_conta} \nNome do Titular alterado: {vet_alterar[index].nome_titular} \nNovo saldo da conta: {vet_alterar[index].saldo:.2f}')
    print()

# opção 4
def menuAlteracao():
    opcao = 1
    while opcao >= 1 and opcao <= 2:
        print('1. Alterar nome')
        print('2. Alterar saldo')
        print('3. Sair')
        opcao = int(input('Qual é a opção desejada? '))
        return opcao

# opção 5
def excluir_conta(vet_excluir):
    Imenor = 0
    menor = 0.0
    for i in range(len(vet_excluir)):
        if i == 0:
            Imenor = i
            menor = vet_excluir[i].saldo
        else:
            if vet_excluir[i].saldo < menor:
                menor = vet_excluir[i].saldo
                Imenor = i
    print(f'Número da conta excluída: {vet_excluir[Imenor].numero_da_conta} \nNome do Titular: {vet_excluir[Imenor].nome_titular} \nSaldo com menor valor: {vet_excluir[Imenor].saldo:.2f}')
    print()
    del(vet_excluir[Imenor])

def main():
    opcao = menu()
    vetconta = []
    while opcao >= 1 and opcao <= 5:
        if opcao == 1:
            cadastrar_contas(vetconta)
        elif opcao == 2:
            exibir_contas(vetconta)
        elif opcao == 3:
            consulta_nome(vetconta)
        elif opcao == 4:
            alterar_nome_saldo(vetconta)
        elif opcao == 5:
            excluir_conta(vetconta)
        opcao = menu()
        
main()