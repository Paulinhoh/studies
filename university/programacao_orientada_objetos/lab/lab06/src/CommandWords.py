'''
This class is part of the "World of Zuul" application.
"World of Zuul" is a very simple, text based adventure game.

This class holds an enumeration of all command words known to the game.
It is used to recognise commands as they are typed in.

@author  Michael Kolling and David J. Barnes
@version 2008.03.30
'''


class CommandWords:

    '''
    Constructor - initialise the command words.
    '''

    def __init__(self):
        # a constant tuple that holds all valid command words
        self.__validCommands = ("go", "quit", "help")

    '''
    Check whether a given String is a valid command word.
    @return true if a given string is a valid command,
    false if it isn't.
    '''

    def isCommand(self, aString):
        if (aString in self.__validCommands):
            return True
        else:
            # we get here, the string was not found in the commands
            return False
