from estudante import Estudante


def main():
    alunoA = Estudante('Eduarda', 1, 50)
    alunoB = Estudante('Paulo Henrique', 2)
    alunoC = Estudante('Duda', 3)

    nome = str(input('Informe o nome do aluno: '))
    cred = int(input('Informe a quantidade de creditos: '))

    if (alunoA.getNome() == nome):
        alunoA.addCredito(cred)
        print(f'{alunoA.getNome()}, {alunoA.getMat()}, {alunoA.getCred()}')
    elif (alunoB.getNome() == nome):
        alunoB.addCredito(cred)
        print(f'{alunoB.getNome()}, {alunoB.getMat()}, {alunoB.getCred()}')
    elif (alunoC.getNome() == nome):
        alunoC.addCredito(cred)
        print(f'{alunoC.getNome()}, {alunoC.getMat()}, {alunoC.getCred()}')
    else:
        print(f'Aluno(a) {nome} não encontrado no sistema!')


if __name__ == '__main__':
    main()
