"""
1. (Função sem parâmetro sem retorno ) Faça um programa contendo uma função/método que apresente o valor 1 se o número digitado for positivo e 0 se for negativo.
"""

def verificar():
    numero = int(input('Digite um número: '))
    if numero > 0:
        print('1')
    else:
        print('0')

def main():
    verificar()

main()