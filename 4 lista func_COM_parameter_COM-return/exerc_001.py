"""
1. (Função com parâmetro com retorno) Faça um programa contendo uma função/método que receba por parâmetro um número e o multiplique por 2, 
retorne e apresente o resultado da função.
"""

def multiplicar(numero):
    result = numero * 2
    return result
     
def main():
    num = int(input('Informe o número: '))
    print('O resultado da multiplicação é:',multiplicar(num))

main()