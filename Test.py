import sys
import Usuario
import GerenciaReuniao
import Reuniao
import Coordenador
import GestorRecursos

def main():
    cadastro = {'Mario': '123', 'Feijao': '123', 'Carlos': '321', 'Marcos': '123'}
    reunioes = []
    u = Usuario.Usuario()
    r = Reuniao.Reuniao()
    c = Coordenador.Coordenador()
    g = GestorRecursos.GestorRecursos()
    gr = GerenciaReuniao.GerenciaReuniao()

    print("##### BEM VINDO #####")
    menu = input("[1].CADASTRAR USUARIO\n[2].LOGAR NO SISTEMA\n[3].SAIR\n")

    while menu != '1' and menu != '2' and menu != '3':
        menu = input("Operação Invalida!!\n[1].CADASTRAR USUARIO\n[2].LOGAR NO SISTEMA\n[3].SAIR\n")

    #Condição para Sair do sistema
    if menu == '3':
        sys.exit()

    #Condição para logar no sistema
    while menu == '1':
        print('##### REALIZAR CADASTRO #####')
        cad = input("[1].USARIO COMUM\n[2].COORDENADOR\n[3].GESTOR DE RECURSOS\n")

        if cad == '1':
            u.setNome(input("Insira o nome do usuário\n"))
            u.setEmail(input("Informe o e-mail do usuário\n"))
            u.setLogin(input("Insira o login do usuário\n"))
            u.setSenha(input("Insira a senha do usuário\n"))

            if u.login in cadastro.keys():
                print("Alguém já esta usando este login")
            else:
                cadastro[u.login] = u.senha
                print("Usuário", u.login, "cadastrado com sucesso")
                print(cadastro)

            menu = input("[1].CADASTRAR USUARIO\n[2].LOGAR NO SISTEMA\n[3].SAIR\n")

        #Condição para logar no sistema como coordenador
        elif cad == '2':
            validar = input("Insira o código de permissão\n")
            if validar == c.getCod():
                c.setNome(input("Insira o nome do usuário\n"))
                c.setEmail(input("Informe o e-mail do usuário\n"))
                c.setLogin(input("Insira o login do usuário\n"))
                c.setSenha(input("Insira a senha do usuário\n"))

                if c.login in c.cadastroCord.keys():
                    print("Alguém já esta usando este login")
                else:
                    c.cadastroCord[c.login] = c.senha
                    print("Coordenador", c.login, "cadastrado com sucesso")
                    print(c.cadastroCord)
            else:
                print("##### CÓDIGO DE PERMISSÃO INVÁLIDO")

            menu = input("[1]. CADASTRAR USUARIO\n[2].LOGAR NO SISTEMA\n[3].SAIR\n")

    #Condição para logar no sistema
    while menu == '2':
        loginAcesso = input("Insira seu Login\n")
        senhaAcesso = input("Insira a senha\n")

        #Validação de acesso
        if loginAcesso in cadastro:
            if senhaAcesso == cadastro.get(loginAcesso):
                print("##### LOGIN REALIZADO COM SUCESSO #####")
                menu = 0
                pagInic = input("[1].CRIAR UMA REUNIAO\n[2].CONFIRMAR OU NEGAR PRESENÇA EM REUNIÕES\n[3].LISTAR REUNIÕES\n")

                while pagInic != '1' and pagInic != '2' and pagInic != '3':
                    pagInic = input("Operação Invalida!!\n[1].CRIAR UMA REUNIAO\n[2].CONFIRMAR OU NEGAR PRESENÇA EM REUNIÕES\n[3].LISTAR REUNIÕES\n")

                #Metodo criação de reunião
                while pagInic == '1':
                    tmp = '1'
                    while tmp == '1' and len(r.participantes) < 10:
                        for t in cadastro:
                            print(t)
                        part = input("Selecione até 10 participantes\n")
                        if part in cadastro:
                            if part in r.getParticipantes():
                                print("Usuário já adicionado a reunião")

                            else:
                                r.participantes.append(part)
                                tmp = input("Deseja adicionar mais um participante?\n[1]. SIM\n[2]. NÃO\n")
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
                    r.setDataReuniao(data)
                    ata = input("##### INFORME A ATA DA REUNIÃO #####\n")
                    r.setAta(ata)
                    r = gr.criarReuniao(r.getParticipantes(), local, data, ata)
                    reunioes.append(r)
                    gr.listarReunioes(reunioes)

                    pagInic = input("[1].CRIAR UMA REUNIAO\n[2].CONFIRMAR OU NEGAR PRESENÇA EM REUNIÕES\n[3].LISTAR REUNIÕES\n")

                #Metodo para listar reunião
                while pagInic == '3':
                    pagInic = ''
                    print("##### LISTAR REUNIÕES #####")
                    gr.listarReunioes(reunioes)
                    arquivo = open('GerenciamentoReuniões.txt', 'w')
                    arquivo.write('A reunião será no dia '+r.getDataReuniao())
                    arquivo.write('Local: '+r.getLocal())
                    arquivo.write('A ata da reunião será: '+r.getAta())
                    arquivo.close()

                    pagInic = input("[1].CRIAR UMA REUNIAO\n[2].CONFIRMAR OU NEGAR PRESENÇA EM REUNIÕES\n[3].LISTAR REUNIÕES\n")

            else:
                print("##### LOGIN/SENHA INCORRETOS #####")

        elif loginAcesso in c.cadastroCord:
            if senhaAcesso == c.cadastroCord.get(loginAcesso):
                print("##### LOGIN REALIZADO COM SUCESSO #####")

            else:
                print("##### LOGIN/SENHA INCORRETOS #####")
        else:
            print("##### LOGIN/SENHA INCORRETOS #####")

main()