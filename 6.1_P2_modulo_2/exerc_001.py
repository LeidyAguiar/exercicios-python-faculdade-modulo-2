"""
1. Em Python crie um programa que atenda o menu a seguir. Desenvolva uma função para cada opção do menu. Utilize a criação de estruturas. 
Cadastrar 5 (vetor) vendas ( Tipo_Venda: cod_venda (int), dia(int), total(float), cliente (Tipo_Cliente: cod_cliente (int), nome(str) )

Menu de opções:
1 Cadastrar clientes
2 Mostrar todos os clientes
3 Cadastrar vendas
4 Mostrar todas as vendas
5 Mostrar o total de vendas de um determinado dia
6 Armazenar todos os campos da venda em um arquivo
7 Apresentar o conteúdo do arquivo
8 Sair

**Observaçôes**: 
* Na opção 4, as vendas podem ter o registro, por exemplo, uma venda dia 22, duas vendas no dia 23, outra venda no dia 21, outra venda no dia 15, 
  mais uma venda no dia 15 e assim por diante.
* Na opção 5, o usuário do sistema informará/digitará o dia que quer e o sistema/programa fará uma pesquisa e calculará o total de vendas.
* Na opção 6 e 7 o nome do arquivo deverá ser **vendas.txt**
"""
class Tipo_Venda:
    cod_venda = 0
    dia = 0
    total = 0.0

class Tipo_Cliente:
    cod_cliente = 0
    nome = ''

def menu():
    print('1. Cadastrar clientes')
    print('2. Mostrar todos os clientes')
    print('3. Cadastrar vendas')
    print('4. Mostrar todas as vendas')
    print('5. Mostrar o total de vendas de um determinado dia')
    print('6. Armazenar todos os campos da venda em um arquivo')
    print('7. Apresentar o conteúdo do arquivo')
    print('8. Sair')
    op = int(input('Qual é a opção desejada? '))
    print()
    return op

# 1. Cadastrar clientes
def cadastrar_clientes(vet_clientes):
    print('\n... Cadastro de Clientes ...')
    for i in range(5):
        clientes = Tipo_Cliente()
        clientes.cod_cliente = int(input('Cadastre o código do cliente: '))
        clientes.nome = input('Cadastre o nome do cliente: ')
        vet_clientes.append(clientes)

# 2. Mostrar todos os clientes
def exibir_todos_clientes(vet_exibir):
    print('Código Cliente  \tNome Cliente')
    for i in range(len(vet_exibir)):
        print(f'{vet_exibir[i].cod_cliente} \t\t\t{vet_exibir[i].nome}')
    print()

# 3. Cadastrar vendas
def cadastrar_vendas(vet_vendas):
    print('\n... Cadastro de Clientes ...')
    for i in range(5):
        vendas = Tipo_Venda()
        vendas.cod_venda = int(input('Digite o código da venda: '))
        vendas.dia = int(input('Digite o dia: '))
        vendas.total = float(input('Digite o valor da venda: '))
        vet_vendas.append(vendas)

# 4. Mostrar todas as vendas
def exibir_todas_vendas(vet_exibir_vend):
    for i in range(len(vet_exibir_vend)):
        print('Código  \tDia  \tTotal')
        print(f'{vet_exibir_vend[i].cod_venda} \t\t{vet_exibir_vend[i].dia} \t{vet_exibir_vend[i].total}')

# 5. Mostrar o total de vendas de um determinado dia
def vendas_dia(vet_vendas):
    dia = int(input('Informe o dia que deseja consultar: '))
    if dia > 0 and dia <= 30:
        soma = 0
        for i in range(len(vet_vendas)):
            if vet_vendas[i].dia == dia:
                soma = soma + vet_vendas[i].total
        print(f'Total de Vendas: {soma}\n')
    else:
        print('Informe somente os dias entre 1 e 30....')

# 6. Armazenar todos os campos da venda em um arquivo
def armazenar_vendas(vetor_vendas):
    arq_vendas = open('vendas.txt', 'w')
    for i in range(len(vetor_vendas)):
        arq_vendas.write(f'{vetor_vendas[i].cod_venda},{vetor_vendas[i].dia},{vetor_vendas[i].total}\n')
    arq_vendas.close()

# 7. Apresentar o conteúdo do arquivo
def apresentar_conteudo():
    print(f'Código \tDia \tTotal')
    arq_vendas = open('vendas.txt', 'r')
    for i in arq_vendas.readlines():
        cod,dia,total = i.strip().split(',')
        print(f'{cod} \t{dia} \t{total}')
    arq_vendas.close()

def main():
    opcao = menu()
    vetclientes = []
    vetvendas = []
    while opcao >= 1 and opcao <= 7:
        if opcao == 1:
            cadastrar_clientes(vetclientes)
        elif opcao == 2:
            exibir_todos_clientes(vetclientes)
        elif opcao == 3:
            cadastrar_vendas(vetvendas)
        elif opcao == 4:
            exibir_todas_vendas(vetvendas)
        elif opcao == 5:
            vendas_dia(vetvendas)
        elif opcao == 6:
            armazenar_vendas(vetvendas)
        elif opcao == 7:
            apresentar_conteudo()
        opcao = menu()
        
main()