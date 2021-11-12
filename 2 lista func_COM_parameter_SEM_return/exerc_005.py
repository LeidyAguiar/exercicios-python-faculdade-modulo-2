"""
5. (Função com parâmetro sem retorno) Faça uma função/método para a partir de um valor inicial e um valor final realizar o acumulo desse valores e apresentar o resultado. 
Não use vetor.

Exemplo:
    a = 2
    b = 8
    // 2 + 3 + 4 + 5 + 6 + 7 + 8 = 35
    r = 35
"""
def acumular_valores(i, f):
    soma = 0
    while i <= f:
        soma = soma + i
        i += 1
    print('O resultado é:',soma)

def main():
    inic = int(input('Digite um número inicial: '))
    fin = int(input('Digite um número final: '))
    acumular_valores(inic, fin)

main()