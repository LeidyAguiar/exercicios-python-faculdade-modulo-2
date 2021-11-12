"""
4. (Função com parâmetro sem retorno) Faça uma função/método para a partir de um preço de um produto informado, 
calcular e apresentar o novo preço reajustado em alguma porcentagem que deve ser informada (digitada) pelo usuário.
"""
def calcular_aumento(preco, perc): # parâmetros
    aumento = preco + (preco * perc / 100)
    print(f'Preço do produto após o aumento: {aumento:.2f}')

def main():
    produto = float(input('Digite o preço do produto R$ '))
    per = float(input('Digite a porcentagem desejada: '))
    calcular_aumento(produto, per) # argumento
    
main() # chamada da função
