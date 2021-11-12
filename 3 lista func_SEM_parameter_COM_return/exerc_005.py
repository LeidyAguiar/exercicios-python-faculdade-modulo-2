"""
5. (Função sem parâmetro com retorno) Faça um programa contendo uma função/método que verifique se um número é par, retorne mostrando a str/string ‘É par’ ou se ‘É ímpar’.
"""
def numero():
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        return 'É par'
    else:
        return 'É ímpar'

def main():
    print(numero())
    
main()
