from produto import Produto


class Impressora(Produto):

    def __init__(self, modelo: str, tipoImpressora: str, estoque: int):
        super().__init__('impressora', '176602', 'Impressora Inc.')
        self.__modeloImpressora = modelo
        self.__tipoImpressora = tipoImpressora
        self.__estoque = estoque
        self.__flag = True

    def getModeloImpressora(self):
        return self.__modeloImpressora

    def getTipoImpressora(self):
        return self.__tipoImpressora

    def getEstoque(self):
        return self.__estoque

    def __getFlag(self):
        return self.__flag

    def setModeloImpressora(self, modelo):
        self.__modeloImpressora = modelo

    def setTipoImpressora(self, tipoImpressora):
        self.__tipoImpressora = tipoImpressora

    def setEstoque(self, estoque):
        self.__estoque = estoque

    def __setflag(self, flag):
        self.__flag = flag

    def imprimi(self):
        super().imprimi()
        print(
            f'Modelo: {self.__modeloImpressora}\nTipo de Impressora: {self.__tipoImpressora}\nEstoque: {self.__estoque}')

    def aumentaEstoque(self, quant):
        try:
            if (quant is None or quant <= 0):
                print('Error: Entrada Invalida')
            else:
                self.__estoque += quant
        except ValueError:
            print('Error: ValueError')
        except TypeError:
            print('Error: TypeError')

    def diminuiEstoque(self, quant):
        try:
            if (quant is None or quant <= 0):
                print('Error: Entrada Invalida')
            elif (quant > self.__estoque or self.__flag is False):
                print('Error: Valor acima do obtido em estoque')
            else:
                self.__estoque -= quant
                if (self.__estoque == 0):
                    self.__setflag(False)
        except ValueError:
            print('Error: ValueError')
        except TypeError:
            print('Error: TypeError')
