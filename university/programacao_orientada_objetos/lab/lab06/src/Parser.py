'''
This class is part of the "World of Zuul" application.
"World of Zuul" is a very simple, text based adventure game.

This parser reads user input and tries to interpret it as an "Adventure"
command. Every time it is called it reads a line from the terminal and
tries to interpret the line as a two word command. It returns the command
as an object of class Command.

The parser has a set of known command words. It checks user input against
the known commands, and if the input is not one of the known commands, it
returns a command object that is marked as an unknown command.

@author  Michael Kolling and David J. Barnes
@version 2008.03.30
'''

from CommandWords import CommandWords
from Command import Command


class Parser:

    '''
    Create a parser to read from the terminal window.
    '''
    def __init__(self):
        self.__commands = CommandWords()  # holds all valid command words

    '''
    @return The next command from the user.
    '''
    def getCommand(self):
        word1 = None
        word2 = None

        inputLine = input("> ").split()

        # Find up to two words on the line.
        if (len(inputLine) >= 1):
            word1 = inputLine[0]
        if (len(inputLine) == 2):
            word2 = inputLine[1]

        # Now check whether this word is known. If so, create a command
        # with it. If not, create a "null" command (for unknown command).
        if (self.__commands.isCommand(word1)):
            return Command(word1, word2)

        else:
            return Command(None, word2)
