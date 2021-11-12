"""
2. (Função sem parâmetro com retorno) Faça um programa contendo uma função/método para subtrair dois números, retornar o resultado e o apresentando.
"""
def subtracao():
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite um outro número: "))
    resultado = n1 - n2
    return resultado

def main():
    print('O resultado é:', subtracao())
    
main()