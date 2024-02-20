class Plano:
    '''
      Atributes:
        __pontos
    '''

    # Construtor
    def __init__(self):
        self.__pontos = list()

    # Métodos
    def inserirPonto(self, p):
        self.__pontos.append(p)

    def removerPonto(self, p):
        # if p in self.__pontos:
        #     self.__pontos.remove(p)
        # else:
        #     print('Este não é um ponto valido!')

        if p < len(self.__pontos):
            self.__pontos.pop(p)
        else:
            print('Este não é um ponto valido!')

    def listarPontos(self):
        index = 0
        while index < len(self.__pontos):
            print(self.__pontos[index])
            index += 1

    def verificaPonto(self, p):
        for i in self.__pontos:
            if i == p:
                return True
            else:
                return False
