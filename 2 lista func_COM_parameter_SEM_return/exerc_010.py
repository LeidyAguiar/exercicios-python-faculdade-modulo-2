"""
10. (Função com parâmetro sem retorno) Faça uma função/método para verificar e contar quantas letras a tem numa frase. 
Não use NENHUMA função pronta da linguagem Python.
"""
def contar(vogal):
    contador = 0
    for i in vogal:
        if i == ('a') or i == ('A'):
            contador = contador + 1
    print('Quantidade de letras(a):',contador)

def main():
    frase = str(input('Digite uma palavra ou frase: '))
    contar(frase)

main()