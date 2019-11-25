class Reuniao:

    def __init__(self):
       self.ata = str
       self.dataReuniao = str
       self.local = str
       self.participantes = []

    def setAta(self, ata):
        self.ata = ata

    def getAta(self):
        return self.ata

    def setDataReuniao(self,dataReuniao):
        self.dataReuniao = dataReuniao

    def getDataReuniao(self):
        return self.dataReuniao

    def setLocal(self, local):
        self.local = local

    def getLocal(self):
        return self.local

    def setParticipantes(self,participante):
        self.participantes = participante

    def getParticipantes(self):
        return self.participantes

    def __repr__(self):
        return f'A reunião será no dia: {self.getDataReuniao()}\nLocal: {self.getLocal()}\nA ata da reunião será: {self.getAta()}\nCom os seguintes participantes\n{self.getParticipantes()}'

