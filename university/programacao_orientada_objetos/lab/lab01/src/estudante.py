class Estudante:
    '''atributes: __nome, __mat, __cred'''

    # Construtor
    def __init__(self, nome, mat, cred=0):
        self.__nome = nome
        self.__mat = mat
        self.__cred = cred

    # Métodos
    def addCredito(self, pontosAdicionais):
        self.__cred += pontosAdicionais

    # Métodos geters e seters
    def setNome(self, nome):
        self.__nome = nome

    def setMat(self, mat):
        self.__mat = mat

    def setCred(self, cred):
        self.__cred = cred

    def getNome(self):
        return self.__nome

    def getMat(self):
        return self.__mat

    def getCred(self):
        return self.__cred
