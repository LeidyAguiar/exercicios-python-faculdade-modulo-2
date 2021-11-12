"""
6. (Função sem parâmetro com retorno) Faça um programa contendo uma função/método que verifique se um número é par, 
retorne/mostre o valor bool True para par e False para ímpar.
"""
def func():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        return True
    else:
        return False

def main():
    print('Este programa apresenta se um número é par ou ímpar....\n')
    if func(): # se func() é verdadeira
        print('Este valor é par')
    else:
        print('Este valor é ímpar')
    
main()
