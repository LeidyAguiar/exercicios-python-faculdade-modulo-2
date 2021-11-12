"""
5. (Função com parâmetro com retorno) Faça um programa contendo uma função/método que receba um valor de porcentagem de aumento e um salário via parâmetro, 
aplique este aumento ao salário do funcionário. Na parte principal do programa, na chamada da função, utilize um laço de repetição para ler 10 salários, chame a 
função para aplicar o aumento e gerar o novo salário, ainda dentro da estrutura de repetição acumule os novos salários e ao final apresente quanto será gasto no novo salário. 
Também apresente qual será a diferença entre o que se pagava para todos os funcionário e o que será pago após o aumento.
"""

# prof fez durante a aula
def aplicar_aumento(porcent_, salario_):
    return salario_ + salario_ * porcent_ / 100
def main():
    soma_salario_novo = 0
    soma_salarios_antigos = 0
    porcent = float(input('Cadastre a porcentagem de aumento: '))
    for cont in range(5):
        salario = float(input('Cadastre o salário: '))
        soma_salarios_antigos = soma_salarios_antigos + salario
        soma_salario_novo += aplicar_aumento(porcent, salario) # x = x + salario_novo
    print(f'\nA empresa pagará o total de novos salários R$ {soma_salario_novo:.2f}' )
    print(f'Resultado da soma do salário antigo R$ {soma_salarios_antigos:.2f}' )
    print(f'A diferença será de R$ {soma_salario_novo - soma_salarios_antigos:.2f}' )
main()