"""
3. (Função sem parâmetro sem retorno) Faça uma função/método que receba três números inteiros a, b, c que sejam divisíveis por a. 
O valores b e c representam o intervalo da estrutura de repetição. Apresente a quantidade e os números divisíveis. 
Não pode usar vetor e função pronta da linguagem Python.

Exemplo:
    a = 5
    b = 1
    c = 10
    qtde = 2
    Números divisíveis 5, 10
"""
def verificar():
    divisiveis = ''
    qtde = 0
    a = int(input('Informe um número inteiro(primeiro número): '))
    b = int(input('Informe um número inteiro(segundo número): '))
    c = int(input('Informe um número inteiro(último número): '))
    while b <= c:       
        if b % a == 0:
            qtde += 1
            divisiveis += str(b) + ', '
        b += 1
    print('Quantidade:',qtde)
    print('Números Divisíveis:',divisiveis)

def main():
    verificar()

main()