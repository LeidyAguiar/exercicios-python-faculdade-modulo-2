"""
3. (Função com parâmetro com retorno) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento via parâmetro, 
aplique este aumento a um salário de um funcionário, retorne e apresente o novo salário.
"""

def salario(perc, salario): 
    porcentagem = perc * salario / 100
    return porcentagem + salario

def main():
    percentual = float(input('Informe o percentual: '))
    salario_funcinario = float(input('Informe o salário: '))
    print('O salário com aumento é:',salario(percentual, salario_funcinario))

main()