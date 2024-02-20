from veiculo import Veiculo
from frota import Frota


def main():
    i8 = Veiculo('vhn185', 'BMW', 4, 'Carro')
    cla_250 = Veiculo('mmn862', 'Mercedez', 4, 'Carro')
    xre = Veiculo('bco123', 'Honda', 2, 'Moto')
    monark = Veiculo('NaN', 'Monark', 2, 'Bicicleta')
    bros = Veiculo('cnn558', 'Honda', 2, 'Moto')

    lista = Frota()

    lista.addVeiculo(i8)
    lista.addVeiculo(cla_250)
    lista.addVeiculo(xre)
    lista.addVeiculo(monark)
    lista.addVeiculo(bros)

    lista.buscarVeiculo(xre)
    print('=-=-=-=--=-=-=-=-=-=-=-==-=-')

    lista.removeVeiculo(cla_250)
    print('=-=-=-=--=-=-=-=-=-=-=-==-=-')

    lista.listVeiculos()
    print('=-=-=-=--=-=-=-=-=-=-=-==-=-')


if __name__ == '__main__':
    main()
