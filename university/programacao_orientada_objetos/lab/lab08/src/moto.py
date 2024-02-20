from veiculo import Veiculo


class Moto(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, cilindradas):
        super().__init__(placaveiculo, fabricanteveiculo, 2, 'Moto')
        self.__cilindradas = cilindradas

    def setCilindradas(self, cilindradas):
        self.__cilindradas = cilindradas

    def getCilindradas(self):
        return self.__cilindradas

    def imprime(self):
        print("Placa do veiculo: " + self._placaVeiculo +
              "\nFabricante do veiculo: " + self._fabricanteVeiculo +
              "\nNumero de rodas: " + str(self._numeroRodas) +
              "\nTipo de veiculo: " + self._tipoVeiculo +
              "\nCilindradas: " + str(self.__cilindradas))
