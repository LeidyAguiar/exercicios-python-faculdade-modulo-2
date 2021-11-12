"""
8. (Função sem parâmetro com retorno) Faça uma função/método retorne um vetor com os três primeiros números perfeitos. Sabe-se que um número é perfeito quando é 
igual a soma de seus divisores (exceto ele mesmo). 

Exemplo: os divisores de 6 são 1, 2 e 3, e 1 + 2 + 3 = 6, logo 6 é perfeito. Não use função pronta.

    1º número perfeito: 6
    2º número perfeito: 28
    3º número perfeito: 496
"""
def perfeito():
    numero_perf = []
    achou = 0
    numero = 1
    while achou < 3:
        soma = 0
        for divisor in range(1, numero):
            if numero % divisor == 0: #Verificando se é divisor
                soma += divisor #Soma os divisores
        if numero == soma: #verifica se a soma dos divisores é igual ao número
            numero_perf.append(numero)
            achou += 1  
        numero += 1

    return numero_perf

def main():
    print('Os três primeiros números perfeitos são:',perfeito())

main()