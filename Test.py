import sys
import Usuario
import GerenciaReuniao
import Reuniao


def main():
    cadastro = {'Mario': '123'}
    us = Usuario.Usuario()
    gr = GerenciaReuniao.GerenciaReuniao()
    r = Reuniao.Reuniao()

    print("##### BEM VINDO #####")
    menu = input("[1]. CADASTRAR USUARIO\n[2].LOGAR NO SISTEMA\n[3].SAIR\n")

    while menu != '1' and menu != '2' and menu != '3':
        menu = input("Operação Invalida!!\n[1]. CADASTRAR USUARIO\n[2].LOGAR NO SISTEMA\n[3].SAIR\n")

    if menu == '3':
        sys.exit()

    while menu == '1':
        print('##### REALIZAR CADASTRO #####')
        us.setNome(input("Insira o nome do usuário\n"))
        us.setCpf(input("Informe o CFP do usuário\n"))
        us.setEmail(input("Informe o e-mail do usuário\n"))
        us.setLogin(input("Insira o login do usuário\n"))
        us.setSenha(input("Insira a senha do usuário\n"))

        if us.login in cadastro.keys():
            print("Alguém já esta usando este login")
        else:
            cadastro[us.login] = us.senha
            print("Usuário", us.login, "cadastrado com sucesso")
            print(cadastro)

        menu = input("[1]. CADASTRAR USUARIO\n[2].LOGAR NO SISTEMA\n[3].SAIR\n")

    while menu == '2':
        loginAcesso = input("Insira seu Login\n")
        senhaAcesso = input("Insira a senha\n")

        if loginAcesso in cadastro:
            if senhaAcesso in cadastro.values():
                print("##### LOGIN REALIZADO COM SUCESSO")
                menu = 0
                pagInic = input("[1].CRIAR UMA REUNIAO\n[2].CONFIRMAR OU NEGAR PRESENÇA EM REUNIÕES\n[3].LISTAR REUNIÕES\n")

                while pagInic != '1' and pagInic != '2' and pagInic != '3':
                    pagInic = input("Operação Invalida!!\n[1].CRIAR UMA REUNIAO\n[2].CONFIRMAR OU NEGAR PRESENÇA EM REUNIÕES\n[3].LISTAR REUNIÕES\n")
                if pagInic == '1':
                    for u in cadastro:
                        print(u)

                while len(r.participantes) < 10:
                    part = input("Selecione até 10 participantes\n")
                    for part in cadastro:
                        if part != r.getParticipantes():
                            r.setParticipantes(part)
                        #   print(r.getParticipantes())

                        else:
                            print("Usuário já adicionado a reunião")

            else:
                print("##### LOGIN/SENHA INCORRETOS #####")


    '''while loginAcesso and senhaAcesso not in cadastro.keys():
        print("###### LOGIN/SENHA INCORRETO\n")
        loginAcesso = input("Insira seu Login\n")
        senhaAcesso = input("Insira a senha\n")'''


    '''us = UsuarioComum.Usuario()
    us.setNome("Paulo")
    us.setEmail('Junior@gmail.com')
    us.setEndereco('Rua a')
    us.setCPF("703.506.464.81")


    us2 = UsuarioComum.Usuario()
    us2.setNome("Sergio")
    us2.setEmail('Juniorvasco@gmail.com')
    us2.setEndereco('Rua b')
    us2.setCPF("703.506.464.81")

    participant = []
    participant.append(us)
    participant.append(us2)

    r = Reuniao.Reuniao()

    #r.setParticipantes(participant)

    #print(participantes)

    #print(r.getParticipantes())

    gr = GerenciaReuniao.GerenciaReuniao()

    r = gr.criarReuniao(participant,"Local a","19/11/2019","Ata desconhecida")

    r2 = gr.criarReuniao(participant,"Local master","25/11/2019","Ata desconectada")

    reunioes = []
    reunioes.append(r)
    reunioes.append(r2)
    gr.listarReunioes(reunioes)

    #print(gr.editarAta(r2,'Ata Conhecida'))'''

main()