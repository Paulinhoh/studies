from cd import CD
from dvd import DVD
from item import Item
from colecao import Colecao


def main():
    cd1 = CD('Dos Prédios', 'Veigh', 7, '0:50')
    dvd1 = DVD('Inception', 'Christopher Nolan', '2:20')

    print(cd1.getTitle())
    print(dvd1.getDirector())

    print()
    print('=-=-==-=-=-=-=-=-=-=-=-=-')
    print()

    lista = Colecao()

    item1 = Item('Dos Prédios', '0:50')
    item2 = Item('Inception', '0:50')
    item3 = Item('Manual de Como Amar Errado', '0:50')

    item1.setGotIt(True)
    item2.setComment('Adoro os filmes deste Diretor.')

    lista.addItem(item1)
    lista.addItem(item2)
    lista.addItem(item3)

    lista.listItems()






if __name__ == '__main__':
    main()
