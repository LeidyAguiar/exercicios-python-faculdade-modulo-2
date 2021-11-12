"""
3. Elabore uma estrutura para representar e armazenar 10 alunos (matricula, nome, telefone). 
Utilize os recursos de arquivo para armazenar estes dados permanentemente. 
O nome do arquivo deve ser o mesmo da estrutura. 
Construa um menu com as seguintes opções, cada uma delas deve ter uma função e a main para chamar todas elas.

Menu de opções:
    1. Cadastrar alunos
    2. Visualizar todos os dados
    3. Sair
"""

class Tipo_Aluno:
    matricula = 0
    nome = ''
    telefone = ''

def cadastrar_alunos(vetAlunos):
    arq_produto = open('aluno.txt','w')
    for i in range(2):
        aluno = Tipo_Aluno()
        aluno.matricula = int(input('Informe a matrícula do aluno: '))
        aluno.nome = input('Informe o nome do aluno: ')
        aluno.telefone = input('Informe o telefone: ')
        vetAlunos.append(aluno)
        arq_produto.write(f'{aluno.matricula},{aluno.nome},{aluno.telefone}\n')
        print()
    arq_produto.close()
    return vetAlunos

def mostrar_dados():
    arq_produto = open('aluno.txt','r')
    for index in arq_produto.readlines():
        matric,nome,telef = index.strip().split(',')
        print(matric.ljust(5,' '),'\t',nome.ljust(12,' '),'\t',telef.ljust(11,' '))
    arq_produto.close()

def main():
    operacao = 1
    while operacao >= 1 and operacao <=2:
        print('*** Gerenciamento de Cadastro Alunos***')
        print('1 - Cadastrar alunos')
        print('2 - Visualizar todos os dados')
        print('3 - Sair')
        operacao = int(input('Digite a opção: '))
        if operacao == 1:
            vetAlun= []
            vetAlun = cadastrar_alunos(vetAlun)
        elif operacao == 2:
            mostrar_dados()

main()