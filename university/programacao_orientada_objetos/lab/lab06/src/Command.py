'''
This class is part of the "World of Zuul" application.
"World of Zuul" is a very simple, text based adventure game.

This class holds information about a command that was issued by the user.
A command currently consists of two strings: a command word and a second
word (for example, if the command was "take map", then the two strings
obviously are "take" and "map").

The way this is used is: Commands are already checked for being valid
command words. If the user entered an invalid command (a word that is not
known) then the command word is <null>.

If the command had only one word, then the second word is <null>.

@author  Michael Kolling and David J. Barnes
@version 2008.03.30
'''


class Command:
    '''
    Create a command object. First and second word must be supplied, but
    either one (or both) can be null.
    @param firstWord The first word of the command. Null if the command
                     was not recognised.
    @param secondWord The second word of the command.
    '''
    def __init__(self, firstWord, secondWord):
        self.__commandWord = firstWord
        self.__secondWord = secondWord

    '''
    Return the command word (the first word) of this command. If the
    command was not understood, the result is null.
    @return The command word.
    '''
    def getCommandWord(self):
        return self.__commandWord

    '''
    @return The second word of this command. Returns null if there was no
    second word.
    '''
    def getSecondWord(self):
        return self.__secondWord

    '''
    @return true if this command was not understood.
    '''
    def isUnknown(self):
        return (self.__commandWord is None)

    '''
    @return true if the command has a second word.
    '''
    def hasSecondWord(self):
        return not (self.__secondWord is None)
