from sys import stdout
from time import sleep


def leiaint(msg):
    while True:
        try:
            n = int(input(f"\033[33m{msg}: \033[m"))
        except (ValueError, TypeError):
            print(
                '\033[31mErro: por favor, digite um numero inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mNenhum valor.\033[m')
            return 0
        else:
            return n


def line(size=42):
    return '-' * size


def cabecalho(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 0
    for c, item in enumerate(lista):
        print(f"\033[32m{c+1}\033[m - \033[36m{item}\033[m")
    print(line())
    opition = leiaint("Sua opção")
    return opition


def novo(email_novo, senha_novo):
    emailtxt = open('emails.txt', 'a')
    emailtxt.write(f'{email_novo}\n')
    emailtxt.close()
    senhatxt = open('senhas.txt', 'a')
    senhatxt.write(f'{senha_novo}\n')
    senhatxt.close()
    carregar('Criando conta', ' Feito')


def logar(email_l, senha_l):
    email_v = open('emails.txt', 'r')
    leitura_e = [line.rstrip() for line in email_v.readlines()]
    senha_v = open("senhas.txt", 'r')
    leitura_s = [line.rstrip() for line in senha_v.readlines()]
    if email_l in leitura_e and senha_l in leitura_s:
        if leitura_e.index(email_l) == leitura_s.index(senha_l):
            carregar('Logando', ' Logado')
    elif email_l in leitura_e and senha_l not in leitura_s:
        print('Senha incorreta')
    else:
        print('conta nao registrada!')
    email_v.close()
    senha_v.close()


def carregar(msg='', msg2=''):
    for i in range(4):
        stdout.write('\r')
        stdout.write(f'{msg} [%-3s] %d%%' % ('.' * i, 33.34 * i))
        sleep(0.25)
    print(msg2)
