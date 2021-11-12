"""
3. Elabore uma estrutura para representar um produto (código, nome, preço). Crie uma função para cadastrar 5 produtos. 
Crie outra função para aplicar 10% de aumento no preço do produto e apresente, por meio de outra função, todos os dados do produtos cadastrados, após o aumento.
"""
class TipoProduto:
    codigo = 0
    nome = ''
    preco = 0.0

def cadastrar_produtos():
    vet_produtos = []
    for i in range(5):
        prod = TipoProduto() #preparo-inicialização da variável que representará o TipoProduto
        prod.codigo = int (input('Cadastre o código do produto: '))
        prod.nome = input('Cadastre o nome do produto: ').ljust(15, ' ')
        prod.preco = float (input('Cadastre o preço do produto: '))
        vet_produtos.append(prod)
        print()
    return vet_produtos

def aumento(vet_prod):
    for i in range(len(vet_prod)):
        vet_prod[i].preco = vet_prod[i].preco + vet_prod[i].preco * 10 / 100

def exibir_produtos(vet_prods):
    for i in range(len(vet_prods)):
        print(f'Código: {vet_prods[i].codigo} \tNome: {vet_prods[i].nome} \tPreço: {vet_prods[i].preco:.2f}')

def main():
    vetProd = cadastrar_produtos()
    aumento(vetProd)
    exibir_produtos(vetProd)

main()