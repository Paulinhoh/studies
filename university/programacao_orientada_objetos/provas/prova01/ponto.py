class Ponto:
    '''
      Atributes:
       __x
       __y
    '''

    # Construtor
    def __init__(self):
        self.__x = 0
        self.__y = 0

    # Métodos getters e setters

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    # Métodos

    def imprimi(self):
        print(f'({self.__x},{self.__y})')

    def distanciaPontos(self, p):
        # distancia == ((x1-x2)**2 + (y1-y2)**2)**(1/2)
        dist = ((self.__x-p[0])**2 + (self.__y-p[1])**2)**(1/2)
        return dist
