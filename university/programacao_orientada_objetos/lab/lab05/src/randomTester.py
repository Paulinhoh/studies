import random


class RandomTester:
    def printOneRandom(self):
        print(f'Numero Aleatório: {(random.random()*10):.0f}')

    def printMultiRandom(self, many):
        print(f'Imprimindo {many} valores aleatórios.')
        for i in range(1, many+1):
            print(f'{i}° valor aleatório {(random.random()*10):.0f}')

    def throwDice(self):
        print(f'Valor aletório entre 1 e 6: {random.randint(1, 6)}')

    def randomMin(self, max):
        self.randomMinMax(max)

    def randomMinMax(self, max, min=1):
        print(
            f'Valor aleatótio entre {min} á {max}: {random.randint(min, max)}')
