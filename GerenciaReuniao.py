import Reuniao

class GerenciaReuniao:

    def __init__(self):
        self.dados = str

    def criarReuniao(self, participantes, local,dataReuniao,ata):
        r = Reuniao.Reuniao()
        r.setParticipantes(participantes)
        r.setLocal(local)
        r.setDataReuniao(dataReuniao)
        r.setAta(ata)
        return r
        
    def editarAta(self, reuniao,ata):
        """
        :type = object
        :param reuniao:
        :param ata:
        :return: reunião com a ata alterada
        """
        reuniao.setAta(ata)
        return reuniao

    def listarReunioes(self,listaR):
        for r in listaR:
            print(r)
