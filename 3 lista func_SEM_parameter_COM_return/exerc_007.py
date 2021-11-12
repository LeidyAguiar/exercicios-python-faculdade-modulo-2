"""
7. (Função sem parâmetro com retorno) Faça uma função/método que leia e armazene 5 elementos inteiros no vetor A, deverá ser gerado um vetor B, de mesmo tamanho, 
que armazenará o fatorial de cada elemento de A. Não use função pronta de cálculo de fatorial. Retorne/apresente o vetor B.
"""
def armazenar():
    A = []
    B = []
    for i in range(1, 6):
        numero = int(input('Digite um número inteiro: '))
        A.append(numero)

    for Index_A in range(len(A)):
        numero = A[Index_A]
        fat = 1
        i = 1
        while i <= numero:
            fat = fat * i
            i += 1
        B.append(fat)
        
    return B

def main():
    print(armazenar())

main()