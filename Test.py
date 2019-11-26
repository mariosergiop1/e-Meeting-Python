import sys
import Usuario
import GerenciaReuniao
import Reuniao
import Coordenador

def main():
    cadastro = {'Mario': '123'}
    us = Usuario.Usuario()
    gr = GerenciaReuniao.GerenciaReuniao()
    r = Reuniao.Reuniao()
    c = Coordenador.Coordenador()

    print("##### BEM VINDO #####")
    menu = input("[1]. CADASTRAR USUARIO\n[2].LOGAR NO SISTEMA\n[3].SAIR\n")

    while menu != '1' and menu != '2' and menu != '3':
        menu = input("Operação Invalida!!\n[1]. CADASTRAR USUARIO\n[2].LOGAR NO SISTEMA\n[3].SAIR\n")

    if menu == '3':
        sys.exit()

    while menu == '1':
        print('##### REALIZAR CADASTRO #####')
        cad = input("[1].USARIO COMUM\n[2].COORDENADOR\n[3].GESTOR DE RECURSOS\n")

        if cad == '1':
            us.setNome(input("Insira o nome do usuário\n"))
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

        elif cad == '2':
            validar = input("Insira o código de permissão\n")
            if validar == c.getCod():
                c.setNome(input("Insira o nome do usuário\n"))
                c.setEmail(input("Informe o e-mail do usuário\n"))
                c.setLogin(input("Insira o login do usuário\n"))
                c.setSenha(input("Insira a senha do usuário\n"))
            else:
                print("##### CÓDIGO DE PERMISSÃO INVÁLIDO")
            if c.login in c.cadastroCord.keys():
                print("Alguém já esta usando este login")
            else:
                c.cadastroCord[c.login] = c.senha
                print("Coordenador", c.login, "cadastrado com sucesso")
                print(c.cadastroCord)

            menu = input("[1]. CADASTRAR USUARIO\n[2].LOGAR NO SISTEMA\n[3].SAIR\n")

    while menu == '2':
        loginAcesso = input("Insira seu Login\n")
        senhaAcesso = input("Insira a senha\n")

        if loginAcesso in cadastro:
            if senhaAcesso == cadastro.get(loginAcesso):
                print("##### LOGIN REALIZADO COM SUCESSO #####")
                menu = 0
                pagInic = input("[1].CRIAR UMA REUNIAO\n[2].CONFIRMAR OU NEGAR PRESENÇA EM REUNIÕES\n[3].LISTAR REUNIÕES\n")

                while pagInic != '1' and pagInic != '2' and pagInic != '3':
                    pagInic = input("Operação Invalida!!\n[1].CRIAR UMA REUNIAO\n[2].CONFIRMAR OU NEGAR PRESENÇA EM REUNIÕES\n[3].LISTAR REUNIÕES\n")
                if pagInic == '1':

                 tmp = '1'
                while tmp == '1' and len(r.participantes) < 10:
                    for u in cadastro:
                        print(u)
                    part = input("Selecione até 10 participantes\n")
                    if part in cadastro:
                        if part != r.getParticipantes():
                            r.participantes.append(part)
                            tmp = input("Deseja adicionar mais um participante?\n[1]. SIM\n[2]. NÃO\n")

                        else:
                            print("Usuário já adicionado a reunião")
                    else:
                        print("##### USUÁRIO NÃO CADASTRADO #####")

                    if tmp == '2':
                        print("PARTICIPANTES CONVIDADOS PARA A REUNIAO")
                        print(r.getParticipantes())
                    elif len(r.participantes) >= 10:
                        print("LIMITE DE PARTICIPANTES EXCEDIDA")

                local = input("##### INSIRA O LOCAL DA REUNIÃO #####\n")
                r.setLocal(local)
                data = input("##### INFORME A DATA DA REUNIÃO #####\n")
                r.dataReuniao(data)
                ata = input("##### INFORME A ATA DA REUNIÃO\n")
                r.setAta(ata)
                r = gr.criarReuniao(r.getParticipantes(), local, data, ata)
                reunioes = []
                reunioes.append(r)
                gr.listarReunioes(reunioes)

            else:
                print("##### LOGIN/SENHA INCORRETOS #####")
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