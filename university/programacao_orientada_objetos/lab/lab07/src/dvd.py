from item import Item


class DVD(Item):

    def __init__(self, theTitle, theDirector, time):
        super().__init__(theTitle, time)
        self.__director = theDirector

    def setDirector(self, theDirector):
        self.__director = theDirector

    def getDirector(self):
        return self.__director

    def imprime(self):
        print(f'Titulo: {self.__title}\nDiretor: {self.__director}\nTempo: {self.__playingTime}\nTenho: {self.__gotIt}\nComentario: {self.__comment}')
