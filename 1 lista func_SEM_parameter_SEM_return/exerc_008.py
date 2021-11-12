"""
8. (Função sem parâmetro sem retorno) Faça uma função/método que leia uma hora de início e de término de um jogo, ambas divididas em dois valores distintos: hora e minuto. 
Deverá ser apresentado a duração expressa em minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que ele pode começar em um dia e terminar no outro.
"""
def jogo():
    hora_inicial = int(input('Informe a hora inicial do jogo: '))
    minuto_inicial = int(input('Informe os minutos iniciais do jogo: '))
    hora_final = int(input('Informe a hora final do jogo: '))
    minuto_final = int(input('Informe os minutos finais do jogo: '))
    if minuto_final < minuto_inicial:
        minuto_final = minuto_final + 60
        hora_final = hora_final - 1
    if hora_final < hora_inicial:
        hora_final = hora_final + 24
    total_minutos = minuto_final - minuto_inicial
    total_horas = hora_final - hora_inicial
    total = total_horas * 60 + total_minutos
    print('A duração do jogo foi de:', total, 'minutos')
    
def main():
    jogo()

main()
