# projeto feito em 08/04/2020
from time import sleep
from sys import stdout
import hashlib

# Sistema de login simples por terminal


class SistemaDeLogin:
    def __init__(self):
        self.msg_menu = '1 - Logar no sistema\n2 - Criar conta\n3 - Sair'
        self.msg_login = ''
        self.msg_novo = 'Criar uma nova conta'
        self.liberar = False

    def linha(self, tam=25):
        return '-' * tam

    # cabeçalho, da um output com msgs formatadas
    def cabecalho(self, msg):
        print(self.linha())
        print(msg.center(25))
        print(self.linha())

    # Menu principal, aqui tem as principais perguntas para o programa tomar um rumo
    def Menu_Principal(self):
        self.cabecalho(self.msg_menu)
        self.resposta = input('Sua escolha: ')

    # def de carregamento
    def carregar(self, msg='', msg2=''):
        for i in range(4):
            stdout.write('\r')
            stdout.write(f'{msg} [%-3s] %d%%' % ('.' * i, 33.34 * i))
            sleep(0.25)
        print('\n'+msg2)

    # def para verificar se o email novo possui '@' e '.', caso n da output de email invalido
    def verify_email1(self):
        while True:
            self.email_novo = str(input("Email: ")).lower()
            if "@" not in self.email_novo:
                print("Email invalido")
                sleep(0.5)
            elif "." not in self.email_novo:
                print("Algo faltando...")
                sleep(0.5)
            else:
                break

# def para verificar se a senha nova tem mais de 8 digitos e tem que coincidir com a senha_verify
    def verify_senha1(self):
        while True:
            self.senha_novo = str(input('Crie uma senha: '))
            if len(self.senha_novo) < 8:
                print('Sua senha deve ter 8 digitos ou mais')
            else:
                senha_verify = str(input('Digite sua senha novamente: '))
                if self.senha_novo != senha_verify:
                    print("Senhas nao coincidem")
                    sleep(0.5)
                else:
                    self.senha_encode = hashlib.md5(
                        self.senha_novo.encode()).hexdigest()
                    break

    # def que escreve a conta do usuario no txt, apos de o email e a senha passarem por verificação
    def Criar(self, email_novo, senha_novo):
        self.arq_email = open('emails.txt', 'a')
        self.arq_email.write(f'{self.email_novo}\n')
        self.arq_email.close()

        self.arq_senha = open('senhas.txt', 'a')
        self.arq_senha.write(f'{self.senha_encode}\n')
        self.arq_senha.close()

    # verificar no login se o email e a senha estao no txt
    def logar(self, email_l, senha_l):
        self.senha_e = hashlib.md5(self.senha_l.encode()).hexdigest()

        self.email_v = open('emails.txt',  'r')
        self.leitura_e = [line.rstrip() for line in self.email_v.readlines()]
        self.senha_v = open("senhas.txt", 'r')
        self.leitura_s = [line.rstrip() for line in self.senha_v.readlines()]

        if self.email_l in self.leitura_e and self.senha_e in self.leitura_s:
            if self.leitura_e.index(self.email_l) == self.leitura_s.index(self.senha_e):
                print('Logado')
                self.liberar = True
        elif self.email_l in self.leitura_e and self.senha_e not in self.leitura_s:
            print('Senha incorreta')
        else:
            print('conta nao registrada!')

        self.email_v.close()
        self.senha_v.close()

    # def Inciar, toda a funçao do sistema de login ira rodar aqui
    def Iniciar(self):
        while True:
            self.Menu_Principal()
            try:
                # Se a resposta for 1 ou Logar no sistema
                if int(self.resposta) == 1 or self.resposta == 'Logar no sistema':
                    self.cabecalho('SING IN')
                    self.email_l = input('Email: ').lower()
                    self.senha_l = input('Senha: ')
                    self.logar(self.email_l, self.senha_l)
                    if self.liberar == False:
                        sleep(0.75)
                        pass
                    elif self.liberar == True:
                        break                   # mais coisas em breve aqui
                # Se a resposta for 2 ou Criar conta
                elif int(self.resposta) == 2 or self.resposta == 'Criar conta':
                    self.cabecalho('SING UP')
                    self.verify_email1()
                    self.verify_senha1()
                    self.Criar(self.email_novo, self.email_novo)
                    self.carregar('Criando conta',
                                  'Registrado no banco de dados')
                    sleep(1)
                # Se a resposta for 3 ou Sair
                elif int(self.resposta) == 3 or self.resposta == 'Sair':
                    print('Saindo')
                    sleep(0.75)
                    self.carregar()
                    break
                else:
                    print('\033[31mErro, digite um numero valido!\033[m')
                    sleep(0.75)
            except:
                print('\033[31mErro, digite um numero valido\033[m')
                sleep(0.75)


sistema = SistemaDeLogin()
sistema.Iniciar()
print('Fim')
