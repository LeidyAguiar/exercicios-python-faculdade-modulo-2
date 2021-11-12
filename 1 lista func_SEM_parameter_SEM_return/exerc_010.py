"""
10. (Função sem parâmetro sem retorno) Faça uma função/método que leia um valor inteiro e positivo N e mostre o valor de S, obtido pelo seguinte cálculo:

S = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
Observação: Não pode usar vetor e função pronta da linguagem Python.
"""
def calcular_fatorial():
    numero = int(input('Digite um número inteiro: '))
    fatorial = 1
    i = 1
    soma = 1
    while i <= numero:
        fatorial = fatorial * i
        soma += 1 / fatorial
        i += 1            
    print(f'Resultado de S: {soma:.2f}')

def main():
    calcular_fatorial()

main()