class Item:

    def __init__(self, theTitle, time):
        self.__title = theTitle
        self.__playingTime = time
        self.__gotIt = False
        self.__comment = ''

    def imprime(self):
        print(f'Titulo: {self.__title}\nTempo: {self.__playingTime}\nTenho: {self.__gotIt}\nComentario: {self.__comment}')

    def setTitle(self, theTitle):
        self.__title = theTitle

    def setPlayingTime(self, time):
        self.__playingTime = time

    def setGotIt(self, gotIt):
        self.__gotIt = gotIt

    def setComment(self, comment):
        self.__comment = comment

    def getTitle(self):
        return self.__title

    def getPlayingTime(self):
        return self.__playingTime

    def getGotIt(self):
        return self.__gotIt

    def getComment(self):
        return self.__comment
