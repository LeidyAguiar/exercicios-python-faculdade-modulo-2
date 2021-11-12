"""
2. (Função sem parâmetro sem retorno) Faça uma função/método que leia dois valores positivos e apresente a soma dos N números existentes entre eles (inclusive).

Exemplo: 
    a = 2
    b = 8
    soma = 35
"""
def calcular1():
    a = int(input('Digite o valor de a: '))
    b = int(input('Digite o valor de b: '))
    soma_numeros = 0
    for a in range(a, b+1):
        soma_numeros = soma_numeros + a
    print('Valor resultante: ',soma_numeros)

def calcular2():
    a = int(input('\nDigite o valor de a...: '))
    b = int(input('Digite o valor de b...: '))
    soma_numeros = 0
    if a > b: # a = 8 e b = 2
        auxiliar = a  # auxiliar = 8
        a = b # a = 2
        b = auxiliar # b = 8
    for a in range(a,b+1):
        soma_numeros = soma_numeros + a
    print('Valor resultante: ',soma_numeros)

def main():
    calcular1()
    calcular2()

main()