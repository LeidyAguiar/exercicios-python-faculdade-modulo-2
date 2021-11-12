"""
1. (Função com parâmetro sem retorno) Faça um programa contendo uma função/método que leia um número e o multiplique por 2, apresente o resultado.

"""
def multiplicar_numero(num):
    mult = num * 2
    print('O resultado é:',mult)

def main():
    numero = float(input('Digite um número: '))
    multiplicar_numero(numero)

main()

