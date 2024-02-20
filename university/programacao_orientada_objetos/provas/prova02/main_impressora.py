from impressora import Impressora


def main():
    try:
        impressora = Impressora('Hp', 'Corporativa', 48)

        impressora.imprimi()

        print('')

        impressora.aumentaEstoque(22)
        impressora.diminuiEstoque(70)

        impressora.imprimi()

        print('')
        impressora.aumentaEstoque(12)

        impressora.imprimi()
    except TypeError:
        print('Error: TypeError')
    except ValueError:
        print('Error: ValueError')


if __name__ == '__main__':
    main()
