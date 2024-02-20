class Professor:
    '''
      Atributes:
        __nome
        __siape
        __cargaHrSemanal
    '''

    def __init__(self, nome, siape, cargaHrSemanal):
        self.__nome = nome
        self.__siape = siape
        self.__cargaHrSemanal = cargaHrSemanal

    def setNome(self, nome):
        self.__nome = nome

    def setSIAPE(self, siape):
        self.__siape = siape

    def setCargHrSemanal(self, cargaHrSemanal):
        self.__cargaHrSemanal = cargaHrSemanal

    def getNome(self):
        return self.__nome

    def getSIAPE(self):
        return self.__siape

    def getCargaHrSemanal(self):
        return self.__cargaHrSemanal

    def maisHoras(self, cargaHr):
        self.__cargaHrSemanal += cargaHr

    def menosHoras(self, cargaHr):
        self.__cargaHrSemanal -= cargaHr
