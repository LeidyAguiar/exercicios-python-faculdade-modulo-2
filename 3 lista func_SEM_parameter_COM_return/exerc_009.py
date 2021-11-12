"""
9. (Função sem parâmetro com retorno) Foi realizada uma pesquisa sobre algumas características físicas de cinco habitantes de uma região. 
Foram coletados os seguintes dados de cada habitante: idade, sexo (M - masculino ou F - feminino), cor dos olhos (A - azuis ou C - castanhos), 
cor dos cabelos (L - louros, P - pretos ou C - castanhos).

    1. Faça uma função/método que leia esses dados, armazenando-os em vetores (listas);
    2. Faça uma função/método que determine e devolva a função principal a média de idades das pessoas com olhos castanhos e cabelos pretos;
    3. Faça uma função/método que determine e devolva a função principal a maior idade entre os habitantes;
    4. Faça uma função/método que determine e devolva a função principal a quantidade de indivíduos do sexo feminino com idade entre 18 e 35 anos(inclusive) 
       e que tenham olhos azuis e cabelos louros.
"""
idade = []
sexo = []
olhos = []
cabelo = []

# item 1
def cadastrar():
    i = 0
    while i < 5:
            idade.append(int(input('Informe a idade: ')))
            sexo.append(str(input('Digite o sexo(M)-masculino ou (F)-feminino: ')))
            olhos.append(str(input('Informe a cor dos olhos(A)-azuis ou (C)-castanhos: ')))
            cabelo.append(str(input('Informe a cor do cabelo(L)-loiros,(P)-pretos ou (C)-castanhos: ')))
            i += 1
            print()

# item 2
def media_castanho_preto():
    soma_idade_c_p = 0
    qtde_c_p = 0
    media = 0
    i = 0
    while i < len(idade):
        if olhos[i] == 'C' and cabelo[i] == 'P':
            soma_idade_c_p += idade[i]
            qtde_c_p += 1
            media = soma_idade_c_p / qtde_c_p
        i += 1
    return media

# item 3
def maior_idade():
    maior = 0
    i = 0
    while i < len(idade):
        if idade[i] > maior:
            maior = idade[i]
        i += 1
    return maior
# item 4
def sexo_feminino():
    sexo_feminino = 0
    i = 0
    while i < len(idade):
        if sexo[i] == 'F' and idade[i] >= 18 and idade[i] <= 35 and olhos[i] == 'A' and cabelo[i] == 'L':
            sexo_feminino += 1
        i += 1
    return sexo_feminino

def main():
    cadastrar()
    print('Média de pessoas com olhos castanhos e cabelos pretos:',media_castanho_preto())
    print('Habitante com maior idade:',maior_idade(),'anos')
    print('Quantidade de pessoas do sexo feminino entre 18 e 35 anos e que tenham olhos azuis e cabelos loiros:',sexo_feminino())

main()