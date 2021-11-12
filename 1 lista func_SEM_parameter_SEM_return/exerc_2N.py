"""
2. (Função sem parâmetro sem retorno) Faça uma função/método que leia dois valores positivos e apresente a soma dos N números existentes entre eles (inclusive).

Exemplo: 
    a = 2
    b = 8
    soma = 35
"""
def verificar():
    soma = 0
    num_inicial = int(input('Informe um número: ')) 
    num_final = int(input('Informe um outro número: '))
    while num_inicial <= num_final:
        soma = soma + num_inicial
        num_inicial += 1   
    print('A soma é:',soma)          

def main():
    verificar()

main()