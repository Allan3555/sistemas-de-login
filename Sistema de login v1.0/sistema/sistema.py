# projeto feito em 05/04/2020
from lib import *
from time import sleep

while True:
    r = menu(['Logar no sistema', 'Novo', 'Sair'])
    if r == 1 or r == 'logar' or r == 'logar no sistema':
        cabecalho('LOGIN')
        email_l = str(input("Digite seu email:\n "))
        senha_l = str(input("Digite sua senha:\n"))
        logar(email_l, senha_l)
        sleep(0.5)
    elif r == 2 or r == 'criar':
        while True:
            cabecalho("CRIAR UMA NOVA CONTA")
            email_novo = str(input("Email: "))
            if "@" not in email_novo:
                print("Email invalido")
                sleep(0.5)
            elif "." not in email_novo:
                print("Algo faltando...")
                sleep(0.5)
            else:
                break
        while True:
            senha_novo = str(input('Crie uma senha: '))
            senha_verify = str(input('Digite sua senha novamente: '))
            if senha_novo != senha_verify:
                print("Senhas nao coincidem")
                sleep(0.5)
            else:
                print('Dados coletados')
                sleep(0.75)
                novo(email_novo, senha_novo)
                break
    elif r == 3 or r == 'sair':
        print('Saindo...')
        sleep(1)
        exit()
    else:
        print("\033[31mErro digite uma opção valida!\033[m")
    sleep(1)
