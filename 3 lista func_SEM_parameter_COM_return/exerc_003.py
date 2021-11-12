"""
3. (Função sem parâmetro com retorno) Faça um programa contendo uma função/método que leia a base e a altura de um triângulo e retorne/apresente sua área A = (base x altura)/2.
"""
def triangulo():
    base = int(input("Informe a base do triângulo: "))
    altura = int(input("Informe a altura do triângulo: "))
    area = (base * altura) / 2
    return area

def main():
    print('A área do triângulo é:', triangulo())
    
main()