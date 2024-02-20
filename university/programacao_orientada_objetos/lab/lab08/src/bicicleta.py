from veiculo import Veiculo


class Bicicleta(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerodemarchas):
        super().__init__(placaveiculo, fabricanteveiculo, 2, 'Bicicleta')
        self.__numerodemarchas = numerodemarchas

    def setNumeroDeMarchas(self, numerodemarchas):
        self.__numerodemarchas = numerodemarchas

    def getNumeroDeMarchas(self):
        return self.__numerodemarchas

    def imprime(self):
        print("Placa do veiculo: " + self._placaVeiculo +
              "\nFabricante do veiculo: " + self._fabricanteVeiculo +
              "\nNumero de rodas: " + str(self._numeroRodas) +
              "\nTipo de veiculo: " + self._tipoVeiculo +
              "\nNumero de marchas: " + str(self.__numerodemarchas))
