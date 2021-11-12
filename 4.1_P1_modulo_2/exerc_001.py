"""
1. Para fazer o cadastro em uma rede social, o usuário deve preencher vários dados, inclusive um e-mail válido, ou seja, 
um e-mail deve conter UM caracter arroba '@' e UM ou MAIS caracteres ponto '.'
Crie uma função que retorne como resposta, se um e-mail é 'válido' ou 'inválido'. Não use nenhum método/função pronto ou o operador in no if, da linguagem Python. 
Avalie caracter por caracter. Deve ser criada a função main para chamar a da verificação.
"""

def verificar_email(email):
    qtde_arroba = 0
    qtde_ponto = 0
    for i in range(len(email)):
        if email[i] == '@':
            qtde_arroba += 1
        if email[i] == '.':
            qtde_ponto += 1
    if qtde_arroba == 1 and qtde_ponto >= 1:
        return 'válido'
    else:
        return 'Inválido'

def main():
    email_pessoa = str(input('Digite seu e-mail: '))
    print('O e-mail é:',verificar_email(email_pessoa))

main()
