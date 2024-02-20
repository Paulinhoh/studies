from ponto import Ponto


def mainPonto(x, y, list):
    pontos = Ponto()

    print(f'X inicializado com: {pontos.getX()}')
    print(f'Y inicializado com: {pontos.getY()}')

    print('')
    print('Alterando os valores de X e Y:')
    pontos.setX(x)
    pontos.setY(y)
    pontos.imprimi()

    print('')
    print('Utilizando os Métodos:')
    distancia = pontos.distanciaPontos(list)
    print(f'Distancia: {distancia:.3f}')


def main():
    mainPonto(5, 7, [3, 5])


if __name__ == '__main__':
    main()
