"""
5. (Função com parâmetro com retorno) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, 
aplique este aumento ao salário do funcionário. Na parte principal do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a 
função para aplicar o aumento e gerar o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. 
Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento.
"""

def novo_salario(perc, salario):
    return salario + salario * perc / 100

def main():
    percentual = float(input('Digite a porcentagem: '))
    salario = 0
    soma_salario_novo = 0
    soma_salario_antigo = 0
    i = 0
    while i < 10:
        salario = float(input('Informe o salário: ')) 
        soma_salario_novo += novo_salario(percentual, salario)
        soma_salario_antigo += salario   
        i += 1
    diferença = soma_salario_novo - soma_salario_antigo
    print(f'\nA soma do novo salário R$ {soma_salario_novo:.2f}')    
    print(f'A soma do antigo salário é R$ {soma_salario_antigo:.2f}')
    print(f'A diferença será de R$ {diferença:.2f}')

main()