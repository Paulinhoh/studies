from item import Item

class Colecao(Item):

    def __init__(self):
        self.__list = list()

    def addItem(self, item):
        self.__list.append(item)

    def __testaListaVazia(self):
        if len(self.__list) > 0:
            return True
        else:
            print('Não há CDs nem DVDs na sua Coleção!')

    def buscarItem(self, item):
        if self.__testaListaVazia():
            if item in self.__list:
                print(item.imprime())
            else:
                print('Objeto não encontrado')


    def listItems(self):
        if self.__testaListaVazia():
            for item in self.__list:
                print(item.imprime())
                print('')

    def removeItem(self, item):
        if self.__testaListaVazia():
            if item in self.__list:
                self.__list.remove(item)
                print('Removido com sucesso')
            else:
                print('Objeto não encontrado')
