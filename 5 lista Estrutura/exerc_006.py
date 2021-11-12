"""
6. Uma empresa prestadora de serviços armazena informações sobre os serviços prestados. Sabe-se que a empresa pode realizar no máximo três serviços diariamente. 
É de interesse de sua direção manter um histórico mensal (30 dias) sobre os serviços prestados.

A empresa realiza quatro tipos de serviços: 
1) pintura; 
2) jardinagem; 
3) faxina e
4) reforma em geral.

Cada serviço realizado deve ser cadastrado com as seguintes informações: número do serviço, valor do serviço, código do serviço e código do cliente, 
**numa matriz 30x3 referente a estrutura Servico_prestado**.
Cadastre/digite os quatro tipos de serviços (código e descrição) que a empresa poderá realizar. Para isso, utilize um vetor de quatro posições referente a 
**estrutura Tipo_servico**.

O programa deverá mostrar o seguinte menu de opções:
    1. Cadastrar os tipos de serviços
    2. Mostrar todos os tipos de serviço
    3. Cadastrar os serviços prestados
    4. Mostrar todos os serviços prestados
    5. Mostrar os serviços prestados em determinado dia
    6. Mostrar os serviços prestados dentro de um intervalo de valor
    7. Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço
    8. Sair

**Para a opção 1**: deve-se cadastrar os tipos de serviços oferecidos pela empresa, com código e descrição.
**Para a opção 3**: deve-se considerar que deverão ser cadastrados os serviços prestados ao logo do mês. 
  Em cada dia podem ser cadastrados, no máximo, três serviços prestados.
  Utilize uma matriz capaz de armazenar em cada posição todas as informações referentes a um serviço prestado (número, valor, código do serviço, código do cliente). 
**Cada linha representa um dia do mês**. Dessa maneira, considere a matriz com dimensão 30 × 3.
  Solicite o dia em que o serviço foi prestado e as demais informações.
  Lembre-se de que a empresa só pode prestar os serviços que já tenham sido cadastrados no vetor de tipo de serviços.

  Caso o usuário digite um código de tipo de serviço inválido, o programa deverá mostrar uma mensagem de erro.
  Quando o usuário tentar cadastrar mais de três serviços prestados em um mesmo dia, também deverá mostrar uma mensagem de erro.
  **Para a opção 5**: o programa deverá receber o dia que se deseja consultar e mostrar os respectivos serviços prestados.
  **Para a opção 6**: o programa deverá receber o valor mínimo e o valor máximo e mostrar os serviços prestados que estiverem nesse intervalo.
  **Para a opção 7**: o programa deverá mostrar todos os serviços prestados, conforme o exemplo a seguir.

                  DIA 01
                        No do serviço   | Valor do serviço R$      | Código do serviço      |   Descrição           | Código do cliente
                            100         |   200,00                 |    1                   |   Pintura             |     1
                            150         |   100,00                 |    3                   |   Faxina              |     5
                            201         |   640,00                 |    4                   |   Reforma em geral    |     2

                  DIA 02
                        No do serviço   | Valor do serviço R$      | Código do serviço      | Descrição             | Código do cliente
                            301         |   600,00                 |    4                   |   Reforma em geral    |   3
                            280         |   352,00                 |    1                   |   Pintura             |   2
                            306         |   200,00                 |    2                   |   Jardinagem          |   1
"""

# Por onde começo a programar esse exercício?
# Sempre comece da parte mais simples/talvez a menor e já vai implementando e testando

class TipoServico:
    codigo_servico = 0
    descricao = ''

class ServicoPrestado:
    numero_do_servico = 0
    valor_do_servico = 0.0
    codigo_do_servico = 0
    codigo_do_cliente = 0

def menu():
    print('\n *** Empresa de Prestação de Serviços ***')
    print('1. Cadastrar os tipos de serviços')
    print('2. Mostrar todos os tipos de serviço')
    print('3. Cadastrar os serviços prestados')
    print('4. Mostrar todos os serviços prestados')
    print('5. Mostrar os serviços prestados em determinado dia')
    print('6. Mostrar os serviços prestados dentro de um intervalo de valor')
    print('7. Mostrar um relatório geral (separado por dia), que exiba, inclusive, a descrição do tipo do serviço')
    print('8. Sair')
    opcao = int(input('Qual é a opção desejada? '))
    return opcao

# opcao 1
def cadastrar_servicos(vet_cadastrar):
    print('\n... Cadastro dos Tipos de Serviços ...')
    continuar = 'S'
    while continuar == 'S':
        servico = TipoServico()
        servico.codigo_servico = int(input('Cadastre o código do tipo de serviço: '))
        servico.descricao = input('Cadastre a descrição do tipo de serviço: ').ljust(10, ' ').title()
        continuar = input('Deseja continuar? [s]im ou [n]ão: ').upper()
        vet_cadastrar.append(servico)

