"""Main file for MacGiver maze game."""
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, \
                          K_UP, K_DOWN, K_LEFT, K_RIGHT
from config import conf_
from maze import Maze
from player import Player
from display import Display


def main():
    """Launch functions."""
    # Load constants
    globals().update(conf_)

    # Launch pygame
    pygame.init()

    # Load & generate the maze from the file
    level = Maze()
    # Manage player movements and generate inventory
    player = Player(level)
    # Display the maze
    display = Display(level, player)

    # Pygame parameters
    pygame.key.set_repeat(KEY_SET_REPEAT_DELAY,
                          KEY_SET_REPEAT_INTERVAL)
    pygame.time.Clock().tick(TIME_CLOCK_TICK)

# GAME LOOP ###################################################################
    loop = 1
    while loop:
        for event in pygame.event.get():
            # Close window
            if event.type == QUIT \
             or event.type == KEYDOWN \
             and event.key == K_ESCAPE:
                loop = 0
            # Keyboard reactions
            keys_events = {
             'UP': K_UP,
             'DOWN': K_DOWN,
             'LEFT': K_LEFT,
             'RIGHT': K_RIGHT}
            if event.type == KEYDOWN:
                for move, value in keys_events.items():
                    if event.key == value:
                        player.movement(move)

        # Check Inventory
        player.loot(level)

        # Meeting BadGuy
        if (player.x, player.y) == level.coord_badguy:
            # Check inventory
            if len(player.inventory_list) != NB_OBJ:
                print('YOU LOOSE.')
                loop = 0
            else:
                display.badguy_sleeping = True

        # Check Exit
        if (player.x, player.y) == level.coord_outdoor:
            # Check if badguy is sleeping
            if display.badguy_sleeping is True:
                print('YOU WIN!')
                loop = 0
            else:
                print('Bad guy is still awake.\nYOU CHEAT')
                loop = 0

        # Re-paste images
        display.repaste_display(level, player)
# END GAME LOOP ###############################################################


if __name__ == "__main__":

    main()
