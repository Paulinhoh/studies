from conta import Conta


def main():
    try:
        banco = Conta('Antonio', '1908')
    except TypeError:
        print('Erro: Tipo de entrada Invalido')
    except SyntaxError:
        print('Erro: Syntaxe Incorreta')


    print(banco.getSaldo())


    try:
        banco.deposito(25)
    except TypeError:
        print('Erro: Tipo de entrada Invalido')
    except SyntaxError:
        print('Erro: Syntaxe Incorreta')


    print(banco.getSaldo())


    try:
        banco.saque(5)
    except TypeError:
        print('Erro: Tipo de entrada Invalido')
    except SyntaxError:
        print('Erro: Syntaxe Incorreta')


    print(banco.getSaldo())


    try:
        banco.saque('abc')
    except TypeError:
        print('Erro: Tipo de entrada Invalido')
    except SyntaxError:
        print('Erro: Syntaxe Incorreta')



if __name__ == '__main__':
    main()
