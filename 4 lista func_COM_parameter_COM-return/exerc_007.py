"""
7. (Função com parâmetro com retorno) Faça um programa contendo algumas funções:

a) Função para construir um menu de opções para uma calculadora:
    *** Minha Calculadora ***
    Digite um número.....: 
    Digite outro número..: 
        + Soma dois números
        - Subtrai dois números
        * Multiplica dois números
        / Divide dois números
    Qual opção deseja? 

b) Desenvolva uma função para cada opção de cálculo, **mas estas não terão retorno**.
Observação: Na chamada da função deve-se utilizar uma estrutura de repetição que permita diversos cálculos, 
quando o usuário quiser sair da calculadora digitará qualquer valor diferente dos **caracteres** do menu.
A função de desenho/construção do menu, chamará todas as outras passando a elas os valores digitados.
"""

def menu():
    print('\n*** Minha Calculadora ***')
    print('+ Soma dois números')
    print('- Subtrai dois números')
    print('* Multiplica dois números')
    print('/ Divide dois números')
    num = str(input('Informe qual caractere você quer: '))
    return num

def soma(num1, num2):
    print(f'{num1} + {num2} = {num1 + num2}')

def subtracao(num1, num2):
    print(f'{num1} - {num2} = {num1 - num2}')

def multiplicacao(num1, num2):
    print(f'{num1} * {num2} = {num1 * num2}')

def divisao(num1, num2):
    print(f'{num1} / {num2} = {num1 / num2}')
    
def main():
    opcao = menu()
    while opcao == '+' or opcao == '-' or opcao == '*' or opcao == '/':    
        numero_1 = int(input('Informe um número: '))
        numero_2 = int(input('Informe um outro número: '))
        if opcao == '+':
            soma(numero_1, numero_2)
        elif opcao == '-':
            subtracao(numero_1, numero_2)
        elif opcao == '*':
            multiplicacao(numero_1, numero_2)
        elif opcao == '/':
            divisao(numero_1, numero_2)
        opcao = menu()
    print('\n\nTérmino da execução do programa........')

main()