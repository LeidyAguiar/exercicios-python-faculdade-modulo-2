"""
4. (Função sem parâmetro sem retorno) Faça uma função/método que leia um único valor representado em segundos, converta-o e apresente o resultado em horas, minutos e segundos.

    h = segundos / 3600
    r = resto(segundos / 3600)
    m = r / 60
    s = resto(r / 60)
    Observação 1: resto de uma divisão em Python %.
    Observação 2: a hora, o minuto e o segundo devem ser apresentados como números inteiros. 
"""
# Declarar/definir a função
def calcular_horas():
    segundos = int(input('Informe um valor em segundos: '))
    horas = segundos / 3600
    resto_horas = segundos % 3600
    minutos = resto_horas / 60
    segundos = resto_horas % 60
    print('\nHora(s):', horas//1, '\nMinutos:',minutos//1, '\nSegundos:', segundos//1)

def main():
    print('Entrei na Main')
    calcular_horas() # chamada da função
    print('\nTérmino do programa....')

main() # chamada da função