# opcao 2
def exibir_servicos(vet_servicos):
    print('\n...Apresentação dos Tipos de Serviços ...')
    print('Código   \tDescrição')
    for i in range(len(vet_servicos)):     
        print(f'{vet_servicos[i].codigo_servico} \t\t{vet_servicos[i].descricao}')

# opcao 3
def cadastrar_servicos_prestado(matriz, vet_servicos):
    i = 0
    dia = int(input('Informe o dia que deseja agendar o serviço: '))
    if dia > 0 and dia <= 30:
        vet_dia = matriz[dia -1]
        if len(vet_dia) < 3:
            prest = ServicoPrestado()
            prest.numero_do_servico = int(input('Digite o número do serviço: '))
            prest.valor_do_servico = float(input('Digite o valor do serviço: '))
            prest.codigo_do_cliente = int(input('Informe o código do cliente: '))
            achou = False
            while achou == False:
                prest.codigo_do_servico = int(input('Informe o código do serviço: '))
                for i in range(len(vet_servicos)):
                    if vet_servicos[i].codigo_servico == prest.codigo_do_servico:
                        achou = True
                if achou == False:
                    print('Código Inválido')        
            print()
            vet_dia.append(prest)
            #return vet_dia
        else:
            print('\nQuantidade máxima de serviços excedida, por favor informe outro dia')
        print()
    else:
        print('Informe os dias entre 1 e 30....')

# opcao 4
def todos_servicos_prestados(matriz):
    print('\n... Apresentação dos Serviços Prestados ...')
    for i in range(len(matriz)):
        linha = matriz[i]
        print(f'Dia {i + 1}')
        print('\tCódigo   \t Valor   \tTipo de Serviço   \tCódigo do Cliente')
        for l in range(len(linha)):
            print(f'\t{linha[l].numero_do_servico} \t\t{linha[l].valor_do_servico:.2f} \t\t\t{linha[l].codigo_do_servico} \t\t\t{linha[l].codigo_do_cliente}')
    print()

# opcao 5
def consultar_dia(matriz):
    dia = int(input('Informe o dia que deseja consultar: '))
    print('\n... Apresentação dos Serviços Prestados em determinado dia ...')
    print('\nNº do Serviço  \t Valor do Serviço R$  \tCódigo do Serviço  \tCódigo do Cliente')
    if dia > 0 and dia <= 30:
        diaVet = matriz[dia -1]
        for col in range(len(diaVet)):
            print(f'{diaVet[col].numero_do_servico} \t\t\t{diaVet[col].valor_do_servico:.2f} \t\t\t{diaVet[col].codigo_do_servico} \t\t\t{diaVet[col].codigo_do_cliente}')
    else:
        print('Informe somente os dias entre 1 e 30....')
        print()

# opcao 6
def valores_min_max(matriz):
    valor_minino = float(input('Informe um valor inicial: '))
    valor_maximo = float(input('Informe um valor final: '))
    for i in range(len(matriz)):
        linha = matriz[i]
        print(f'Dia {i + 1}')
        print('\tCódigo   \t Valor   \tTipo de Serviço   \tCódigo do Cliente')
        for l in range(len(linha)):
            if linha[l].valor_do_servico >= valor_minino and linha[l].valor_do_servico <= valor_maximo:
                print(f'\t{linha[l].numero_do_servico} \t\t{linha[l].valor_do_servico:.2f} \t\t\t{linha[l].codigo_do_servico} \t\t\t{linha[l].codigo_do_cliente}')

# opcao 7
def todos_servicos(matriz, vetserv):
    print('\n... Apresentação de todos os Serviços Prestados ...')
    
    for i in range(len(matriz)):
        linha = matriz[i]
        if len(linha) > 0:
            print(f'\nDia {i + 1}')
            print('\tNº do Serviço  \t Valor do Serviço R$  \tCódigo do Serviço  \tDescrição  \tCódigo do Cliente')
            for l in range(len(linha)):
                for i in range(len(vetserv)):
                        if vetserv[i].codigo_servico == linha[l].codigo_do_servico:
                            descricao = vetserv[i].descricao
                print(f'\t{linha[l].numero_do_servico} \t\t\t{linha[l].valor_do_servico:.2f} \t\t\t{linha[l].codigo_do_servico} \t\t{descricao} \t\t{linha[l].codigo_do_cliente}')  
   
def main():
    vetserv = []
    matriz_servicos = []
    for lin in range(30):
        vet_linha = []
        matriz_servicos.append(vet_linha)
    opcao = menu()
    while opcao >= 1 and opcao <= 7:
        if opcao == 1:
            cadastrar_servicos(vetserv)
        elif opcao == 2:
            exibir_servicos(vetserv)
        elif opcao == 3:
            cadastrar_servicos_prestado(matriz_servicos, vetserv)
        elif opcao == 4:
            todos_servicos_prestados(matriz_servicos)
        elif opcao == 5:
            consultar_dia(matriz_servicos)
        elif opcao == 6:
            valores_min_max(matriz_servicos)
        elif opcao == 7:
            todos_servicos(matriz_servicos, vetserv)
        opcao = menu()
        
main()