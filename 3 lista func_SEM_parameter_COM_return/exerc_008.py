"""
8. (Função sem parâmetro com retorno) Faça uma função/método retorne um vetor com os três primeiros números perfeitos. Sabe-se que um número é perfeito quando é 
igual a soma de seus divisores (exceto ele mesmo). 

Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito. Não use função pronta.

    1º número perfeito: 6
    2º número perfeito: 28
    3º número perfeito: 496
"""
# outra forma de fazer
def num_perfeito():
    n = 1
    num_perfeito = []
    for n in range (1, 497):
        soma = 0
        for div in range(1,n):
            if n % div == 0:
                soma += div
        if n == soma:
            num_perfeito.append(n)
            n += 1

    return num_perfeito

def main():
    print('Os 3 números perfeitos são: ',num_perfeito())

main()