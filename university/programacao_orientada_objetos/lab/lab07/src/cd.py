from item import Item


class CD(Item):

    def __init__(self, theTitle, theArtist, tracks, time):
        super().__init__(theTitle, time)
        self.__artist = theArtist
        self.__numberOfTracks = tracks

    def setArtist(self, theArtist):
        self.__artist = theArtist

    def setNumberOfTracks(self, tracks):
        self.__numberOfTracks = tracks

    def getArtist(self):
        return self.__artist

    def getNumberOfTracks(self):
        return self.__numberOfTracks

    def imprime(self):
        print(f'Titulo: {self.__title}\nArtista: {self.__artist}\nTracks: {self.__numberOfTracks}\nTempo: {self.__playingTime}\nTenho: {self.__gotIt}\nComentario: {self.__comment}')
