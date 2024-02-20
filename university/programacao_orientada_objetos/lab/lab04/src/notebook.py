from random import randint


class Notebook:
    def __init__(self):
        self.__notes = list()

    def storeNote(self, note):  # Adiciona uma nota a lista
        self.__notes.append(note)

    def numberOfNotes(self):  # Mostra quantas notas tem na lista
        return len(self.__notes)

    def showNote(self, noteNumber):  # Mostra as notas de acordo com o indice
        if noteNumber <= 0:
            print('Este não é um número de nota válido')
        elif noteNumber <= self.numberOfNotes():
            print(self.__notes[noteNumber-1])
        else:
            print('Este não é um número de nota válido')

    def removeNote(self, note):  # Remove uma nota através da Nota
        if note in self.__notes:
            self.__notes.remove(note)
        else:
            print(f'Esta não é uma nota válida')

    def listNotes(self):  # Lista as notas
        index = 0
        while index < self.numberOfNotes():
            print(self.__notes[index])
            index += 1

    def listNotesfor(self):
        for i in range(0, self.numberOfNotes()):
            print(self.__notes[i])

    def hasNotes(self):
        if self.numberOfNotes() != 0:
            return True
        else:
            return False

    def compareNotes(self, note):
        count = 0
        for c in self.__notes:
            if c == note:
                count += 1
        if count != 0:
            return True
        else:
            return False

    def showNoteRandom(self):
        valor = randint(1, self.numberOfNotes())
        self.showNote(valor)

    def showMultiNoteRandom(self, quant):
        i = 0
        while i < quant:
            valor = (randint(1, self.numberOfNotes()))
            self.showNote(valor)
            i += 1
