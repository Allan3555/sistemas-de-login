# projeto feito dia 18/04
import PySimpleGUI as sg
from pathlib import Path
import hashlib

sg.change_look_and_feel('LightGrey1')

# Arquivo txt para escrever e ler os usuarios
ARQUIVO = 'conta.txt'
# verificar se o arquivo ja existe, caso nao, cria um
file = Path(ARQUIVO)
if file.is_file():
    pass
else:
    file = open(ARQUIVO, 'w')
    file.close()


class AppLogin:
    def __init__(self):
        # layout de login
        layout_de_login = [
            [sg.Text('Email'), sg.Input(key='email_login')],
            [sg.Text('Senha'), sg.Input(key='senha_login')],
            [sg.Checkbox('Mante-se conectado', key='KeepConnected'),
             sg.Button('Logar')],
            [sg.Button('Criar uma conta'), sg.Button('Sair')]
        ]

        # janela de login
        self.janela_de_login = sg.Window('Login', layout=(layout_de_login))

        # layout de registro
        layout_de_registro = [
            [sg.Text('Email'), sg.Input(key='email')],
            [sg.Text('Senha'), sg.Input(key='senha')],
            [sg.Text('Confirmar senha'), sg.Input(key='senha_verify')],
            [sg.Button('Criar conta'), sg.Button('Sair')]
        ]

        # janela de registro
        self.janela_de_registro = sg.Window(
            'Resgistrar-se', layout=(layout_de_registro))

    # cria um hash md5 para as senhas
    def gerar_hash(self, senha):
        return hashlib.md5(senha.encode()).hexdigest()

    # inicia a janela de login
    def Iniciar(self):
        while True:
            buttons, values = self.janela_de_login.Read()
            self.email_login = values['email_login']
            self.senha_login = values['senha_login']
            if buttons == None:
                break
            if buttons in ('Sair'):
                sair = sg.popup_yes_no('Voce realmente deseja sair?')
                if sair == 'Yes':
                    break
                else:
                    pass
            elif buttons == 'Logar':
                if not self.empty_verify_login():
                    self.login()
                else:
                    sg.popup('Preencha os campos corretamente!',
                             no_titlebar=True)
            elif buttons == 'Criar uma conta':
                self.janela_de_login.Close()
                self.register()

    # inicia a janela de resgrito de contas
    def register(self):
        while True:
            buttons, values = self.janela_de_registro.Read()
            self.email = values['email']
            self.senha = values['senha']
            self.senha_verify = values['senha_verify']
            if buttons == None:
                break
            if buttons == 'Sair':
                sair = sg.popup_yes_no('Você realmente deseja sair?')
                if sair == 'Yes':
                    break
                else:
                    pass
            elif buttons == 'Criar conta':
                if not self.empty_verify_register():
                    self.registrar()
                else:
                    sg.popup('Preencha os campos corretamente!',
                             no_titlebar=True)

    # verifica se todos os campos da janela de registro estão preenchidos
    def empty_verify_register(self):
        if self.email == '' or self.senha == '' or self.senha_verify == '':
            return True

    # verifica se a senha de cadastro possui mais de 8 caracteres e se é igual a "senha_verify"
    def verify_senha(self):
        if len(self.senha) < 2:
            sg.popup('As senhas devem contem 8 ou mais caracteres!',
                     no_titlebar=True)
        else:
            if self.senha != self.senha_verify:
                sg.popup('As senhas não coincidem!', no_titlebar=True)
            else:
                return True

    # verifica se o email de cadastro possui os caracteres [@] e [.]
    def verify_email(self):
        if '@' not in self.email and '.' not in self.email:
            sg.popup_ok('email invalido')
        else:
            return True

    # verifica se o email e a senha de cadastro estao no padrao correto
    def registrar(self):
        self.verify_email()
        if self.verify_email():
            self.verify_senha()
            if self.verify_senha() == True:
                self.escrever_conta()
                sg.popup('Conta criada!', no_titlebar=True)

    # escreve a conta do usuario no arquivo txt
    def escrever_conta(self):
        senha = self.gerar_hash(self.senha)
        arq = open(ARQUIVO, 'a')
        arq.write(f'{self.email};{senha}\n')
        arq.close()

    # verifica se todos os campos da janela de login estão preenchidos
    def empty_verify_login(self):
        if self.email_login == '' or self.senha_login == '':
            return True

    # verifica se o email digitado se encontra no arquivo txt, caso sim, retorna as informações
    def search_email(self):
        global leitura
        arq = open(ARQUIVO, 'r')
        for line in arq.readlines():
            leitura = line.replace(';', ' ').split()
            if leitura[0] == self.email_login:
                return leitura
            else:
                return None

    # verificar se a senha coincide com a do registro
    def verificar_senha(self):
        senha = self.gerar_hash(self.senha_login)
        if leitura[1] == senha:
            return True
        else:
            pass

    # verifica se todos os dados foram inseridos corretamente
    def logar(self):
        self.search_email()
        if self.search_email() != None:
            self.verificar_senha()
            if self.verificar_senha():
                sg.popup_no_titlebar('logado!!')
                self.janela_de_login.close()
            else:
                sg.popup_no_titlebar('Senha incorreta')
        else:
            sg.popup_no_titlebar('Conta não cadastrada!')


sistema = AppLogin()
sistema.Iniciar()
