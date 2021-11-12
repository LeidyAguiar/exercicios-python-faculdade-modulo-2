"""
2. (Função com parâmetro sem retorno) Faça um programa contendo uma função/método para subtrair dois números e apresentar o resultado.
"""
# Definir a função
def subtrair_numeros_SEM_parametros():
    a = int(input('Informe o primeiro valor: '))
    b = int(input('Informe o segundo valor: '))
    r = a - b
    print('SEM PARÂMETRO ----> O resultado da subtração é', r)

def subtrair_numeros_COM_parametros(x, y):# x = num   y = numero
    # passagem de parâmetro por valor - PARÂMETRO (x, y)
    w = x - y
    print('COM PARÂMETRO ----> O resultado da subtração é',w)

def main():# ponto principal de execução
    subtrair_numeros_SEM_parametros()
    num = int(input('Informe o primeiro valor: '))
    numero = int(input('Informe o segundo valor: '))
    subtrair_numeros_COM_parametros(num, numero)# ARGUMENTOS (num, numero)

main()