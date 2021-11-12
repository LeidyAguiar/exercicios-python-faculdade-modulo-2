"""
2. Elabore uma estrutura para representar e armazenar 10 produtos (código, nome, preço). 
Utilize os recursos de arquivo para armazenar estes dados permanentemente. 
O nome do arquivo deve ser o mesmo da estrutura. 
Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.

Menu de opções:
    1. Cadastrar produtos
    2. Visualizar todos os dados
    3. Sair
"""

class Tipo_Produto:
    codigo = 0
    nome = ''
    preco = 0.0

def cadastrar_produtos(vetfuncionario):
    arq_produto = open('produto2.txt','w')
    for i in range(2):
        produto = Tipo_Produto()
        produto.codigo = int(input('Informe o código do produto: '))
        produto.nome = input('Informe o nome do produto: ')
        produto.preco = float(input('Informe o preço do produto: '))
        vetfuncionario.append(produto)
        arq_produto.write(f'{produto.codigo},{produto.nome},{produto.preco:.2f}\n')
        print()
    arq_produto.close()
    return vetfuncionario

def mostrar_dados():
    arq_produto = open('produto2.txt','r')
    for index in arq_produto.readlines():
        codigo,nome,preco = index.strip().split(',')
        print(codigo.ljust(2,' '),'\t',nome.ljust(15,' '),'\t',preco)
    arq_produto.close()

def main():
    operacao = 1
    while operacao >= 1 and operacao <=2:
        print('*** Gerenciamento de Produtos ***')
        print('1 - Cadastrar')
        print('2 - Mostrar')
        print('3 - Sair')
        operacao = int(input('Digite a opção: '))
        if operacao == 1:
            vetFunc= []
            vetFunc = cadastrar_produtos(vetFunc)
        elif operacao == 2:
            mostrar_dados()

main()