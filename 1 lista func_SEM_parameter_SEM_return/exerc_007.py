"""
7. (Função sem parâmetro sem retorno) Faça uma função/método que leia três notas de um aluno e uma letra, se a letra for igual a A, deverá calcular a média aritimética 
das notas dos alunos, se for P, deverá calcular a média ponderada, com pesos 5, 3 e 2. A média deve ser mostrada ao final.

    N1, N2 e N3 são notas.
    P1, P2 e P3 são pesos.
    Média ponderada = (N1 * P1 + N2 * P2 + N3 * P3 ) / (P1 + P2 + P3)
"""
def notas_alunos():
    N1 = float(input('Digite a primeira nota: '))
    N2 = float(input('Digite a segunda nota: '))
    N3 = float(input('Digite a terceira nota: '))
    letra = str(input('Digite uma letra (A ou P): ')) 
    if letra == 'A':
        media = (N1 + N2 + N3) / 3                              
    elif letra == 'P':
        P1 = 5
        P2 = 3
        P3 = 2
        media = (N1 * P1 + N2 * P2 + N3 * P3 ) / (P1 + P2 + P3)
    print(f'A média é: {media:.2f}')

def main():
    notas_alunos()

main()