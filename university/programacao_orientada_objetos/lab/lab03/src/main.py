from professor import Professor
import os
from time import sleep


def escolhaCaso(obj):
    print('Deseja alterar algo:')
    sleep(0.4)
    print('[ 1 ]  Alterar Nome')
    sleep(0.4)
    print('[ 2 ]  Alterar Matricula SIAPE')
    sleep(0.4)
    print('[ 3 ]  Alterar Carga Horaria')
    sleep(0.4)
    print('[ 4 ]  Almentar Carga Horaria')
    sleep(0.4)
    print('[ 5 ]  Diminuir Carga Horaria')
    sleep(0.4)
    print('[ 6 ]  Sair e mostrar Resultados')
    escolha = str(input('>>> '))

    match escolha:
        case '1':
            novoNome = str(input('Novo nome: '))
            obj.setNome(novoNome)
            os.system('cls')
            escolhaCaso(obj)
        case '2':
            novaMatriculaSIAPE = int(input('Nova Matricula: '))
            obj.setSIAPE(novaMatriculaSIAPE)
            os.system('cls')
            escolhaCaso(obj)
        case '3':
            novaCargaHr = int(input('Nova Carga Horaria Semanal: '))
            obj.setCargHrSemanal(novaCargaHr)
            os.system('cls')
            escolhaCaso(obj)
        case '4':
            cargaHr = int(input('Qunato hrs deseja adicionar: ').strip())
            obj.maisHoras(cargaHr)
            os.system('cls')
            escolhaCaso(obj)
        case '5':
            cargaHr = int(input('Qunato hrs deseja diminuir: ').strip())
            obj.menosHoras(cargaHr)
            os.system('cls')
            escolhaCaso(obj)
        case '6':
            mostrarResultados(obj)
        case _:
            print('Escolha invalida! Tente novamente.')
            sleep(2)
            os.system('cls')
            escolhaCaso(obj)


def mostrarResultados(obj):
    print('')
    print('=-='*20)
    print(f'Nome: {obj.getNome()}')
    print(f'Matricula SIAPE: {obj.getSIAPE()}')
    print(f'Carga Horaria Semanal: {obj.getCargaHrSemanal()}')
    print('=-='*20)


def main():
    nome = str(input('Nome: ').strip())
    matriculaSIAPE = int(input('SIAPE: ').strip())
    cargaHr = int(input('Carga Horaria Semanal: ').strip())

    professor = Professor(nome, matriculaSIAPE, cargaHr)
    escolhaCaso(professor)


if __name__ == '__main__':
    main()
