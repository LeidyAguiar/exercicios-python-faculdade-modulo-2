"""
2. (Função com parâmetro com retorno) Faça um programa contendo uma função/método que receba dois números via parâmetro, some os dois valores, retorne e apresente o resultado.
"""

def somar(n1, n2):
    soma = n1 + n2
    return soma

def main():
    numero_1 = int(input('Digite o primeiro número: '))
    numero_2 = int(input('Digite o segundo número: '))
    print('O resultado da soma é:',somar(numero_1, numero_2))

main()