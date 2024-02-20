'''
This class is the main class of the "World of Zuul" application.
"World of Zuul" is a very simple, text based adventure game.  Users
can walk around some scenery. That's all. It should really be extended
to make it more interesting!

To play this game, create an instance of this class and call the "play"
method.

This main class creates and initialises all the others: it creates all
rooms, creates the parser and starts the game.  It also evaluates and
executes the commands that the parser returns.

@author  Michael Kolling and David J. Barnes
@version 2008.03.30
'''

from Parser import Parser
from Room import Room


class Game:

    '''
    Create the game and initialise its internal map.
    '''

    def __init__(self):
        self.__createRooms()
        self.__parser = Parser()

    '''
    Create all the rooms and link their exits together.
    '''

    def __createRooms(self):
        # create the rooms
        outside = Room("outside the main entrance of the university")
        theatre = Room("in a lecture theatre")
        pub = Room("in the campus pub")
        lab = Room("in a computing lab")
        office = Room("in the computing admin office")
        resun = Room("in the university restaurant")
        bicen = Room("in the library")

        # initialise room exits
        outside.setExits(None, theatre, lab, pub, None, None)
        theatre.setExits(None, None, None, outside, bicen, None)
        pub.setExits(None, outside, None, None, None, resun)
        lab.setExits(outside, office, None, None, None, None)
        office.setExits(None, None, None, lab, None, None)
        resun.setExits(None, None, None, None, pub, None)
        bicen.setExits(None, None, None, None, None, theatre)

        self.currentRoom = outside  # start game outside

    '''
    Main play routine.  Loops until end of play.
    '''

    def play(self):
        self.__printWelcome()

        # Enter the main command loop.  Here we repeatedly read commands and
        # execute them until the game is over.

        finished = False
        while (not finished):
            command = self.__parser.getCommand()
            finished = self.__processCommand(command)
        print("Thank you for playing.  Good bye.")

    '''
    Print out the opening message for the player.
    '''

    def __printWelcome(self):
        print("\nWelcome to the World of Zuul!")
        print("World of Zuul is a new, incredibly boring adventure game.")
        print("Type 'help' if you need help.\n")

        self.__printLocationInfo()

    '''
    Given a command, process (that is: execute) the command.
    @param command The command to be processed.
    @return true If the command ends the game, false otherwise.
    '''

    def __processCommand(self, command):
        wantToQuit = False

        if (command.isUnknown()):
            print("I don't know what you mean...")
            return False

        commandWord = command.getCommandWord()
        if (commandWord == "help"):
            self.__printHelp()
        elif (commandWord == "go"):
            self.__goRoom(command)
        elif (commandWord == "quit"):
            wantToQuit = self.__quit(command)

        return wantToQuit

    # implementations of user commands:

    '''
    Print out some help information.
    Here we print some stupid, cryptic message and a list of the
    command words.
    '''

    def __printHelp(self):
        print("You are lost. You are alone. You wander")
        print("around at the university.\n")
        print("Your command words are:")
        print("   go quit help")

    '''
    Try to go to one direction. If there is an exit, enter
    the new room, otherwise print an error message.
    '''

    def __goRoom(self, command):
        if (not command.hasSecondWord()):
            # if there is no second word, we don't know where to go...
            print("Go where?")
            return

        direction = command.getSecondWord()

    # Try to leave current room.

        nextRoom = None
        if (direction == "north"):
            nextRoom = self.currentRoom.getExit(direction)
        if (direction == "east"):
            nextRoom = self.currentRoom.getExit(direction)
        if (direction == "west"):
            nextRoom = self.currentRoom.getExit(direction)
        if (direction == "south"):
            nextRoom = self.currentRoom.getExit(direction)
        if (direction == "up"):
            nextRoom = self.currentRoom.getExit(direction)
        if (direction == "down"):
            nextRoom = self.currentRoom.getExit(direction)
        if (nextRoom is None):
            print("There is no door!")
        else:
            self.currentRoom = nextRoom

            self.__printLocationInfo()

    '''
    "Quit" was entered. Check the rest of the command to see
    whether we really quit the game.
    @return true, if this command quits the game, false otherwise.
    '''

    def __quit(self, command):
        if (command.hasSecondWord()):
            print("Quit what?")
            return False
        else:
            return True  # signal that we want to quit

    def __printLocationInfo(self):
        print("You are " + self.currentRoom.getDescription())
        exits = ""

        if (self.currentRoom.getExit("north") is not None):
            exits += "north "
        if (self.currentRoom.getExit("east") is not None):
            exits += "east "
        if (self.currentRoom.getExit("south") is not None):
            exits += "south "
        if (self.currentRoom.getExit("west") is not None):
            exits += "west "
        if (self.currentRoom.getExit("up") is not None):
            exits += "up "
        if (self.currentRoom.getExit("down") is not None):
            exits += "down "

        print("Exits: " + exits)
