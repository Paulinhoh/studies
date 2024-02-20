class Produto:

    def __init__(self, tipoProduto, codigoProduto, descricao):
        self.__tipoProduto = tipoProduto
        self.__codigoProduto = codigoProduto
        self.__descricaoProduto = descricao

    def getTipoProduto(self):
        return self.__tipoProduto

    def getCodigoProduto(self):
        return self.__codigoProduto

    def getDescricaoProduto(self):
        return self.__descricaoProduto

    def setTipoProduto(self, tipoProduto):
        self.__tipoProduto = tipoProduto

    def setCodigoProduto(self, codigoProduto):
        self.__codigoProduto = codigoProduto

    def setDescricaoProduto(self, descricao):
        self.__descricaoProduto = descricao

    def imprimi(self):
        print(
            f'Tipo de Produto: {self.__tipoProduto}\nCódigo: {self.__codigoProduto}\nDescrição: {self.__descricaoProduto}')
