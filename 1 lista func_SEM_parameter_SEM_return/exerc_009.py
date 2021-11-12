"""
9. (Função sem parâmetro sem retorno) Faça uma função/método que leia cinco valores inteiros, determine e mostre o maior e o menor deles. 
Não pode usar vetor e função pronta da linguagem Python.
"""
def valores():
    for i in range(5):
        numero = int(input('Digite um número inteiro: '))
        if i == 0:
            maior = numero
            menor = numero
        if numero >= maior:
            maior = numero
        if numero <= menor:
            menor = numero                  
    print('Número menor: ',menor)
    print('Número maior: ',maior)
    
def main():
    valores()

main()