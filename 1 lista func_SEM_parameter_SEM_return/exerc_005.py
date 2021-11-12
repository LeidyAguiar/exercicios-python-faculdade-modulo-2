"""
5. (Função sem parâmetro sem retorno) Faça uma função/método que receba o preço antigo e atual de um produto, 
determine o percentual de acréscimo entre esses valores e apresente-o.

r = (100 * preco_novo - 100 * preco_antigo) / preco_antigo

"""
def preco():
    preco_antigo = float(input('Informe o preço antigo do produto: '))
    preco_novo = float(input('Informe o preço novo do produto: '))
    resultado = (100 * preco_novo - 100 * preco_antigo) / preco_antigo
    print(f'Acréscimo: {resultado:.2f}' '%')

def main():
    preco()

main()