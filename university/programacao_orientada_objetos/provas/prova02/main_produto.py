from produto import Produto


def main():
    try:
        produto = Produto('Caneta', '1908', 'Caneta esferografica')

        print(produto.getTipoProduto())

        produto.setCodigoProduto('115521')

        produto.imprimi()
    except TypeError:
        print('Error: TypeError')
    except ValueError:
        print('Error: ValueError')


if __name__ == '__main__':
    main()
