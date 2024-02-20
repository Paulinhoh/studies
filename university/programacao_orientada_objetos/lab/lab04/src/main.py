from notebook import Notebook


def main():
    bloco_de_notas = Notebook()

    print('=-='*20)
    c = int(input('Quantas notas serão adicionadas: ').strip())
    for i in range(1, c+1):
        conteudo = str(input(f'{i}° Notas: ').strip())
        bloco_de_notas.storeNote(conteudo)

    print('=-='*20)
    print(
        f'Verificando se ha notas cadastradas: {bloco_de_notas.hasNotes()}')

    if bloco_de_notas.hasNotes() == True:
        print('=-='*20)
        print(f'Quantidade de Notas: {bloco_de_notas.numberOfNotes()}')

        print('=-='*20)
        show = int(input('Indice da nota que deseja exibir: '))
        bloco_de_notas.showNote(show)

        print('=-='*20)
        print('Listando as Notas:')
        bloco_de_notas.listNotes()

        print('=-='*20)
        remove = str(input('Qual nota deseja remover: '))
        bloco_de_notas.removeNote(remove)

        print('=-='*20)
        print('Listando Notas com o for:')
        bloco_de_notas.listNotes()

        print('=-='*20)
        compare = str(input('O que deseja comparar: '))
        print(f'Comparação: {bloco_de_notas.compareNotes(compare)}')

        print('=-='*20)
        print('Mostrando uma nota aleatória: ')
        bloco_de_notas.showNoteRandom()

        print('=-='*20)
        quant = int(input('Quantas nostas aleatoria deseja mostra: '))
        print('Mostrando varias nota aleatória:')
        bloco_de_notas.showMultiNoteRandom(quant)
    else:
        print('Não há notas cadastradas')


if __name__ == '__main__':
    main()
