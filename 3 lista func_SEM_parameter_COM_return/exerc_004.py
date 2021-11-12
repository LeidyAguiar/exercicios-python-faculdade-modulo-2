"""
4. (Função sem parâmetro com retorno) Faça um programa contendo uma função/método que leia o lado de um quadrado e retorne sua área, area = lado².
"""
def lado_quadrado():
    lado = int(input("Digite um lado de um quadrado: "))
    area = lado ** 2
    return area

def main():
    print('O resultado é:', lado_quadrado())
    
main()
