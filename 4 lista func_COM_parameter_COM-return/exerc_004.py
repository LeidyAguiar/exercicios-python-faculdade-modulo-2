"""
4. (Função com parâmetro com retorno) Faça um programa contendo uma função/método que receba duas notas (P1, P2) calcule a média, 
chame outra função na main que avalie se este aluno esta aprovado ou reprovado retornando a str/string 'Aprovado' ou 'Reprovado'.
"""

def calcula_media(p1, p2):
    media_notas = (p1 + p2) / 2
    return media_notas

def verificar_media(media):
    if media >= 6:
        return 'Aprovado'
    else:
        return 'Reprovado'

def main():
    nota_1 = float(input('Digite a nota 1: '))
    nota_2 = float(input('Digite a nota 2: '))
    med = calcula_media(nota_1, nota_2)
    print('Média:',med)
    print('O aluno foi:',verificar_media(med))

main()