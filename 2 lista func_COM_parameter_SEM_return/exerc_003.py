"""
3. (Função com parâmetro sem retorno) Faça uma função/método para a partir de um preço de um produto informado, calcular e apresentar o novo preço reajustado em 9%.
"""
def preco_produto(preco):
    per = preco * 9 / 100
    total = preco + per
    print('O preço do novo produto reajustado é R$',total)

def main():
    valor = float(input('Informe o valor: '))
    preco_produto(valor)

main()
    