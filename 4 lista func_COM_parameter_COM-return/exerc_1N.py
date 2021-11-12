"""
1. (Função com parâmetro com retorno) Faça um programa contendo uma função/método que receba por parâmetro um número e o multiplique por 2, 
retorne e apresente o resultado da função.
"""

# prof fez na aula como exemplo

def multiplicar(numero):
    result = numero * 2
    return result

def main():
    # outra forma de chamar a função com retorno
    numero = int(input('Informe o número: '))
    x = multiplicar(numero)
    print('O resultado da multiplicação é:',x)
    if x > 5:
        print('É maior que 5')
        w = 1000 + x
        print(w)

main()