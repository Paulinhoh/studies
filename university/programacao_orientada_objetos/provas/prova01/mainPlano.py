from plano import Plano


def mainPlano():
    pontoList = Plano()

    quant = int(input('Quantas cordenadas deseja adicionar: '))

    i = 1
    while i < quant+1:
        ponto = list()

        x = int(input(f'Insira o valor de X da {i}° cordenada: '))
        y = int(input(f'Insira o valor de Y da {i}° cordenada: '))
        ponto.append(x)
        ponto.append(y)

        valida = pontoList.verificaPonto(ponto)
        if valida == True:
            print('Cordenada ja existente!')
            i -= 1
        else:
            print('Cordenada não existente')
            print('Adicionando cordenada...')
            pontoList.inserirPonto(ponto)

        i += 1

    print('')
    print('Listando os pontos: ')
    pontoList.listarPontos()

    print('')
    remove = int(input('Qual o indice do ponto que deseja remover: '))
    pontoList.removerPonto(remove)

    print('')
    print('Listando os Pontos:')
    pontoList.listarPontos()


def main():
    mainPlano()


if __name__ == '__main__':
    main()
