from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(input("Please enter your name: "), room['outside'])


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# READ
# EVAL
# PRINT
# LOOP
while True:
    print(f'{player1.name} is now in {player1.current_room.name}...')
    print(f'{player1.current_room.description}...')
    x = input(
        "Where would you like to go next? press [n] for north, [s] for south, [e] for east, and [w] for west: ")
    if (x == 'q'):
        print('Goodbye')
        quit(0)

    elif x == 'n':
        if player1.current_room.n_to is not None:
            player1.current_room = player1.current_room.n_to
            print(f'{player1.name} moved North...')
        else:
            print('You cannot go that way')
    elif x == 's':
        if player1.current_room.s_to is not None:
            player1.current_room = player1.current_room.s_to
            print(f'{player1.name} moved South...')
        else:
            print('You cannot go that way')
    elif x == 'e':
        if player1.current_room.e_to is not None:
            player1.current_room = player1.current_room.e_to
            print(f'{player1.name} moved East...')
        else:
            print('You cannot go that way')
    elif x == 'w':
        if player1.current_room.w_to is not None:
            player1.current_room = player1.current_room.w_to
            print(f'{player1.name} moved West...')
        else:
            print('You cannot go that way')
    elif (x not in ['n', 's', 'w', 'e']):
        print('Please enter a valid direction')

