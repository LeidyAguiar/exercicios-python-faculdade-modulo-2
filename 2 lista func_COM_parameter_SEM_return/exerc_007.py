"""
7. (Função com parâmetro sem retorno) Faça uma função/método que calcule a média de um aluno que realizou duas provas (P1 e P2), a partir desta média, 
chame/crie OUTRA função que verifique se esta média aprova ou reprova o aluno.
"""
# Definição das funções
def calcular_media(p1, p2):# p1 = nota1  p2 = nota2
    media = (p1 + p2) / 2
    print('A média é',media)
    verificar_situacao(media)

def verificar_situacao(med): # med = media
    if med >= 6:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')

def main():
    nota1 = float(input('Cadastre a primeira nota..: '))
    nota2 = float(input('Cadastre a segunda nota...: '))
    calcular_media(nota1, nota2) #argumentos - chamada da função

main()