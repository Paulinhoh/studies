from veiculo import Veiculo


class Frota(Veiculo):

    def __init__(self):
        self.__frota = list()

    def addVeiculo(self, object):
        self.__frota.append(object)

    def __testaListaVazia(self):
        if len(self.__frota) > 0:
            return True
        else:
            print('A Frota esta vazia!')

    def buscarVeiculo(self, object):
        if self.__testaListaVazia():
            if object in self.__frota:
                print(object.imprime())
            else:
                print('Objeto não encontrado')

    def removeVeiculo(self, object):
        if self.__testaListaVazia():
            if object in self.__frota:
                self.__frota.remove(object)
                print('Removido com sucesso')
            else:
                print('Objeto não encontrado')

    def listVeiculos(self):
        if self.__testaListaVazia():
            for object in self.__frota:
                if object._tipoVeiculo == 'Carro':
                    print(object.imprime())
                    print('')
            for object in self.__frota:
                if object._tipoVeiculo == 'Moto':
                    print(object.imprime())
                    print('')
            for object in self.__frota:
                if object._tipoVeiculo == 'Bicicleta':
                    print(object.imprime())
                    print('')
