"""
1. (Função sem parâmetro com retorno) Faça um programa contendo uma função/método que leia um número e o multiplique por 2 retornando o resultado e o apresente.
"""
def multiplicar():
    n = int(input("Digite um número: "))
    resultado = n * 2
    return resultado

def main():
    print('O resultado é:', multiplicar())
    
main()
