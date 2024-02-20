class ProfessorUFS:
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
        self.__cargaHrSemanalMinima = 8
        self.__cargaHrSemanalMaxima = 20

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
        if (self.__cargaHrSemanal + cargaHr) > self.__cargaHrSemanalMaxima:
            self.__cargaHrSemanal = 20
            print('Limite maximo ultrapassado valor da carga horario setado em 20hrs')
        else:
            self.__cargaHrSemanal += cargaHr

    def menosHoras(self, cargaHr):
        if (self.__cargaHrSemanal - cargaHr) < self.__cargaHrSemanalMinima:
            self.__cargaHrSemanal = 0
            print('Limite minino ultrapassado valor da carga horario setado em 0hrs')
        else:
            self.__cargaHrSemanal -= cargaHr
