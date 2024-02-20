'''
Class Room - a room in an adventure game.

This class is part of the "World of Zuul" application.
"World of Zuul" is a very simple, text based adventure game.

A "Room" represents one location in the scenery of the game.  It is
connected to other rooms via exits.  The exits are labelled north,
east, south, west.  For each direction, the room stores a reference
to the neighboring room, or null if there is no exit in that direction.

@author  Michael Kolling and David J. Barnes
@version 2008.03.30
'''


class Room:

    '''
    Create a room described "description". Initially, it has
    no exits. "description" is something like "a kitchen" or
    "an open court yard".
    @param description The room's description.
    '''

    def __init__(self, description):
        self.__description = description
        self.__northExit = None
        self.__southExit = None
        self.__eastExit = None
        self.__westExit = None
        self.__upExit = None
        self.__downExit = None

    '''
    Define the exits of this room.  Every direction either leads
    to another room or is null (no exit there).
    @param north The north exit.
    @param east The east east.
    @param south The south exit.
    @param west The west exit.
    '''

    def setExits(self, north, east, south, west, up, down):
        if north is not None:
            self.__northExit = north
        if east is not None:
            self.__eastExit = east
        if south is not None:
            self.__southExit = south
        if west is not None:
            self.__westExit = west
        if up is not None:
            self.__upExit = up
        if down is not None:
            self.__downExit = down

    def getExit(self, direction):
        if direction == "north":
            return self.__northExit
        if direction == "east":
            return self.__eastExit
        if direction == "south":
            return self.__southExit
        if direction == "west":
            return self.__westExit
        if direction == "up":
            return self.__upExit
        if direction == "down":
            return self.__downExit

    '''
    @return The description of the room.
    '''

    def getDescription(self):
        return self.__description
