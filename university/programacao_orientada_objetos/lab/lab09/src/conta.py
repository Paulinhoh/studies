class Conta:

    # Construtor
    def __init__(self, nome: str, conta: str):
        self.__nomeCorrentista = self.setNomeCorrentista(nome)
        self.__numeroConta = self.setNumeroConta(conta)
        self.__saldo = 0
        self.__flag = True

    # Métodos
    def deposito(self, valor):
        if self.__flag:
            try:
                if valor > 0:
                    self.__saldo += valor
                else:
                    print('Erro: Valor abaixo ou igual a Zero')
            except ValueError:
                print("Erro: Valor Invalido")
            except TypeError:
                print('Erro: Tipo de entrada invalido')
        else:
            print('Erro: Conta Desativada')

    def saque(self, valor):
        if self.__flag:
            try:
                if valor > 0:
                    if self.__saldo - valor >= 0:
                        self.__saldo -= valor
                    else:
                        print('Erro: Valor acima do possuinte em conta')
                else:
                    print('Erro: Valor abaixo ou igual a Zero')
            except ValueError:
                print('Erro: Valor Invalido')
            except TypeError:
                print('Erro: Tipo de entrada Invalido')
        else:
            print('Erro: Conta Desativada')

    # Métodos Geters and Seters
    def setNomeCorrentista(self, nome):
        if (nome is not None):
            self.__nomeCorrentista = nome
        else:
            print('Erro Tipo de entrada Invalido')

    def setNumeroConta(self, conta):
        if (conta is not None):
            self.__numeroConta = conta
        else:
            print('Erro Tipo de entrada Invalido')

    def setSaldo(self, saldo):
        if (saldo < 0):
            print('Erro Tipo de entrada Invalido')
        else:
            self.__saldo = saldo

    def setContaAtiva(self, contaAtiva):
        self.__flag = contaAtiva

    def getNomeCorrentista(self):
        return self.__nomeCorrentista

    def getNumeroConta(self):
        return self.__numeroConta

    def getSaldo(self):
        return self.__saldo

    def getContaAtiva(self):
        return self.__flag
