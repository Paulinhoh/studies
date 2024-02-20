from produto import Produto
# from impressora import Impressora
from cadastroProduto import CadastroProduto


def main():
    caneta = Produto('Caneta', '1908', 'Caneta esferografica')

    lista = CadastroProduto()

    lista.armazenar(caneta)
    lista.listarItens()


if __name__ == '__main__':
    main()
