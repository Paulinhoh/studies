from veiculo import Veiculo
from carro import Carro
from moto import Moto
from bicicleta import Bicicleta


def main():
    veiculo = Veiculo('vhz817', 'BMW', 4, 'Carro')
    carro = Carro('vhz817', 'BMW', 4)
    moto = Moto('vhz817', 'Honda', 500)
    bicicleta = Bicicleta('vhz817', 'Xracing', 6)

    veiculo.imprime()
    print('')
    carro.imprime()
    print('')
    moto.imprime()
    print('')
    bicicleta.imprime()


if __name__ == '__main__':
    main()
