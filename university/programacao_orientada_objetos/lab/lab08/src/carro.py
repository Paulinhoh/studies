from veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, placaveiculo, fabricanteveiculo, numerodeportas):
        super().__init__(placaveiculo, fabricanteveiculo, 4, 'Carro')
        self.__numerodeportas = numerodeportas

    def setNumeroDePortas(self, numeroDePortas):
        self.__numerodeportas = numeroDePortas

    def getNumeroDePortas(self):
        return self.__numerodeportas

    def imprime(self):
        print("Placa do veiculo: " + self._placaVeiculo +
              "\nFabricante do veiculo: " + self._fabricanteVeiculo +
              "\nNumero de rodas: " + str(self._numeroRodas) +
              "\nTipo de veiculo: " + self._tipoVeiculo +
              "\nNumero de portas: " + str(self.__numerodeportas))
