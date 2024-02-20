class CadastroProduto():

    def __init__(self):
        self.__cadastro = list()

    def armazenar(self, item):
        self.__cadastro.append(item)

    def listarItens(self):
        for item in self.__cadastro:
            print(item)

    def delete(self, item):
        if item in self.__cadastro:
            self.__cadastro.remove(item)
