"""
6. (Função sem parâmetro sem retorno) Faça uma função/método que leia um valor inteiro entre 1 e 9 e mostre a seguinte tabela de multiplicação
Neste exemplo foi escolhido o número 9.

1    
2     4
3     6     9
4     8    12    16
5    10    15    20    25
6    12    18    24    30    36
7    14    21    28    35    42    49
8    16    24    32    40    48    56    64   
9    18    27    36    45    54    63    72    81
for i = 1 até n
   for j = 1 até i

Observação: configure o print para não pular linha
"""

# Para ter a mesma forma de apresentação use assim o print(r, end = '\t')
def inteiro():
    numero = int(input('Digite um número entre 1 e 9: '))
    if numero <= 9:
        for i in range(1, numero + 1):
            for j in range(1, i + 1):
                print(j * i,end = '\t')
            print()
def main():
    inteiro()
    
main()