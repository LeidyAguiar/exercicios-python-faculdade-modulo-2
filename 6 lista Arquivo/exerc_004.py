"""
4. Baixe o arquivo futebol.txt que esta na pasta Material do aula do Teams. Leia este arquivo e o apresente. Com os dados lidos, 
armazene na estrutura Futebol (posicao_jogo, altura, peso, imc), calcule o IMC (Índice de Massa Corporal), armazene na estrutura e também em outro arquivo, 
mas agora chamado futebol_imc.txt. 
Apresente este novo arquivo. 

Observação: esse exercício deve ser testado fora do Colab, no Idle ou qualquer outra IDE, porque usará um arquivo que estará na pasta material de aula.
"""

# imc = peso / (altura ** 2)

class Tipo_Futebol:
    posicao_jogo = ''
    altura = 0.0
    peso = 0.0
    imc = 0.0

arq_futebol = open('futebol.txt','r')
arquivo = open('futebol_imc.txt','w+')
for index in arq_futebol.readlines():
    posicao,altura,peso= index.strip().split(',')
    altura = float(altura)
    peso = float(peso)
    imc = peso / (altura ** 2)   
    print(f'{posicao},\t{altura},\t{peso}')
    posicao,altura,peso= index.strip().split(',')
    arquivo.write(f'{posicao},{altura},{peso},{imc:.2f}\n')
print()
arq_futebol.close()
arquivo.close()

arquivo_imc = open('futebol_imc.txt','r')
print('*** Arquivo com IMC ***')
for i in arquivo_imc.readlines():
    pos,alt,pes,imc= i.strip().split(',')
    print(f'{pos},\t{alt},\t{pes},\t{imc}')

arquivo_imc.close()




        

