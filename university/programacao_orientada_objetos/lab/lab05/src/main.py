from randomTester import RandomTester


def main():
    aleatorio = RandomTester()

    aleatorio.printOneRandom()

    aleatorio.printMultiRandom(3)

    aleatorio.throwDice()

    aleatorio.randomMin(3)

    aleatorio.randomMinMax(17, 5)


if __name__ == '__main__':
    main()
