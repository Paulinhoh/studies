class Veiculo:
    def __init__(self, placaveiculo, fabricanteveiculo,
                 numerorodas, tipoveiculo):
        self._placaVeiculo = placaveiculo
        self._fabricanteVeiculo = fabricanteveiculo
        self._numeroRodas = numerorodas
        self._tipoVeiculo = tipoveiculo

    def imprime(self):
        print("Placa do veiculo: " + self._placaVeiculo +
              "\nFabricante do veiculo: " + self._fabricanteVeiculo +
              "\nNumero de rodas: " + str(self._numeroRodas) +
              "\nTipo de veiculo " + self._tipoVeiculo)

    def getFabricanteVeiculo(self):
        return self._fabricanteVeiculo

    def setFabricanteVeiculo(self, fabricanteveiculo):
        if len(fabricanteveiculo) == 0:
            print("Fabricante de veiculo vazio")
        else:
            self._fabricanteVeiculo = fabricanteveiculo

    def getPlacaVeiculo(self):
        return self._placaVeiculo

    def setPlacaVeiculo(self, placaveiculo):
        if len(placaveiculo) == 0:
            print("Placa de veiculo vazio")
        else:
            self._placaVeiculo = placaveiculo

    def getNumeroRodas(self):
        return self._numeroRodas

    def setNumeroRodas(self, numerorodas):
        if numerorodas <= 0:
            print("Numero de rodas invalido")
        else:
            self._numeroRodas = numerorodas

    def getTipoVeiculo(self):
        return self._tipoVeiculo

    def setTipoVeiculo(self, tipoveiculo):
        if len(tipoveiculo) == 0:
            print("Tipo de veiculo vazio")
        else:
            self._tipoVeiculo = tipoveiculo
