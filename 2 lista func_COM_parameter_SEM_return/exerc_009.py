"""
9. (Função com parâmetro sem retorno) Faça uma função/método para verificar se um nome digitado é igual a ‘Ana’, mostre o valor True ou False como resposta.
"""
def verificar_nome(nome):
    if nome == 'Ana' or nome == 'ana':
        print('True')
    else:
        print('False')

def main():
    pessoa = str(input('Digite um nome: '))
    verificar_nome(pessoa)

main()