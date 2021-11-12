"""
8. (Função com parâmetro sem retorno) Faça uma função/método sem parâmetro, para ler um valor e chamar/criar OUTRA função (com parâmetro) que mostre se o valor é par ou ímpar.
"""
def valor_SEM_parametro():
    numero = int(input('Informe um valor: '))
    valor_COM_parametro(numero)

def valor_COM_parametro(numero):
    if numero % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')

def main():
    valor_SEM_parametro()

main()