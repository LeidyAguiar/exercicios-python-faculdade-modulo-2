"""
6. (Função com parâmetro sem retorno) Faça uma função/método para calcular a tabuada de um número informado pelo usuário.
"""
def calcular_tabuada(numero):
    for i in range(1, 11):
        print(numero, 'X',i,'=', numero * i)

def main():
    tabuada = int(input('Informe um número: '))
    calcular_tabuada(tabuada)

main()