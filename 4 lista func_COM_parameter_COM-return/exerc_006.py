"""
6. (Função com parâmetro com retorno) Faça um programa contendo algumas funções:

a) Função para construir um menu de opções para uma calculadora:
    Menu de cálculos
    1.   Número ao quadrado
    2.   Número ao cubo
    3.   Raiz do número
    4.   Raiz cúbica do número
    Qual é a opção desejada?

b) Desenvolva uma função para cada opção de cálculo.
Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, 
quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos **números** do menu.
A função de desenho/construção do menu, esta chamará todas as outras passando a elas o valor digitado.
"""

def menu():
    print('\nMenu de cálculos')
    print('1.   Número ao quadrado') 
    print('2.   Número ao cubo')
    print('3.   Raiz do número')
    print('4.   Raiz cúbica do número')
    print('5.   Sair')
    op = int(input('Qual é a opção desejada? '))
    return op

def calcular_quadrado(num):
    return num ** 2

def calcular_cubo(num):
    return num ** 3

def calcular_raiz(num):
    return num ** (1/2)

def calcular_cubica(num):
    return num ** (1/3)

def main():
    opcao = menu()
    while opcao >= 1 and opcao <= 4:
        numero = int(input('Informe um número: '))
        if opcao == 1:
            print('O quadrado do número',numero,'é:',calcular_quadrado(numero) )
        elif opcao == 2:
            print('O cubo do número',numero,'é:',calcular_cubo(numero) )
        elif opcao == 3:
            print(f'A raiz quadrada do número {numero} é: {calcular_raiz(numero):.2f}' )
        elif opcao == 4:
            print(f'A raiz cúbica do número {numero} é: {calcular_cubica(numero):.2f}' )
        opcao = menu()
    print('\n\nTérmino da execução do programa........')

main()