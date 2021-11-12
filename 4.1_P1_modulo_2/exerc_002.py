"""
2. Não use nenhum método/função pronto da linguagem Python. 

Desenvolva todas as funções a seguir:

a) Faça uma função com retorno (um valor no INSS calculado) e com parâmetro (um salario e alíquota de 9% do INSS) 
para calcular o imposto do INSS que é descontado de um funcionário.
b) Faça uma função com retorno (um salário líquido) e com parâmetro (um salario, um valor do INSS) que calcule o salário líquido de cada funionário.
c) Na função main() num laço de repetição, preencha um vetor de 10 funcionários. Em outro laço chame as outras funções (a e b) e apresente 
os salários orginais um por um, o valor que será desconto do INSS e salário líquido gerado.
"""

def calcular_desconto_INSS(salario, aliquota):
    desconto = salario * aliquota / 100
    return desconto

def salario_liquido(salario, imposto):
    return salario - imposto

def main():   
    i = 0
    salario_funcionario = []
    while i < 10:
        salario_funcionario.append(float(input('Digite um salário: ')))
        i += 1
    print('Salário de cada funcionário:',salario_funcionario)
    i = 0
    while i < len(salario_funcionario):
        desconto_INSS = calcular_desconto_INSS(salario_funcionario[i], 9)
        liquido = salario_liquido(salario_funcionario[i], desconto_INSS)
        print('\nDesconto INSS R$',desconto_INSS)
        print('Salário original de cada funcionário R$',salario_funcionario[i])
        print('Salário Líquido R$',liquido)
        i += 1
    
main()